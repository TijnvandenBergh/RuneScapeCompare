from unittest.mock import MagicMock, patch

import requests

from tests.conftest import SAMPLE_HISCORES_DATA


class TestIndexRoute:
    def test_index_no_player(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert b"Player Lookup" in response.data

    def test_index_with_valid_player(self, client):
        mock_response = MagicMock()
        mock_response.text = SAMPLE_HISCORES_DATA
        mock_response.raise_for_status = MagicMock()

        with patch("app.routes.requests.get", return_value=mock_response):
            response = client.get("/?player=TestUser")
            assert response.status_code == 200
            assert b"TestUser" in response.data
            assert b"1,500" in response.data or b"1500" in response.data

    def test_index_player_not_found(self, client):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with patch("app.routes.requests.get", return_value=mock_response):
            response = client.get("/?player=NonExistent")
            assert response.status_code == 200
            assert b"not found" in response.data

    def test_index_api_connection_error(self, client):
        with patch(
            "app.routes.requests.get",
            side_effect=requests.exceptions.ConnectionError(),
        ):
            response = client.get("/?player=TestUser")
            assert response.status_code == 200
            assert b"Could not connect" in response.data


class TestCompareRoute:
    def test_compare_no_players(self, client):
        response = client.get("/compare")
        assert response.status_code == 200
        assert b"Compare Players" in response.data

    def test_compare_with_valid_players(self, client):
        mock_response = MagicMock()
        mock_response.text = SAMPLE_HISCORES_DATA
        mock_response.raise_for_status = MagicMock()

        with patch("app.routes.requests.get", return_value=mock_response):
            response = client.get("/compare?player1=User1&player2=User2")
            assert response.status_code == 200
            assert b"User1" in response.data
            assert b"User2" in response.data

    def test_compare_first_player_not_found(self, client):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with patch("app.routes.requests.get", return_value=mock_response):
            response = client.get("/compare?player1=Bad&player2=Good")
            assert response.status_code == 200
            assert b"not found" in response.data

    def test_compare_second_player_not_found(self, client):
        good_response = MagicMock()
        good_response.text = SAMPLE_HISCORES_DATA
        good_response.raise_for_status = MagicMock()

        bad_response = MagicMock()
        bad_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with patch(
            "app.routes.requests.get", side_effect=[good_response, bad_response]
        ):
            response = client.get("/compare?player1=Good&player2=Bad")
            assert response.status_code == 200
            assert b"not found" in response.data

    def test_compare_api_error(self, client):
        with patch(
            "app.routes.requests.get",
            side_effect=requests.exceptions.ConnectionError(),
        ):
            response = client.get("/compare?player1=A&player2=B")
            assert response.status_code == 200
            assert b"Could not connect" in response.data

    def test_compare_only_one_player_provided(self, client):
        response = client.get("/compare?player1=OnlyOne")
        assert response.status_code == 200
        assert b"Compare Players" in response.data


class TestAppFactory:
    def test_create_app_testing(self, app):
        assert app.config["TESTING"] is True

    def test_create_app_default(self):
        from app import create_app

        app = create_app()
        assert app.config["DEBUG"] is True


class TestConfig:
    def test_development_config(self):
        from app import create_app

        app = create_app("development")
        assert app.config["DEBUG"] is True

    def test_testing_config(self):
        from app import create_app

        app = create_app("testing")
        assert app.config["TESTING"] is True

    def test_production_config(self):
        from app import create_app

        app = create_app("production")
        assert app.config["DEBUG"] is False

    def test_osrs_url_configured(self, app):
        assert "hiscore_oldschool" in app.config["OSRS_HISCORES_URL"]
