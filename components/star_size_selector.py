import pandas as pd
import dash_core_components as dcc

def get_star_size_selector(data_frame, star_size_selector_id):
    bins = [0, 0.8, 1.2, 100]
    names = ['small', 'similar', 'bigger']
    data_frame['StarSize'] = pd.cut(data_frame['RSTAR'], bins, labels=names)
    
    options = []
    
    for i in names:
        options.append({'label': i, 'value': i})
    
    star_size_selector = dcc.Dropdown(
        id = star_size_selector_id,
        options=options,
        value =['small', 'similar', 'bigger'],
        multi=True
    )
    return star_size_selector
