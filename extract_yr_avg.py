import pandas as pd
from bs4 import BeautifulSoup
import requests as re

URL = 'https://www.basketball-reference.com/players/c/curryst01.html'
response = re.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Column Titles
thead = soup.find('thead')
tr = thead.find('tr')

cols = []

for th in tr.find_all('th'):
    cols.append(th.get('data-stat'))

# Get Averages.
data = []

tbody = soup.find('tbody')
for tr in tbody.find_all('tr'):
    row = []
    season = tr.find('th').find('a').text
    row.append(season)
    for td in tr.find_all('td'):
        if td.find('a'):
            row.append(td.find('a').text)
        else:
            row.append(td.text)

    data.append(row)

yr_avg_df = pd.DataFrame(data=data, columns=cols)
yr_avg_df.to_csv('sc_yr_avg.csv', index=False)
