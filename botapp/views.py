import os

from flask import Flask, render_template, request, jsonify

from . query import Query
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', google_api_key=os.getenv('GOOGLE_API_MAP_KEY'))


@app.route('/question', methods=['POST'])
def question():
    """  """
    content = request.json
    response = 'Error'

    if "question" in content:
        query = Query(os.getenv('GOOGLE_API_PLACE_KEY'))
        response = query.parser(content['question'])
    print(response)
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run()
