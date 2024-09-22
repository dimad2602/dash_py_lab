from dash.dependencies import Input, Output, State
import plotly.express as px


def filters_celestial_and_temperature_chart_callback(
        app, data_frame, temp_chart_id, celestial_chart_id, slider_id,
        star_size_selector_id, reletive_distance_chart_id, mstar_tsar_chart_id, button_id):

    @app.callback([
        Output(component_id=celestial_chart_id, component_property='figure'),
        Output(component_id=temp_chart_id, component_property='figure'),
        Output(component_id=reletive_distance_chart_id,
               component_property='figure'),
        Output(component_id=mstar_tsar_chart_id,
               component_property='figure')
    ], [Input(component_id=button_id, component_property='n_clicks')], [
        State(component_id=slider_id, component_property='value'),
        State(component_id=star_size_selector_id, component_property='value')
    ])
    def update_charts(n, radius_range, star_size):
        chart_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
                                & (data_frame['RPLANET'] < radius_range[1])
                                & data_frame['StarSize'].isin(star_size)]

        # Фигуры для графиков
        fig_celestial = px.scatter(chart_data,
                                   x='RA',
                                   y='DEC',
                                   size='RPLANET',
                                   color='status')

        fig_temp = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')

        # График гистограммы расстояний
        fig_distance = px.histogram(chart_data,
                                    x='relative_dist',
                                    color='status',
                                    barmode='overlay',
                                    marginal='violin')

        fig_distance.add_vline(x=1,
                               y0=0,
                               y1=155,
                               annotation_text='Earth',
                               line_dash='dot')

        fig_mstar = px.scatter(chart_data,
                               x='MSTAR',
                               y='TSTAR',
                               size='RPLANET',
                               color='status')

        return fig_celestial, fig_temp, fig_distance, fig_mstar
