import pytest
import requests


class MockResponseGooglePositive(object):
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "candidates": [
                {
                    "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                    "geometry": {
                        "location": {
                            "lat": 48.8975156,
                            "lng": 2.3833993
                        },
                        "viewport": {
                            "northeast": {
                                "lat": 48.89886702989273,
                                "lng": 2.384756379892722
                            },
                            "southwest": {
                                "lat": 48.89616737010729,
                                "lng": 2.382056720107278
                            }
                        }
                    },
                    "name": "OpenClassrooms"
                }
            ],
            "status": "OK"
        }


@pytest.fixture
def mock_response_google_positive(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseGooglePositive()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseGoogle404(object):
    def __init__(self):
        self.status_code = 404


@pytest.fixture
def mock_response_google_404(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseGoogle404()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseGoogleNoResult(object):
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "candidates": [],
            "status": "ZERO_RESULTS"
        }


@pytest.fixture
def mock_response_google_no_result(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseGoogleNoResult()

    monkeypatch.setattr(requests, "get", mock_get)
