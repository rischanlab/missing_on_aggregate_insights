import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine



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

def randZipf(n, alpha, numSamples, seed):
    # Calculate Zeta values from 1 to n:
    tmp = np.power( np.arange(1, n+1), -alpha )
    zeta = np.r_[0.0, np.cumsum(tmp)]
    # Store the translation map:
    distMap = [x / zeta[-1] for x in zeta]
    # Generate an array of uniform 0-1 pseudo-random values:
    np.random.seed(seed)
    u = np.random.random(numSamples)
    # bisect them with distMap
    v = np.searchsorted(distMap, u)
    samples = [t-1 for t in v]
    return samples

def percentage_missing_zipf(N_samples, alpha, seed):

    s = randZipf(8, alpha, N_samples, seed)
    unique, counts = np.unique(s, return_counts=True)
    d = dict(zip(unique, counts / N_samples))
    return d

def missing_data_attr(db, N_samples, alpha, seed, percent):
    rank = percentage_missing_zipf(N_samples, alpha, seed)
    df = db.copy()

    gender = df['gender'].values
    gender = dropout(gender, percent*rank[0], seed)

    #admission_source_id = df['admission_source_id'].values
    #admission_source_id = dropout(admission_source_id, rank[2], seed)

    admission_type_id = df['admission_type_id'].values
    admission_type_id = dropout(admission_type_id, percent*rank[1], seed)

    #diabetesmed = df['diabetesmed'].values
    #diabetesmed = dropout(diabetesmed, rank[4], seed)

    age = df['age'].values
    age = dropout(age, percent*rank[2], seed)

    insulin = df['insulin'].values
    insulin = dropout(insulin, percent*rank[3], seed)

    race = df['race'].values
    race = dropout(race, percent*rank[4], seed)

    #max_glu_serum = df['max_glu_serum'].values
    #max_glu_serum = dropout(max_glu_serum, rank[8], seed)

    diag_1 = df['diag_1'].values
    diag_1 = dropout(diag_1, percent*rank[5], seed)

    #a1cresult = df['a1cresult'].values
    #a1cresult = dropout(a1cresult, rank[10], seed)

    change = df['change'].values
    change = dropout(change, percent*rank[6], seed)

    #discharge_disposition_id = df['discharge_disposition_id'].values
    #discharge_disposition_id = dropout(discharge_disposition_id, rank[12], seed)

    readmitted = df['readmitted'].values
    readmitted = dropout(readmitted, percent*rank[7], seed)

        
    frame = { 'gender': gender,
            'admission_type_id': admission_type_id,
             'age': age, 'insulin': insulin,
             'race': race,
             'diag_1': diag_1,
             'change': change,
            'readmitted': readmitted       
            } 

    missing_attr = pd.DataFrame(frame)

    return missing_attr

def missing_data_measure(db, N_samples, alpha, seed, percent):

    rank = percentage_missing_zipf(N_samples, alpha, seed)
    df = db.copy()

    number_emergency = df['number_emergency'].values
    number_emergency = dropout(number_emergency, percent*rank[0], seed)

    number_outpatient = df['number_outpatient'].values
    number_outpatient = dropout(number_outpatient, percent*rank[1], seed)

    number_inpatient = df['number_inpatient'].values
    number_inpatient = dropout(number_inpatient, percent*rank[2], seed)

    number_diagnoses = df['number_diagnoses'].values
    number_diagnoses = dropout(number_diagnoses, percent*rank[3], seed)

    num_procedures = df['num_procedures'].values
    num_procedures = dropout(num_procedures, percent*rank[4], seed)

    num_medications = df['num_medications'].values
    num_medications = dropout(num_medications, percent*rank[5], seed)

    time_in_hospital = df['time_in_hospital'].values
    time_in_hospital = dropout(time_in_hospital, percent*rank[6], seed)

    num_lab_procedures = df['num_lab_procedures'].values
    num_lab_procedures = dropout(num_lab_procedures, percent*rank[7], seed)


    frame = { 'number_emergency': number_emergency, 'number_outpatient': number_outpatient,
            'number_inpatient': number_inpatient, 'number_diagnoses': number_diagnoses,
             'num_procedures': num_procedures, 'num_medications': num_medications,
             'time_in_hospital': time_in_hospital, 'num_lab_procedures': num_lab_procedures    
            } 

    missing_measure = pd.DataFrame(frame)
    return missing_measure


a_columns = ['gender',
             'admission_type_id',
             'age',
             'insulin',
             'race',
             'diag_1',
             'change',
             'readmitted']
m_columns = ['number_emergency',
             'number_outpatient',
             'number_inpatient',
             'number_diagnoses',
             'num_procedures',
             'num_medications',
             'time_in_hospital',
             'num_lab_procedures']

table_name = 'diabetes'
connection = pg.connect("dbname=same_len_col_large_experiment_zipf_missing user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)

df = db.copy()
df_attr = df.select_dtypes(['object'])
df_attr = df_attr.reindex(columns=a_columns)
df_measure = df.select_dtypes(['int64']).astype(float)
df_measure = df_measure.reindex(columns=m_columns)


mlist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
a_list = [1.01, 1.03, 1.06, 1.07, 1.1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
N_samples = 784416

print("Data missing export to Postgre")
for i in mlist:
    for a in a_list:
        for j in range(20):
            x = int(i * 100)
            #print(int(i * 100), j)
            #print(df)
            #print(df.columns.to_series().groupby(df.dtypes).groups)
            # db missing is db with row contains missing drop
            # db NaN is db with row contain missing keep
            y = int(a * 100)
            table_name1 = "db_" + str(x) + "zipf" + str(y) + "_missing_attr" + str(j+1)
            table_name2 = "db_" + str(x) + "zipf" + str(y) + "_missing_measure" + str(j + 1)

            df = db.copy()
            new_df_a_m = db.copy()
            df_attr = df.select_dtypes(['object'])
            #df_float = df.select_dtypes(['float'])
            df_measure = df.select_dtypes(['int64']).astype(float)
            df_attr_missing = missing_data_attr(df_attr, N_samples, a, j, i)
            new_df_attr = pd.concat([df_attr_missing, df_measure], axis=1, ignore_index=False, sort=False)
            df_measure_missing = missing_data_measure(df_measure, N_samples, a, j, i)
            new_df_measure = pd.concat([df_attr, df_measure_missing], axis=1, ignore_index=False, sort=False)

            engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/same_len_col_large_experiment_zipf_missing')
            c = engine.connect()
            conn = c.connection

            print("Exporting...", table_name1)
            new_df_attr.to_sql(table_name1, engine)

            print("Exporting...", table_name2)
            new_df_measure.to_sql(table_name2, engine)

