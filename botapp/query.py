#! /usr/bin/env python3
# coding: utf-8
""" Query class """
import random
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Query:
    """ Query class Find the answers to a question on google and wikimedia """

    def __init__(self, google_api_place_key=''):
        """ Class initializer """

        nltk.download('stopwords')
        nltk.download('punkt')

        self.stop_words = stopwords.words('french')
        self.stop_words += ['connais', 'est-ce', 'grandpy', 'salut', '!']

        self.google_api_place_key = google_api_place_key

    def get(self, search_input):
        """ return the answer to the question """

        search_input_clean = self.clean_input_user(search_input)

        wikimedia = self.search_in_wikimedia(search_input_clean)
        if wikimedia is not None and 'pageid' in wikimedia:
            wikimedia['description'] = self.search_description_in_wikimedia(wikimedia['pageid'])
        return {
            'beginning_phrase': self.beginning_response(),
            'google': self.search_in_google_place(search_input_clean),
            'wikimedia': wikimedia,
        }

    def clean_input_user(self, search_input):
        """ text cleaning """

        word_tokens = word_tokenize(search_input.lower())
        filtered_sentence = [w for w in word_tokens if w not in self.stop_words]

        return ' '.join(filtered_sentence)

    def beginning_response(self):
        """ random beginning of sentence """

        return random.choice((
            'Bien sûr mon poussin !',
            'Voilà ma réponse mon coco !',
            'Voici ma meilleure réponse !'))

    def search_in_google_place(self, search):
        """ search for the phrase in the google api """

        response = self.query_google_place(search)

        if response.status_code == 200:
            content = response.json()

            if len(content['candidates']) > 0 and content['status'] == 'OK':
                return content['candidates'][0]

        return None

    def query_google_place(self, search):
        """ request on google api """

        return requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
                            'input={search}&inputtype=textquery&'
                            'fields=formatted_address,name,geometry&'
                            'key={google_api_place_key}'.
                            format(search=search, google_api_place_key=self.google_api_place_key))

    def search_in_wikimedia(self, search):
        """ search for the phrase in the wikimedia api """

        response = self.query_wikimedia(search)

        if response.status_code == 200:
            content = response.json()

            if len(content['query']['search']) > 0:
                return content['query']['search'][0]

        return None

    def query_wikimedia(self, search):
        """ request on wikimedia api """

        return requests.get('https://fr.wikipedia.org/w/api.php?'
                            'action=query&list=search&format=json&'
                            'srsearch={search}'.format(search=search))

    def search_description_in_wikimedia(self, pageids):
        """ search the description on the wikimedia api """

        response = self.query_wikimedia_desciption(pageids)

        if response.status_code == 200:
            content = response.json()
            return content['query']['pages'][str(pageids)]['extract']

        return None

    def query_wikimedia_desciption(self, pageids):
        """ search request for the description on the wikimedia API """

        return requests.get('https://fr.wikipedia.org/w/api.php?'
                            'action=query&prop=extracts&explaintext=1&exsentences=5&format=json&'
                            'pageids={pageids}'.format(pageids=pageids))
