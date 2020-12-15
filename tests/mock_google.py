#! /usr/bin/env python3
# coding: utf-8
""" Mock for google api """
import pytest
import requests


class MockResponseGooglePositive:
    """ Class MockResponseGooglePositive """

    def __init__(self):
        """ Class initializer """

        self.status_code = 200

    @staticmethod
    def json():
        """ json response """

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
    """ mock response for google positive response """

    def mock_get(*args, **kwargs):
        """ get mock """

        return MockResponseGooglePositive()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseGoogle404:
    """ Class MockResponseGoogle404 """

    def __init__(self):
        """ Class initializer """

        self.status_code = 404


@pytest.fixture
def mock_response_google_404(monkeypatch):
    """ mock response for google 404 code response """

    def mock_get(*args, **kwargs):
        """ get mock"""

        return MockResponseGoogle404()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseGoogleNoResult:
    """ Class MockResponseGoogleNoResult """

    def __init__(self):
        """ Class initializer """

        self.status_code = 200

    @staticmethod
    def json():
        """ json response """

        return {
            "candidates": [],
            "status": "ZERO_RESULTS"
        }


@pytest.fixture
def mock_response_google_no_result(monkeypatch):
    """ mock response for google no response """

    def mock_get(*args, **kwargs):
        """ get mock"""
        return MockResponseGoogleNoResult()

    monkeypatch.setattr(requests, "get", mock_get)
