import pandas as pd


def get_planet_temperature(data_frame):
    tp_bins = [0, 200, 400, 500, 5000]
    tp_labels = ['low', 'optimal', 'higt', 'extreme']
    data_frame['temp'] = pd.cut(data_frame['TPLANET'],
                                tp_bins,
                                labels=tp_labels)

    return data_frame
