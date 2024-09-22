import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from data import estimate_status, planet_gravity, planet_temperature
from data.relative_distance import get_relative_distance
import data.repository as repository
from components import planet_radius_selector, star_size_selector
from callbacks.celestial_and_temperature_chart_callback import filters_celestial_and_temperature_chart_callback

slider_id = 'planet-radius-slider'
star_size_selector_id = 'star-selector'
apply_button_id = 'submit-button'
temp_chart_id = 'dist-temp-chart'
celestial_chart_id = 'celestial-chart'
reletive_distance_chart_id = 'reletive_distance_chart'
mstar_tsar_chart_id = 'mstar_tsar_chart'

data_limit = 2000
""" READ DATA"""

data_frame = repository.load_data(data_limit)
data_frame = data_frame[data_frame['PER'] > 0]

#fig = px.scatter(data_frame, x='TPLANET', y='A')

data_frame = planet_temperature.get_planet_temperature(data_frame)
data_frame = planet_gravity.get_planet_gravity(data_frame)

data_frame = estimate_status.get_estimate_status(data_frame)

planet_radius_selector_component = planet_radius_selector.get_selector(
    data_frame, slider_id)

star_size_category_component = star_size_selector.get_star_size_selector(
    data_frame, star_size_selector_id)

#RELATIVE DISTANCE (distance to SUN/SUM radii)
relative_distance = get_relative_distance(data_frame)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
""" LAYOUT """

app.layout = html.Div(
    [
        dbc.Row(html.H1('Hello Dash'), style={'margin-bottom': 40}),
        dbc.Row([
            dbc.Col([
                html.Div('Select planet main semi-axis range'),
                html.Div(planet_radius_selector_component),
            ],
                    width={'size': 2}),
            dbc.Col([
                html.Div('Star size'),
                html.Div(star_size_category_component)
            ],
                    width={
                        'size': 3,
                        'offset': 1
                    }),
            dbc.Col([
                dbc.Button(
                    'Apply', id=apply_button_id, n_clicks=0, className='mr-2')
            ])
        ],
                style={'margin-bottom': 40}),
        #charts
        dbc.Row([
            dbc.Col([
                html.Div('Planet Temprature ~ Distance from the Star'),
                dcc.Graph(id=temp_chart_id),
            ],
                    width={
                        'size': 6,
                    },
                    md=6),
            dbc.Col([
                html.Div('Position on the Celestial Sphere'),
                dcc.Graph(id=celestial_chart_id)
            ],
                    md=6)
        ]),
        dbc.Row([
            dbc.Col([
                html.Div('Relative Distance (AU/SOl radii)'),
                dcc.Graph(id=reletive_distance_chart_id),
            ],
                    width={
                        'size': 6,
                    },
                    md=6),
            dbc.Col([html.Div('Star Mass ~ Star Temperature'),
                     dcc.Graph(id=mstar_tsar_chart_id)],
                    md=6)
        ],
                style={'margin-bottom': 40})
    ],
    style={
        'margin-left': '80px',
        'margin-right': '80px'
    })
""" CALLBACKS """

filters_celestial_and_temperature_chart_callback(
    app, data_frame, temp_chart_id, celestial_chart_id, slider_id,
    star_size_selector_id, reletive_distance_chart_id, mstar_tsar_chart_id,
    apply_button_id)

if __name__ == '__main__':
    app.run_server(debug=True)
