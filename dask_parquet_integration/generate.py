import os
import fastparquet as fp
import pyarrow as pa
import pyarrow.parquet as pq
import dask.dataframe as dd
import pandas as pd


df1 = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [1.1, 2, 3, 4],
    "C": ['a', 'b', 'c', 'd'],
    "D": pd.Categorical(['a', 'b', 'c', 'd']),
    "E": pd.to_datetime(['2017', '2018', '2019', '2020']),
})
df2 = df1.copy()
df2.index.name = 'idx'
df3 = df2.copy()
df3.columns.name = 'cidx'
PKG = os.path.dirname(__file__)
DATA = os.path.join(PKG, "data")


def namer(df, module, number, dask):
    return f'{module.__name__}-{module.__version__}-{number}-{dask}.parq'


def write_pyarrow(df, number):
    t = pa.Table.from_pandas(df)
    name = namer(df, pa, number, False)
    return pq.write_table(t, os.path.join(DATA, name))


def write_fastparquet(df, number):
    name = namer(df, fp, number, False)
    return fp.write(os.path.join(DATA, name), df)


def write_pyarrow_(df, number):
    name = os.path.join(DATA, namer(df, pa, number, True))
    dd.from_pandas(df, 2).to_parquet(name, engine="pyarrow")


def write_fastparquet_(df, number):
    name = os.path.join(DATA, namer(df, fp, number, True))
    dd.from_pandas(df, 2).to_parquet(name, engine='fastparquet')


def main():
    os.makedirs(DATA, exist_ok=True)
    for i, df in enumerate([df1, df2, df3], 1):
        for writer in [write_pyarrow, write_fastparquet,
                       write_pyarrow_, write_fastparquet_]:
            writer(df, i)


if __name__ == '__main__':
    main()
