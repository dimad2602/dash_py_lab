import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from callbacks.filter_data_collback import filter_data_callback
from components.tab3_content import get_tab3_content
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
data_table_id = 'data_table'
filtered_data_store_id = 'filtered_data_store'

data_limit = 2000
""" READ DATA"""

data_frame = repository.load_data(data_limit)
data_frame = data_frame[data_frame['PER'] > 0]
data_frame['KOI'] = data_frame['KOI'].astype(int, errors='ignore')

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
"""TABS CONTENT"""
tab1_content = [
    dbc.Row([
        dbc.Col([
            html.H4('Planet Temprature ~ Distance from the Star'),
            dcc.Graph(id=temp_chart_id),
        ],
                width={
                    'size': 6,
                },
                md=6),
        dbc.Col([
            html.H4('Position on the Celestial Sphere'),
            dcc.Graph(id=celestial_chart_id)
        ],
                md=6)
    ],
            style={'margin-top': 20}),
    dbc.Row([
        dbc.Col([
            html.H4('Relative Distance (AU/SOl radii)'),
            dcc.Graph(id=reletive_distance_chart_id),
        ],
                width={
                    'size': 6,
                },
                md=6),
        dbc.Col([
            html.H4('Star Mass ~ Star Temperature'),
            dcc.Graph(id=mstar_tsar_chart_id)
        ],
                md=6)
    ],
            style={'margin-bottom': 40})
]

tab2_content = [dbc.Row(html.Div(id=data_table_id), style={'margin-top': 20})]

table_header = [
    html.Thead(html.Tr([html.Th("Field Name"),
                        html.Th("Detailds")]))
]

tab3_content = get_tab3_content()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
""" LAYOUT """

app.layout = html.Div(
    [
        dcc.Store(id=filtered_data_store_id, storage_type='session'),
        dbc.Row(html.H1('Джегло Дмитрий КИ24-02-7М'),
                style={'margin-bottom': 40}),
        dbc.Row([
            dbc.Col([
                html.H6('Select planet main semi-axis range'),
                html.Div(planet_radius_selector_component)
            ],
                    width={'size': 2}),
            dbc.Col(
                [html.H6('Star size'),
                 html.Div(star_size_category_component)],
                width={
                    'size': 3,
                    'offset': 1
                }),
            dbc.Col(
                dbc.Button(
                    'Apply', id=apply_button_id, n_clicks=0, className='mr-2'),
                align='center',
            ),
        ],
                style={'margin-bottom': 40}),
        #charts
        dbc.Tabs([
            dbc.Tab(tab1_content, label='Charts'),
            dbc.Tab(tab2_content, label='Data Table'),
            dbc.Tab(tab3_content, label='About')
        ])
    ],
    style={
        'margin-left': '80px',
        'margin-right': '80px'
    })
""" CALLBACKS """

filter_data_callback(app, data_frame, filtered_data_store_id, apply_button_id,
                     slider_id, star_size_selector_id)

filters_celestial_and_temperature_chart_callback(
    app, data_frame, temp_chart_id, celestial_chart_id, slider_id,
    star_size_selector_id, reletive_distance_chart_id, mstar_tsar_chart_id,
    data_table_id, apply_button_id, filtered_data_store_id)

if __name__ == '__main__':
    app.run_server(debug=True)
