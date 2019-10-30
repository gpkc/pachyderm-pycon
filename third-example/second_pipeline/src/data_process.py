import json
import os

import pandas as pd


INPUT_PATH = '/pfs/first-pipeline'
OUTPUT_PATH = '/pfs/out'


def read_config_file(filepath):
    with open(filepath) as config_file:
        config_dict = json.load(config_file)

    return config_dict


def read_csv_file(filepath):
    df = pd.read_csv(filepath)

    return df


def process_data(df):
    return df.sum()


def write_to_pachyderm(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    for column in data.keys():
        with open(os.path.join(output_path, column), 'w+') as output_file:
            output_file.write(str(data[column]))


def separate_files(files):
    """Gets the two input files and select explicitly the csv and json one.
    """
    return dict(zip(map(lambda x: os.path.splitext(x)[1][1:], files), files))


def run():
    print('Starting data process...')

    print(f'Reading from {INPUT_PATH}')
    (_, _, files) = next(os.walk(INPUT_PATH))
    print(f'Files found: {files}')
    file = files[0]

    print(f'Reading {file}...')
    csvpath = os.path.join(INPUT_PATH, file)
    data = read_csv_file(csvpath)
    print("Finished reading csv.")

    output_path = os.path.join(OUTPUT_PATH, f"{file}/")
    print(f'Result path: {output_path}')

    print('Processing data...')
    processed_data = process_data(data)

    print(f'Writing data...')
    write_to_pachyderm(processed_data, output_path)

    print('Done!')


run()
