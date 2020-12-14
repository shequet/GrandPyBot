from botapp.query import Query
from tests.mock_google import \
    mock_response_google_positive, \
    mock_response_google_404, \
    mock_response_google_no_result


def test_google_search_response_positive_not_none(mock_response_google_positive):

    response = Query().search_in_google_place('openclassrooms')
    assert response is not None


def test_google_search_response_positive_key_name(mock_response_google_positive):

    response = Query().search_in_google_place('openclassrooms')
    assert 'name' in response


def test_google_search_response_positive_name_openclassrooms(mock_response_google_positive):

    response = Query().search_in_google_place('openclassrooms')
    assert response['name'] == 'OpenClassrooms'


def test_google_search_response_no_result(mock_response_google_no_result):

    response = Query().search_in_google_place('aaaaaaaaaaaaaaaaaaaaaaaaa')
    assert response is None


def test_google_search_response_404(mock_response_google_404):

    response = Query().search_in_google_place('')
    assert response is None


def test_google_query_response_positive_not_none(mock_response_google_positive):

    response = Query().query_google_place('openclassrooms')
    assert response is not None


def test_google_query_response_positive_key_status(mock_response_google_positive):

    response = Query().query_google_place('openclassrooms')
    assert 'status' in response.json()


def test_google_query_response_positive_key_status_ok(mock_response_google_positive):

    response = Query().query_google_place('openclassrooms')
    assert response.json()['status'] == 'OK'


def test_google_query_response_positive_candidates_gt0(mock_response_google_positive):

    response = Query().query_google_place('openclassrooms')
    assert len(response.json()['candidates']) > 0


def test_google_query_response_positive_geometry_location(mock_response_google_positive):

    response = Query().query_google_place('openclassrooms').json()
    assert response['candidates'][0]['geometry']['location']['lat'] == 48.8975156 \
           and response['candidates'][0]['geometry']['location']['lng'] == 2.3833993


def test_google_query_response_404(mock_response_google_404):

    response = Query().query_google_place('')
    assert response.status_code == 404


def test_google_query_response_no_result_status_200(mock_response_google_no_result):

    response = Query().query_google_place('aaaaaaaaaaaaaaaaaaaaaaaaa')
    assert response.status_code == 200


def test_google_query_response_no_result_candidates_key_candidates(mock_response_google_no_result):

    response = Query().query_google_place('aaaaaaaaaaaaaaaaaaaaaaaaa')
    assert 'candidates' in response.json()
