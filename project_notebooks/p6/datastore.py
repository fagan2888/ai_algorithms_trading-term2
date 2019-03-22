import json
import pandas as pd

from pathlib import Path

data_path = Path('../../data/data.json')


def json_datastore(data=None, do='get'):

    if data == None:
        df = pd.read_json(data_path)
        return df['data'].values.tolist()
    elif do == 'delete':
        df = pd.DataFrame(data, columns=['data'])
        df.to_json(data_path)
        return df['data'].values.tolist()
    else:
        df = pd.read_json(data_path)
        df2 = pd.DataFrame(data, columns=['data'])
        df = pd.concat([df, df2], ignore_index=True)
        df.to_json(data_path)
        return df['data'].values.tolist()
