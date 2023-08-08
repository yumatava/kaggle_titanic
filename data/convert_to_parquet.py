import pandas as pd

target = [
    'train',
    'test',
]

extension = 'csv'
# extension = 'tsv'
# extension = 'zip'

for t in target:
    (pd.read_csv('./data/input/' + t + '.' + extension, encoding="utf-8"))\
        .to_parquet('./data/input/' + t + '.parquet')
