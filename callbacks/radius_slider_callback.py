from dash.dependencies import Input, Output
import plotly.express as px


def radius_slider_callbacks(app, data_frame, temp_chart_id, slider_id):

    @app.callback(
        Output(component_id=temp_chart_id, component_property='figure'),
        Input(component_id=slider_id, component_property='value'))
    def update_dist_temp_chart(radius_range):
        chart_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
                                & (data_frame['RPLANET'] < radius_range[1])]
        fig = px.scatter(chart_data, x='TPLANET', y='A')
        return fig
