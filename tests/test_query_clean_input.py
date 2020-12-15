#! /usr/bin/env python3
# coding: utf-8
""" Test query class clean input """
from botapp.query import Query


def test_query_clean_input_lowercase():
    """ test query clean input lowercase """

    input_clean = Query().clean_input_user('OPENCLASSROOMS')
    assert input_clean == 'openclassrooms'


def test_query_clean_input_space():
    """ test query clean input space """

    input_clean = Query().clean_input_user(' OpenClassRooms ')
    assert input_clean == 'openclassrooms'


def test_query_clean_input_remove_words_remove_double_space():
    """ test query clean input remove words remove double space in middle """

    input_clean = Query().clean_input_user('adresse  OpenClassRooms')
    assert input_clean == 'adresse openclassrooms'


def test_query_clean_input_remove_words_01():
    """ test query clean input remove words 01 """

    input_clean = Query().clean_input_user('Est-ce que tu connais l\'adresse d\'OpenClassrooms ?')
    assert input_clean == 'l\'adresse d\'openclassrooms ?'


def test_query_clean_input_remove_words_02():
    """ test query clean input remove words 02 """

    input_clean = Query().clean_input_user('L\'adresse du musée du louvre')
    assert input_clean == 'l\'adresse musée louvre'
