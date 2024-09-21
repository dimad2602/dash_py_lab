import numpy as np


def get_estimate_status(data_frame):
    # Присваиваем 'promising' если 'temp' и 'gravity' равны 'optimal'
    data_frame['status'] = np.where((data_frame['temp'] == 'optimal') &
                                    (data_frame['gravity'] == 'optimal'),
                                    'promising', None)

    # Присваиваем 'challenging' если 'temp' равен 'optimal' и 'gravity' в ['low', 'high']
    data_frame['status'] = np.where(
        (data_frame['temp'] == 'optimal') &
        (data_frame['gravity'].isin(['low', 'high'])), 'challenging',
        data_frame['status'])

    # Присваиваем 'challenging' если 'temp' в ['low', 'high'] и 'gravity' равен 'optimal'
    data_frame['status'] = np.where((data_frame['temp'].isin(['low', 'high']))
                                    & (data_frame['gravity'] == 'optimal'),
                                    'challenging', data_frame['status'])

    # Все оставшиеся значения присваиваются 'extreme'
    data_frame['status'] = data_frame['status'].fillna('extreme')

    # Группируем и выводим количество по статусам
    #print(data_frame.groupby('status')['ROW'].count())
    return data_frame
