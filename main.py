import requests
import json
import csv
from datetime import datetime, timedelta

# Part 1: List the top 50 classical chess players
def get_top_50_classical_players() -> list:
    """Fetches the top 50 classical chess players from Lichess.

    Calls the Lichess API to retrieve the top 50 classical chess players and their ratings.

    Args:
        None

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing player information, including username and rating details.
        Returns an empty list if the API request fails.
    """
    url = "https://lichess.org/api/player/top/50/classical"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        users = data.get("users", [])
        return users
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def print_top_50_classical_players() -> None:
    """Lists the top 50 classical chess players from Lichess and print them.

    Fetches data from the Lichess API, extracts the usernames of the top 50 classical chess players,
    and prints them to the console.

    Args:
        None

    Returns:
        None
    """

    top_50_players = get_top_50_classical_players()

    #print("Top 50 Classical Chess Players:")
    [print(user["username"]) for user in top_50_players]

# Part 2: Print the rating history for the top chess player in classical chess for the last 30 calendar days.
def parsing_player_last_30_day_rating(classical_history):
    """Processes a player's classical chess rating history for the last 30 days.

    Takes a player's classical chess rating history data and processes it to create a day-by-day
    rating history for the last 30 days. If a player didn't play on a specific day, their last
    known rating is used.

    Args:
        classical_history (List[List]): List of rating history points, where each point is a list
        containing [year, month, day, rating].

    Returns:
        Dict[datetime.date, int]: Dictionary mapping dates to ratings for the last 30 days.
    """
    all_days_ratings = {}
    for point in classical_history:
        try:
            year, month, day, rating = point
            # Month is 0-indexed in the API
            date = datetime(year, month+1, day).date()
            all_days_ratings[date] = rating
        except Exception as e:
            print("Error parsing data")
            continue

    today = datetime.now().date()
    thirty_days_ago = today - timedelta(days=30)
    last_rating = max(list(all_days_ratings.keys()))
    last_30_days_ratings = {}

    for i in range(30):
        date = thirty_days_ago + timedelta(days=i)
        if date not in list(all_days_ratings.keys()) and i!=0:
            last_30_days_ratings[date] = last_rating
        elif date not in list(all_days_ratings.keys()) and i==0:
            datas_les_then_date = list(filter(lambda x: x < date, list(all_days_ratings.keys())))
            if not datas_les_then_date:
                last_30_days_ratings[date] = 0
            else:
                data_max_les_then_date = max(datas_les_then_date)
                last_30_days_ratings[date] = all_days_ratings[data_max_les_then_date]
        else:
            last_30_days_ratings[date] = all_days_ratings[date]
        last_rating = last_30_days_ratings[date]

    return last_30_days_ratings

def parsing_multiple_player_last_30_day_rating(top_players):
    """Processes rating histories for multiple players for the last 30 days.

    Fetches and processes the classical chess rating histories for multiple players
    over the last 30 days, maintaining the last known rating for days when a player
    didn't play.

    Args:
        top_players (List[Dict[str, Any]]): List of dictionaries containing player information,
        including username and rating details.

    Returns:
        Dict[str, Dict[datetime.date, int]]: Dictionary mapping player usernames to their
        rating histories (which are dictionaries mapping dates to ratings).
    """
    top_players_last_30_days_ratings = {}
    for player in top_players:
        player_name = player["username"]

        # Get the rating history
        url = f"https://lichess.org/api/user/{player_name}/rating-history"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Find classical rating history
            classical_history = None
            for perf in data:
                if perf["name"] == "Classical":
                    classical_history = perf["points"]
                    break

            if not classical_history:
                print(f"No classical rating history found for {player_name}")
                return

            player_last_30_days_ratings = parsing_player_last_30_day_rating(classical_history)
            top_players_last_30_days_ratings[player_name] = player_last_30_days_ratings
    return top_players_last_30_days_ratings


def print_last_30_day_rating_for_top_player() -> None:
    """Prints the rating history of the top classical chess player for the last 30 days.

       Args:
           None

       Returns:
           None: The function outputs the results to the console but doesn't return a value.
       """
    # Get the top player
    top_players = get_top_50_classical_players()
    if not top_players:
        print("No players found.")
        return
    top_players_last_30_days_ratings = parsing_multiple_player_last_30_day_rating(top_players)

    for player in top_players_last_30_days_ratings:
        print(player, end=', ')
        datas = top_players_last_30_days_ratings[player]
        print("{", end='')
        for data in datas:
            print(f"{data.strftime("%b %d")}: {datas[data]}", end=', ')
        print("}")


# Part 3: Create a CSV that shows the rating history for each of these 50 players, for the last 30 days.



if __name__ == '__main__':
    # # Part 1
    # top_50_players = print_top_50_classical_players()

    # Part 2
    print_last_30_day_rating_for_top_player()

    # # Part 3
    # generate_rating_csv_for_top_50_classical_players()