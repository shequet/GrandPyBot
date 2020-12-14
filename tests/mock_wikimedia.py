import pytest
import requests


class MockResponseWikimediaPositive(object):
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "batchcomplete": "",
            "continue": {
                "sroffset": 10,
                "continue": "-||"
            },
            "query": {
                "searchinfo": {
                    "totalhits": 43
                },
                "search": [
                    {
                        "ns": 0,
                        "title": "OpenClassrooms",
                        "pageid": 4338589,
                        "size": 30952,
                        "wordcount": 3149,
                        "snippet": "chez <span class=\"searchmatch\">OpenClassrooms</span> », <span class=\"searchmatch\">OpenClassrooms</span> : le blog,‎ 17 avril 2018 (lire en ligne, consulté le 11 juillet 2018) « <span class=\"searchmatch\">OpenClassrooms</span> », sur <span class=\"searchmatch\">openclassrooms</span>.com",
                        "timestamp": "2020-11-09T13:42:52Z"
                    },
                    {
                        "ns": 0,
                        "title": "Massive Open Online Course",
                        "pageid": 6436398,
                        "size": 55084,
                        "wordcount": 5703,
                        "snippet": "sur <span class=\"searchmatch\">openclassrooms</span>.com (consulté le 22 septembre 2015) « Google », sur <span class=\"searchmatch\">openclassrooms</span>.com (consulté le 22 septembre 2015) « IBM », sur <span class=\"searchmatch\">openclassrooms</span>.com",
                        "timestamp": "2020-12-14T17:53:53Z"
                    },
                    {
                        "ns": 0,
                        "title": "Broadcast (informatique)",
                        "pageid": 3363958,
                        "size": 3825,
                        "wordcount": 551,
                        "snippet": "Anycast Géocast Voir Broadcast address (en) Calculer ses plages d'adresses sur <span class=\"searchmatch\">OpenClassrooms</span> Portail de l’informatique Portail des télécommunications",
                        "timestamp": "2019-05-02T12:12:24Z"
                    },
                    {
                        "ns": 0,
                        "title": "Types de donnée du langage C",
                        "pageid": 13425095,
                        "size": 7483,
                        "wordcount": 505,
                        "snippet": "== b) { /* faire quelque chose */ } « L'allocation dynamique », sur <span class=\"searchmatch\">OpenClassrooms</span> (consulté le 25 octobre 2020) Portail de la programmation informatique",
                        "timestamp": "2020-12-11T23:06:41Z"
                    },
                    {
                        "ns": 0,
                        "title": "Compilateur",
                        "pageid": 635,
                        "size": 23027,
                        "wordcount": 2776,
                        "snippet": "« Découvrez le cours &quot;Compilation à la volée avec libtcc&quot; sur @<span class=\"searchmatch\">OpenClassrooms</span> », sur <span class=\"searchmatch\">OpenClassrooms</span> (consulté le 21 novembre 2016). « tranpiler », sur wiktionary",
                        "timestamp": "2020-08-15T12:49:38Z"
                    },
                    {
                        "ns": 0,
                        "title": "Recherche dichotomique",
                        "pageid": 842,
                        "size": 10776,
                        "wordcount": 1387,
                        "snippet": "régner (informatique) Méthode de dichotomie Severance, « Recherche dichotomique », sur <span class=\"searchmatch\">OpenClassrooms</span>, octobre 2013 Portail de l'informatique théorique",
                        "timestamp": "2020-10-24T20:29:41Z"
                    },
                    {
                        "ns": 0,
                        "title": "Percolation",
                        "pageid": 84364,
                        "size": 7795,
                        "wordcount": 875,
                        "snippet": "Hoshen-Kopelman Théorie de la percolation La percolation sur le site <span class=\"searchmatch\">OpenClassrooms</span> Article La percolation, un jeu de pavages aléatoires de Hugo Duminil-Copin",
                        "timestamp": "2020-09-08T03:02:50Z"
                    },
                    {
                        "ns": 0,
                        "title": "Unix",
                        "pageid": 3081,
                        "size": 43633,
                        "wordcount": 4699,
                        "snippet": "(consulté le 2 juillet 2017). « Mais c'est quoi, Linux ? @<span class=\"searchmatch\">OpenClassrooms</span> », sur <span class=\"searchmatch\">OpenClassrooms</span> (consulté le 3 juillet 2017). (en) Andrew Tanenbaum, « Some",
                        "timestamp": "2020-10-12T15:19:08Z"
                    },
                    {
                        "ns": 0,
                        "title": "Fonction exponentielle",
                        "pageid": 12023,
                        "size": 27945,
                        "wordcount": 3659,
                        "snippet": " « Autour de la fonction exponentielle et ses constructions », sur <span class=\"searchmatch\">OpenClassrooms</span>. (en) Foster Morrison, The Art of Modeling Dynamic Systems : Forecasting",
                        "timestamp": "2020-11-19T20:19:51Z"
                    },
                    {
                        "ns": 0,
                        "title": "Zeste de Savoir",
                        "pageid": 12431773,
                        "size": 4665,
                        "wordcount": 344,
                        "snippet": "fondée le 1er avril 2014, à la suite de changements de politique d''<span class=\"searchmatch\">OpenClassrooms</span>. Celle-ci promeut le partage de connaissances et l'auto-formation, participe",
                        "timestamp": "2020-07-05T10:10:30Z"
                    }
                ]
            }
        }


@pytest.fixture
def mock_response_wikimedia_positive(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseWikimediaPositive()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseWikimedia404(object):
    def __init__(self):
        self.status_code = 404


@pytest.fixture
def mock_response_wikimedia_404(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseWikimedia404()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseWikimediaNoResult(object):
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "batchcomplete": "",
            "query": {
                "searchinfo": {
                    "totalhits": 0
                },
                "search": []
            }
        }


@pytest.fixture
def mock_response_wikimedia_no_result(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseWikimediaNoResult()

    monkeypatch.setattr(requests, "get", mock_get)


class MockResponseWikimediaExtracts(object):
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "batchcomplete": "",
            "query": {
                "pages": {
                    "4338589": {
                        "pageid": 4338589,
                        "ns": 0,
                        "title": "OpenClassrooms",
                        "extract": "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ou historiquement par des bénévoles. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé « interface de rédaction » puis « Course Lab ». De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les sciences."
                    }
                }
            }
        }


@pytest.fixture
def mock_response_wikimedia_extracts(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseWikimediaExtracts()

    monkeypatch.setattr(requests, "get", mock_get)
