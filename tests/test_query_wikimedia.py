from botapp.query import Query
from tests.mock_wikimedia import \
    mock_response_wikimedia_positive, \
    mock_response_wikimedia_404, \
    mock_response_wikimedia_no_result, \
    mock_response_wikimedia_extracts


def test_wikimedia_response_positive_is_not_none(mock_response_wikimedia_positive):

    response = Query().search_in_wikimedia('openclassrooms')
    assert response is not None


def test_wikimedia_response_positive_key_title(mock_response_wikimedia_positive):

    response = Query().search_in_wikimedia('openclassrooms')
    assert 'title' in response


def test_wikimedia_response_positive_key_snippet(mock_response_wikimedia_positive):

    response = Query().search_in_wikimedia('openclassrooms')
    assert 'snippet' in response


def test_wikimedia_response_no_result(mock_response_wikimedia_no_result):

    response = Query().search_in_wikimedia('aaaaaaaaaaaaaaaaaaaaaaaaa')
    assert response is None


def test_wikimedia_response_404(mock_response_wikimedia_404):

    response = Query().search_in_google_place('')
    assert response is None


def test_wikimedia_response_extract_is_not_none(mock_response_wikimedia_extracts):

    response = Query().query_wikimedia_desciption('4338589')
    assert response.json() is not None


def test_wikimedia_search_desciption_extract_is_not_none(mock_response_wikimedia_extracts):

    response = Query().search_description_in_wikimedia(4338589)
    assert response is not None


def test_wikimedia_search_desciption_extract_len_size(mock_response_wikimedia_extracts):

    response = Query().search_description_in_wikimedia(4338589)
    assert len(response) >= 500
