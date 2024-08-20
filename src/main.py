import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd


def get_game_url(game_id):
    """Constructs the full URL for a given game ID."""
    base_url = 'https://understat.com/match/'
    return base_url + str(game_id)


def fetch_game_data(url):
    """Fetches content from the URL and returns a BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad requests
    return BeautifulSoup(response.content, 'lxml')


def extract_json(script):
    """Extracts and returns JSON data from a script tag, handling cases where the pattern is not found."""
    match = re.search(r'JSON\.parse\(\'(.*?)\'\)', script.text)
    if match:
        json_text = match.group(1)
        json_text = json_text.encode().decode('unicode_escape')
        return json.loads(json_text)
    else:
        return None  # Or handle the absence of a match as appropriate


def find_shots_data_script(soup):
    """Searches through script tags to find the 'shotsData' script and extracts JSON."""
    scripts = soup.find_all('script')
    for script in scripts:
        if 'shotsData' in script.text:
            return extract_json(script)
    return None


def main():
    try:
        game_id = input('Please enter a game id: ')
        url = get_game_url(game_id)
        print(f"Fetching data from URL: {url}")

        soup = fetch_game_data(url)
        shots_data = find_shots_data_script(soup)

        if shots_data:
            # Pretty print the JSON data
            print(json.dumps(shots_data, indent=4))
            return shots_data
        else:
            return ("No 'shotsData' script was found containing JSON.")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    data = main()
    print(f'Zac test data {data}')
    x = []
    y = []
    xg = []
    team = []
    data_away = data['a']
    data_home = data['h']
    print(f'zac test data_home {json.dumps(
        data_home, indent=4)} \r\n {len(data_home)}')
    for k in data_home:
        x.append(k['X'])
        y.append(k['Y'])
        xg.append(k['xG'])
        team.append(k['h_team'])

    for k in data_away:
        x.append(k['X'])
        y.append(k['Y'])
        xg.append(k['xG'])
        team.append(k['a_team'])

    # create the dataframe
    col_names = ['x', 'y', 'xG', 'team']
    data_frame = pd.DataFrame([x, y, xg, team], index=col_names)
    flipped = data_frame.T
    print(flipped)
