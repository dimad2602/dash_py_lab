import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import requests
import pandas as pd

import plotly.express as px
import repository
from components import planet_radius_selector
from callbacks import radius_slider_callback

data_limit = 2000

data_frame = repository.load_data(data_limit)

fig = px.scatter(data_frame, x='TPLANET', y='A')

slider_id = 'planet-radius-slider'
temp_chart_id = 'dist-temp-chart'

platet_radius_selector = planet_radius_selector.get_selector(
    data_frame, slider_id)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div('Select planet main semi-axis range'),
    html.Div(platet_radius_selector,
             style={
                 'width': '400px',
                 'margin-bottom': '40px'
             }),
    html.Div('Planet Temprature ~ Distance from the Star'),
    dcc.Graph(id=temp_chart_id, figure=fig)
],
                      style={
                          'margin-left': '80px',
                          'margin-right': '80px'
                      })


radius_slider_callback(app, data_frame, temp_chart_id, slider_id)



if __name__ == '__main__':
    app.run_server(debug=True)


# @app.callback(
#     Output(component_id='dist-temp-chart', component_property='figure'),
#     Input(component_id=slider_id, component_property='value'))
# def update_dist_temp_chart(radius_range):
#     #print(radius_range)
#     chart_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
#                             & (data_frame['RPLANET'] < radius_range[1])]

#     fig = px.scatter(chart_data, x='TPLANET', y='A')

#     return fig