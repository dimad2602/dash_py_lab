from dash.dependencies import Input, Output, State
import plotly.express as px


#Больше не используется
def filters_temp_chart_callback(app, data_frame, temp_chart_id, slider_id,
                                star_size_selector_id, button_id):

    @app.callback(
        Output(component_id=temp_chart_id, component_property='figure'),
        [Input(component_id=button_id, component_property='n_clicks')], [
            State(component_id=slider_id, component_property='value'),
            State(component_id=star_size_selector_id,
                  component_property='value')
        ])
    def update_dist_temp_chart(n, radius_range, star_size):
        chart_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
                                & (data_frame['RPLANET'] < radius_range[1])
                                & data_frame['StarSize'].isin(star_size)]
        fig = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')
        return fig
