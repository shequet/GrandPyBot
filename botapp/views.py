#! /usr/bin/env python3
# coding: utf-8
""" Flask router """
import os
from flask import Flask, render_template, request, jsonify

from . query import Query
app = Flask(__name__)


@app.route('/')
def index():
    """ Site root page """

    return render_template('index.html', google_api_key=os.getenv('GOOGLE_API_MAP_KEY'))


@app.route('/question', methods=['POST'])
def question():
    """ page for the ajax type question """

    content = request.json
    response = 'Error'

    if "question" in content:
        query = Query(os.getenv('GOOGLE_API_PLACE_KEY'))
        response = query.get(content['question'])
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run()
