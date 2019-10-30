import datetime
import json
import os

import numpy as np
import pandas as pd


INPUT_PATH = '/pfs/first-pipeline-input'
OUTPUT_PATH = '/pfs/out'


def read_config_file(filepath):
    with open(filepath) as config_file:
        config_dict = json.load(config_file)

    return config_dict


def generate_data(config):
    rows = config['length']
    cols = config['headers']
    return pd.DataFrame(
        np.random.randint(0, 100, size=(rows, len(cols))), columns=cols
    )


def write_to_pachyderm(data, output_path_csv):
    os.makedirs(os.path.dirname(output_path_csv), exist_ok=True)

    with open(output_path_csv, 'w+') as output_file:
        data.to_csv(output_file, header=True, index=False)


def run():
    print('Starting data ingress...')

    print(f'Reading from {INPUT_PATH}')
    (_, _, files) = next(os.walk(INPUT_PATH))
    print(f'Files found: {files}')
    file = files[0]

    today_date = datetime.date.today()
    print(f'Date: {today_date}')

    print(f'Reading {file}...')
    configpath = os.path.join(INPUT_PATH, file)
    print(f'from path {configpath}...')
    config = read_config_file(configpath)
    print(f'Config file: {config}')

    output_path_csv = os.path.join(OUTPUT_PATH, f"{config['id']}.csv")
    print(f'Report path: {output_path_csv}')

    print('Getting data...')
    data = generate_data(config)

    print(f'Writing data...')
    write_to_pachyderm(data, output_path_csv)

    print('Done!')


run()
