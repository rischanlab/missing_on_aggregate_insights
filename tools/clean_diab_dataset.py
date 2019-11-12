import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/large_experiment_missing_predicate')


# read the file and create a pandas dataframe
data = pd.read_csv('diabetic_data.csv')
data.drop(['encounter_id', 'patient_nbr', 'payer_code'], axis=1, inplace=True)
data.drop(['weight', 'medical_specialty'], axis=1, inplace=True) #hard to impute these features

data = data[data['race'] != '?']
data = data[data['diag_1'] != '?']
data = data[data['diag_2'] != '?']
data = data[data['diag_3'] != '?']
data = data[data['gender'] != 'Unknown/Invalid']

# original 'discharge_disposition_id' contains 28 levels
# reduce 'discharge_disposition_id' levels into 2 categories
# discharge_disposition_id = 1 corresponds to 'Discharge Home'
data['discharge_disposition_id'] = pd.Series(['Home' if val == 1 else 'Other discharge' 
                                              for val in data['discharge_disposition_id']], index=data.index)

# original 'admission_source_id' contains 25 levels
# reduce 'admission_source_id' into 3 categories
data['admission_source_id'] = pd.Series(['Emergency Room' if val == 7 else 'Referral' if val == 1 else 'Other source' 
                                              for val in data['admission_source_id']], index=data.index)

# original 'admission_type_id' contains 8 levels
# reduce 'admission_type_id' into 2 categories
data['admission_type_id'] = pd.Series(['Emergency' if val == 1 else 'Other type' 
                                              for val in data['admission_type_id']], index=data.index)


#How to deal with 'diag_1', 'diag_2', and 'diag_3'?
# See = Strack, Beata, et al. "Impact of HbA1c measurement on hospital readmission rates: analysis of 70,000 clinical database patient records." BioMed research international 2014 (2014).

#The primary, secondary, and third medical diagnoses are marked by the ICD9 codes.
#ICD9 code for diabetes: 250.xx

# denote 'diag_1' as '1' if it relates to diabetes and '0' if it's not
# remove 'diag_2' and 'diag_3'

data['diag_1'] = pd.Series(['Yes' if val.startswith('250') else 'No' for val in data['diag_1']], index=data.index)
data.drop(['diag_2', 'diag_3'], axis=1, inplace=True)


# keep only 'insulin' and remove the other 22 diabetes medications
data.drop(['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 
           'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 
           'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide', 'examide', 
           'citoglipton', 'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone',
           'metformin-rosiglitazone', 'metformin-pioglitazone', 'A1Cresult', 'diabetesMed', 'discharge_disposition_id', 'admission_source_id', 'max_glu_serum'], axis=1, inplace=True)

# why we remove those features? just plot it or check the count. E.g., miglitol: all data are filled by No

#data = data.rename(columns={"A1Cresult": "a1cresult", "diabetesMed": "diabetesmed"})

# Export to csv
#print("exporting to csv")
#data.to_csv('diab_clean_version.csv',index=True)


#Export to postgre
print("exporting to postgre table")
c = engine.connect()
conn = c.connection
data.to_sql('diabetes', engine)

conn.close()

