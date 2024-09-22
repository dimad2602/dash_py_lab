from dash.dependencies import Input, Output, State


def filter_data_callback(app, data_frame, filtered_data_store_id, button_id,
                         slider_id, star_size_selector_id):

    @app.callback(
        Output(component_id=filtered_data_store_id, component_property='data'),
        [Input(component_id=button_id, component_property='n_clicks')], [
            State(component_id=slider_id, component_property='value'),
            State(component_id=star_size_selector_id,
                  component_property='value')
        ])
    def filter_data(n, radius_range, star_size):
        my_data = data_frame[(data_frame['RPLANET'] > radius_range[0])
                             & (data_frame['RPLANET'] < radius_range[1])
                             & data_frame['StarSize'].isin(star_size)]
        return my_data.to_json(date_format='iso',
                               orient='split',
                               default_handler=str)
