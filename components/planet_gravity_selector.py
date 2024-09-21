import pandas as pd


def get_planet_gravity(data_frame):
    rp_bins = [0, 0.5, 2, 4, 100]
    rp_labels = ['low', 'optimal', 'high', 'extreme']
    data_frame['gravity'] = pd.cut(data_frame['RPLANET'],
                                   rp_bins,
                                   labels=rp_labels)
    return data_frame
