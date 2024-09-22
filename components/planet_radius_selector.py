from dash import dcc


def get_selector(data_frame, slider_id):
    selector = dcc.RangeSlider(id=slider_id,
                               min=min(data_frame['RPLANET'], ),
                               max=max(data_frame['RPLANET'], ),
                               marks={
                                   5: '5',
                                   10: '10',
                                   20: '20'
                               },
                               step=1,
                               value=[
                                   min(data_frame['RPLANET'], ),
                                   max(data_frame['RPLANET'], ),
                               ])
    return selector
