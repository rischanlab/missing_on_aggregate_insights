# -*- coding: utf-8 -*-
from a_seedb_function import SeeDB
from a_seedb_db import data
import psycopg2
# conn = psycopg2.connect("dbname=same_len_col_large_experiment user=postgres password=zenvisage")
#
# cursor = conn.cursor()
# cursor.execute("""SELECT table_name FROM information_schema.tables
#        WHERE table_schema = 'public'""") # and table_name like '%diabetes%'
# mytable_db = cursor.fetchall()


if __name__ == "__main__":

    top_k = 10
    #atr = ['race', 'gender', 'age']
    atr = ['race', 'gender', 'age', 'admission_type_id', 'diag_1','insulin', 'change','readmitted']
    #measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures']
    measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
               'num_medications', 'number_outpatient', 'number_emergency',
               'number_inpatient', 'number_diagnoses']

    func = ['sum', 'avg', 'max', 'count']

    # for i in mytable:
    #     db, table, data_set = data(i[0], atr, measure, func)
    #     print("running with db {}".format(i[0]))
    #     framework = SeeDB(db,data_set,table,top_k)
    #     framework.main()
    #     print("done")
    mlist = [0.1, 0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    mytable = []
    #mytable = ['db_30rand_missing_a_m7']
    for i in mlist:
        for j in range(3):
            # print(int(i * 100), j)
            x = int(i * 100)
            # print(df)
            # print(df.columns.to_series().groupby(df.dtypes).groups)
            # db missing is db with row contains missing drop
            # db NaN is db with row contain missing keep
            table_name = "db_" + str(x) + "rand_missing_predicate" + str(j+1)
            mytable.append(table_name)
    print(mytable)
    # print(len(mytable))

    for i in mytable:
        db, table, data_set = data(i, atr, measure, func)
        print("running with db {}".format(i))
        try:
            framework = SeeDB(db, data_set, table, top_k)
            framework.main()
            time.sleep(300)
        except:
            pass  # doing nothing on exception
        print("done")