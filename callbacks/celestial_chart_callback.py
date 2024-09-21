from dash.dependencies import Input, Output
import plotly.express as px


def filters_celestial_chart_callback(app, data_frame, celestial_chart_id,
                                     slider_id, star_size_selector_id):

    @app.callback(
        Output(component_id=celestial_chart_id, component_property='figure'), [
            Input(component_id=slider_id, component_property='value'),
            Input(component_id=star_size_selector_id,
                  component_property='value')
        ])
    def update_celestial_chart(radius_range, star_size):
        chart_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
                                & (data_frame['RPLANET'] < radius_range[1])
                                & data_frame['StarSize'].isin(star_size)]
        fig = px.scatter(chart_data,
                         x='RA',
                         y='DEC',
                         size='RPLANET',
                         color='status')
        return fig
