import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Query:

    def __init__(self, google_api_place_key):
        """ Class initialiser """
        nltk.download('stopwords')
        nltk.download('punkt')

        self.stop_words = stopwords.words('french')
        self.stop_words += ['connais', 'est-ce', 'grandpy', 'salut', '!']

        self.google_api_place_key = google_api_place_key

    def parser(self, search_input):
        search_input = search_input.lower()
        word_tokens = word_tokenize(search_input)
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words]

        search_input_clean = ' '.join(filtered_sentence)
        print(search_input_clean)
        return {
            'google': self.search_in_google_place(search_input_clean),
            'wikimedia': self.search_in_wikimedia(search_input_clean),
        }

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

