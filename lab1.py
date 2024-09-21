import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import repository
from components import planet_radius_selector
from callbacks.radius_slider_callback import radius_slider_callback

slider_id = 'planet-radius-slider'
temp_chart_id = 'dist-temp-chart'

data_limit = 2000
""" READ DATA"""

data_frame = repository.load_data(data_limit)
data_frame = data_frame[data_frame['PER'] > 0]

#fig = px.scatter(data_frame, x='TPLANET', y='A')

platet_radius_selector = planet_radius_selector.get_selector(
    data_frame, slider_id)

app = dash.Dash(__name__)
""" LAYOUT """

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div('Select planet main semi-axis range'),
    html.Div(platet_radius_selector,
             style={
                 'width': '400px',
                 'margin-bottom': '40px'
             }),
    html.Div('Planet Temprature ~ Distance from the Star'),
    dcc.Graph(id=temp_chart_id)
],
                      style={
                          'margin-left': '80px',
                          'margin-right': '80px'
                      })
""" CALLBACKS """
radius_slider_callback(app, data_frame, temp_chart_id, slider_id)

if __name__ == '__main__':
    app.run_server(debug=True)
