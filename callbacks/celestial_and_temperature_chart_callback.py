from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from dash import dash_table
from dash import html
import pandas as pd
#Design settings

CHARTS_TEMPLATE = go.layout.Template(
    layout=dict(font=dict(family='Century Gothic', size=14),
                legend=dict(orientation='h', title_text='', x=0, y=1.1)))

COLOR_STATUS_VALUES = ['lightgray', '#1F85DE', '#f90f04']  #'#62de1f'


def filters_celestial_and_temperature_chart_callback(
        app, data_frame, temp_chart_id, celestial_chart_id, slider_id,
        star_size_selector_id, reletive_distance_chart_id, mstar_tsar_chart_id,
        data_table_id, button_id, filter_data):

    @app.callback(
        [
            Output(component_id=celestial_chart_id,
                   component_property='figure'),
            Output(component_id=temp_chart_id, component_property='figure'),
            Output(component_id=reletive_distance_chart_id,
                   component_property='figure'),
            Output(component_id=mstar_tsar_chart_id,
                   component_property='figure'),
            Output(component_id=data_table_id, component_property='children')
        ],
        [Input(component_id=filter_data, component_property='data')],
    )
    def update_charts(data):
        chart_data = pd.read_json(data, orient='split')

        # Фигуры для графиков
        fig_celestial = px.scatter(chart_data,
                                   x='RA',
                                   y='DEC',
                                   size='RPLANET',
                                   color='status',
                                   color_discrete_sequence=COLOR_STATUS_VALUES)

        fig_celestial.update_layout(template=CHARTS_TEMPLATE)

        fig_temp = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')

        fig_temp.update_layout(template=CHARTS_TEMPLATE)

        # График гистограммы расстояний
        fig_distance = px.histogram(chart_data,
                                    x='relative_dist',
                                    color='status',
                                    barmode='overlay',
                                    marginal='box')  #marginal='violin'

        fig_distance.add_vline(x=1,
                               y0=0,
                               y1=155,
                               annotation_text='Earth',
                               line_dash='dot')

        fig_distance.update_layout(template=CHARTS_TEMPLATE)

        fig_mstar = px.scatter(chart_data,
                               x='MSTAR',
                               y='TSTAR',
                               size='RPLANET',
                               color='status',
                               color_discrete_sequence=COLOR_STATUS_VALUES)

        fig_mstar.update_layout(template=CHARTS_TEMPLATE)

        #DATA TABLE
        raw_data = chart_data.drop(
            ['relative_dist', 'StarSize', 'ROW', 'temp', 'gravity'], axis=1)

        tb1 = dash_table.DataTable(data=raw_data.to_dict('records'),
                                   columns=[{
                                       'name': i,
                                       'id': i
                                   } for i in raw_data.columns],
                                   style_data={
                                       'width': '100px',
                                       'maxWidth': '100px',
                                       'minWidth': '100px'
                                   },
                                   style_header={'textAlign': 'center'},
                                   page_size=40)

        html_tb1 = [html.H4('Raw Data'), tb1]

        return fig_celestial, fig_temp, fig_distance, fig_mstar, html_tb1
