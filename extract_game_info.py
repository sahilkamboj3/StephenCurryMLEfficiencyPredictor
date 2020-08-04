import pandas as pd
from bs4 import BeautifulSoup
import requests as re

year = 2010

data = {
    'mp': [],
    'fg': [],
    'fga': [],
    'fg_pct': [],
    'fg3': [],
    'fg3a': [],
    'fg3_pct': [],
    'ft': [],
    'fta': [],
    'ft_pct': [],
    'orb': [],
    'drb': [],
    'trb': [],
    'ast': [],
    'stl': [],
    'blk': [],
    'pf': [],
    'tov': [],
    'pts': [],
    'plus_minus': []
}

while year < 2021:
    sc_url = f'https://www.basketball-reference.com/players/c/curryst01/gamelog/{year}/'

    response = re.get(sc_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find_all('tbody')
    rows = table[0].find_all('tr')

    for row in rows:
        for td in row.find_all('td'):
            stat = td.get('data-stat')
            if stat in data:
                val = td.text
                if val == "":
                    val = None

                data[stat].append(val)

    year += 1

df = pd.DataFrame(data=data)
df.to_csv('sc_stats.csv', index=False)
