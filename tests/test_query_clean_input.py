from botapp.query import Query


def test_query_clean_input_lowercase():

    input_clean = Query().clean_input_user('OPENCLASSROOMS')
    assert input_clean == 'openclassrooms'


def test_query_clean_input_space():

    input_clean = Query().clean_input_user(' OpenClassRooms ')
    assert input_clean == 'openclassrooms'


def test_query_clean_input_remove_words_remove_double_space():

    input_clean = Query().clean_input_user('adresse  OpenClassRooms')
    assert input_clean == 'adresse openclassrooms'


def test_query_clean_input_remove_words_01():

    input_clean = Query().clean_input_user('Est-ce que tu connais l\'adresse d\'OpenClassrooms ?')
    assert input_clean == 'l\'adresse d\'openclassrooms ?'


def test_query_clean_input_remove_words_02():

    input_clean = Query().clean_input_user('L\'adresse du musée du louvre')
    assert input_clean == 'l\'adresse musée louvre'




