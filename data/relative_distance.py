import pandas as pd


def get_relative_distance(data_frame):
    data_frame.loc[:, 'relative_dist'] = data_frame['A'] / data_frame['RSTAR']

    return data_frame
