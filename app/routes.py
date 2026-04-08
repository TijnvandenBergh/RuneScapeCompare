import requests
from flask import Blueprint, current_app, render_template, request

from app.models.player import Player

main = Blueprint("main", __name__)


def fetch_player_data(username):
    """Fetch player data from the OSRS Hiscores API."""
    url = current_app.config["OSRS_HISCORES_URL"]
    response = requests.get(url, params={"player": username}, timeout=10)
    response.raise_for_status()
    return response.text


@main.route("/")
def index():
    """Home page — optionally look up a player."""
    username = request.args.get("player")
    player = None
    error = None

    if username:
        try:
            data = fetch_player_data(username)
            player = Player(username, data)
        except requests.exceptions.HTTPError:
            error = f"Player '{username}' not found on the OSRS Hiscores."
        except requests.exceptions.RequestException:
            error = (
                "Could not connect to the OSRS Hiscores API. Please try again later."
            )

    return render_template("home.html", player=player, error=error)


@main.route("/compare")
def compare():
    """Compare two players side by side."""
    player1_name = request.args.get("player1")
    player2_name = request.args.get("player2")
    player1 = None
    player2 = None
    error = None

    if player1_name and player2_name:
        try:
            data1 = fetch_player_data(player1_name)
            player1 = Player(player1_name, data1)
        except requests.exceptions.HTTPError:
            error = f"Player '{player1_name}' not found."
        except requests.exceptions.RequestException:
            error = "Could not connect to the OSRS Hiscores API."

        if not error:
            try:
                data2 = fetch_player_data(player2_name)
                player2 = Player(player2_name, data2)
            except requests.exceptions.HTTPError:
                error = f"Player '{player2_name}' not found."
            except requests.exceptions.RequestException:
                error = "Could not connect to the OSRS Hiscores API."

    return render_template(
        "compare.html", player1=player1, player2=player2, error=error
    )
