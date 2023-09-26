import pandas as pd
import requests
from io import StringIO


spreads_csv_url = "https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data?select=spreadspoke_scores.csv"
response = requests.get(spreads_csv_url)

if response.status_code == 200:
    spreads = pd.read_csv(StringIO(response.text), on_bad_lines='skip')
else:
    print(f"error reading spreads - error code {response.status_code}", )

