import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine
from sklearn.base import TransformerMixin
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def missing_predicate(db, predicate, percentage, seed):
    df = db.copy()
    df_p = df[predicate]
    data = df_p.values
    modified = dropout(data, percentage, seed)
    df = df.drop([predicate], axis=1)
    df = df.assign(readmitted=pd.Series(modified))
    return df



table_name = 'diabetes'
connection = pg.connect("dbname=large_experiment_missing_predicate user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)

predicate = 'readmitted'

mlist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#mlist = [0.8]

print("Data missing export to Postgre")
for i in mlist:
    for j in range(100):
        #print(int(i * 100), j)
        x = int(i * 100)
        #print(df)
        #print(df.columns.to_series().groupby(df.dtypes).groups)
        # db missing is db with row contains missing drop 
        # db NaN is db with row contain missing keep 
        table_name = "db_" + str(x) + "rand_missing_predicate" + str(j+1)


        df = db.copy()
        
        new_df= missing_predicate(df, predicate, i, j)

        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/large_experiment_missing_predicate')
        c = engine.connect()
        conn = c.connection

        print("Exporting...", table_name)
        new_df.to_sql(table_name, engine)
        #new_df_attr.dropna(inplace=True)
