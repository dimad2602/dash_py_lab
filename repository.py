import requests
import pandas as pd

import plotly.express as px


def load_data(data_limit):
    response = requests.get(
        f'http://asterank.com/api/kepler?query={{}}&limit={data_limit}')
    data_frame = pd.json_normalize(response.json())
    return data_frame
