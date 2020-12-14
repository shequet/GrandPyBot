import random

import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Query:

    def __init__(self, google_api_place_key=''):
        """ Class initialiser """
        nltk.download('stopwords')
        nltk.download('punkt')

        self.stop_words = stopwords.words('french')
        self.stop_words += ['connais', 'est-ce', 'grandpy', 'salut', '!']

        self.google_api_place_key = google_api_place_key

    def parser(self, search_input):

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
        word_tokens = word_tokenize(search_input.lower())
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words]

        return ' '.join(filtered_sentence)

    def beginning_response(self):
        return random.choice((
            'Bien sûr mon poussin !',
            'Voilà ma réponse mon coco !',
            'Voici ma meilleure réponse !'))

    def search_in_google_place(self, search):
        response = self.query_google_place(search)

        if response.status_code == 200:
            content = response.json()

            if len(content['candidates']) > 0 and content['status'] == 'OK':
                return content['candidates'][0]
        else:
            return None

    def query_google_place(self, search):

        return requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
                                'input={search}&inputtype=textquery&'
                                'fields=formatted_address,name,geometry&'
                                'key={google_api_place_key}'.format(
            search=search,
            google_api_place_key=self.google_api_place_key))

    def search_in_wikimedia(self, search):
        response = self.query_wikimedia(search)

        if response.status_code == 200:
            content = response.json()

            if len(content['query']['search']) > 0:
                return content['query']['search'][0]
        else:
            return None

    def query_wikimedia(self, search):
        return requests.get('https://fr.wikipedia.org/w/api.php?'
                            'action=query&list=search&format=json&srsearch={search}'.format(search=search))

    def search_description_in_wikimedia(self, pageids):
        response = self.query_wikimedia_desciption(pageids)

        if response.status_code == 200:
            content = response.json()
            print(content)
            return content['query']['pages'][str(pageids)]['extract']
        else:
            return None

    def query_wikimedia_desciption(self, pageids):
        return requests.get('https://fr.wikipedia.org/w/api.php?'
                            'action=query&prop=extracts&explaintext=1&exsentences=5&format=json&pageids={pageids}'.format(pageids=pageids))
