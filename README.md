# Chess Rankings Analyzer

A Python application that interacts with the Lichess API to retrieve, analyze, and export chess player rankings and rating histories.

## Project Overview

This application provides three main functionalities:

1. **List Top Players**: Lists the top 50 classical chess players from Lichess.
2. **Track Top Player's Rating**: Shows the rating history of the top player in classical chess for the last 30 days.
3. **Generate Comprehensive CSV**: Creates a CSV file with the rating history for all 50 top players over the last 30 days.

## Features

- Retrieves data from Lichess API without requiring authentication
- Maintains consistent player ratings across days when no games were played
- Exports data in an easily readable CSV format for further analysis
- Properly handles missing data and API error responses

## Requirements

- Python 3.9+
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/henriqueSpencer/commure-chalenge.git
   cd chess-rankings-analyzer
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   # activate the virtual environment
   poetry env activate
   ```

### Running specific parts:

You can modify the `__main__` block in the script to run only specific parts if needed:

```python
if __name__ == '__main__':
    # Part 1: Uncomment to run
    # print("Top 50 classical chess players:")
    # print_top_50_classical_players()

    # Part 2: Uncomment to run 
    # print("Rating history for the top chess player:")
    # print_last_30_day_rating_for_top_player()

    # Part 3: Uncomment to run
    # generate_rating_csv_for_top_50_classical_players()
```

## Output

- **Part 1**: Displays usernames of the top 50 classical chess players on Lichess.
- **Part 2**: Shows the rating history of the top classical chess player over the last 30 days in the format: `username, {date1: rating1, date2: rating2, ...}`.
- **Part 3**: Creates a CSV file named `top_50_classical_players_ratings.csv` with the following structure:
  - First column: Player's username
  - Columns 2-32: Daily ratings over the last 30 days

## API Documentation

This project uses the [Lichess API](https://lichess.org/api) with the following endpoints:

- `/api/player/top/50/classical` - Get top 50 classical chess players
- `/api/user/{username}/rating-history` - Get rating history for a specific player

## Error Handling

The application includes error handling for:
- Failed API requests
- Missing or incomplete player data
- Data parsing errors


## License

[MIT License](LICENSE)