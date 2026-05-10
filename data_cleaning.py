import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://docs.google.com/spreadsheets/d/1J6x8ynn9UPqgwiC_Eh0LadYQuyoIjpMkT4j_Itg5Apk/export?format=csv'
df = pd.read_csv(url)

df.head()
# df.info()


"""# **1. Data Cleaning**

1.1. Checking for duplicates
"""

df.duplicated().sum()

"""1.2. Checking for NaN values"""

df.isnull().sum()

"""1.3. Correcting columns one by one

1.3.1. Column **"PERSON_AGE"**
"""

print(f"Column 'PERSON_AGE'")

df['PERSON_AGE'] = df['PERSON_AGE'].fillna(df["PERSON_AGE"].mean()).round()
print (f"Verifying 0 null values in the 'PERSON_AGE' column: \nnull values in the column:{df['PERSON_AGE'].isnull().sum()}")
# print(f"Unique values:{df['PERSON_AGE'].nunique()}")

"""1.3.2. Column **"SAFETY_EQUIPMENT"**"""

print(f"\nColumn 'SAFETY_EQUIPMENT'")

df['SAFETY_EQUIPMENT'] = df['SAFETY_EQUIPMENT'].fillna('Unknown')
print (f"Verifying 0 null values in the 'SAFETY_EQUIPMENT' column: \nnull values in the column:{df['SAFETY_EQUIPMENT'].isnull().sum()}")
# print(f"Unique values:{df['SAFETY_EQUIPMENT'].nunique()}")

"""1.3.3. Column **"PED_LOCATION"**"""

print(f"\nColumn 'PED_LOCATION'")

df['PED_LOCATION'] = df['PED_LOCATION'].fillna('Does Not Apply')
df['PED_LOCATION'] = df['PED_LOCATION'].replace('Unknown', 'Does Not Apply')
# print(df.PED_LOCATION.unique().tolist())
print (f"Verifying 0 null values in the 'SAFETY_EQUIPMENT' column: \nnull values in the column:{df['PED_LOCATION'].isnull().sum()}")
# print(f"Unique values:{df['PED_LOCATION'].nunique()}")

"""1.3.4 & 1.3.5 Columns **"CONTRIBUTING_FACTOR_1"** and **"CONTRIBUTING_FACTOR_2"**"""

df['CONTRIBUTING_FACTOR_1'] = df['CONTRIBUTING_FACTOR_1'].fillna('Does Not Apply')
df['CONTRIBUTING_FACTOR_1'] = df['CONTRIBUTING_FACTOR_1'].replace('Unspecified', 'Does Not Apply')

# To view the repeating contributing 1 factors, run
# pd.Series(df['CONTRIBUTING_FACTOR_1'].unique())

df['CONTRIBUTING_FACTOR_2'] = df['CONTRIBUTING_FACTOR_2'].fillna('Does Not Apply')
df['CONTRIBUTING_FACTOR_2'] = df['CONTRIBUTING_FACTOR_2'].replace('Unspecified', 'Does Not Apply')

# To view the repeating contributing 2 factors, run
# pd.Series(df['CONTRIBUTING_FACTOR_2'].unique())

"""1.3.6. Column **"PED_ACTION"**"""

df['PED_ACTION'] = df['PED_ACTION'].fillna('Does Not Apply')
df['PED_ACTION'] = df['PED_ACTION'].replace('Unknown', 'Does Not Apply')

# To view the repeating values for the PED_ACTION column, run
# pd.Series(df.PED_ACTION.unique().tolist())

"""1.3.7. Column **"POSITION_IN_VEHICLE"**"""

df["POSITION_IN_VEHICLE"] = df["POSITION_IN_VEHICLE"].fillna("Does Not Apply")
df["POSITION_IN_VEHICLE"] = df["POSITION_IN_VEHICLE"].replace("Unknown", "Does Not Apply")

# To view the repeating values for the POSITION_IN_VEHICLE column, run
# pd.Series(df.PED_ACTION.unique().tolist())

"""1.3.8. Column **"EJECTION"**

Fill the missing values with the mode of the column, which in this case is the **"Not Ejected"** value taking more than 78% of occurences in the column values
"""

# df.EJECTION.value_counts()[0]/df.shape[0] * 100
# df.EJECTION.value_counts()

df['EJECTION'] = df['EJECTION'].fillna('Not Ejected')
# df.EJECTION.value_counts()

# additional possibly important information / code used in process
# df.EJECTION.isnull().sum()
# pd.Series(df.EJECTION.unique().tolist())
# df.EJECTION.mode()

"""1.3.9. Column **"VEHICLE_ID"**"""

df["VEHICLE_ID"] = df["VEHICLE_ID"].fillna("Does Not Apply")
df["VEHICLE_ID"] = df["VEHICLE_ID"].replace("Unknown", "Does Not Apply")

# To view the repeating values for the POSITION_IN_VEHICLE column, run
# (df.VEHICLE_ID.unique().tolist())

"""### 🎉 **OUR DATASET IS CLEAN** !!!"""

df.isnull().sum()

"""1.4. Several adjustments for the finally clean dataset

1.4.1. Check data types
"""

df.dtypes

"""1.4.2. Transform **"CRASH_DATE"** and **"CRASH_TIME"** into a more applicable data type, and

1.4.3. Merge them into **"CRASH_DATE_TIME"** to make the further analysis more effective.

We will remove the crash_date and crash_time columns later, before starting(see 1.4.7).
"""

df['CRASH_DATE_TIME'] = df['CRASH_DATE'] + ' ' + df['CRASH_TIME']
pd.to_datetime(df.CRASH_DATE_TIME)
df['CRASH_DATE_TIME'] = pd.to_datetime(df.CRASH_DATE_TIME)
df['CRASH_DATE_TIME']

"""Additional checking for correct values

1.4.4. Check for the values of **"PERSON_SEX"** column

1.4.5 Check for the values of **"BODILY_INJURY"** column

"""

print(df.PERSON_SEX.unique())
print(df.BODILY_INJURY.unique())

"""1.4.6. Removing all **"PERSON_AGE"** values which are out of logic"""

print((df['PERSON_AGE'] < 0).sum())
df.loc[df['PERSON_AGE'] < 0, 'PERSON_AGE'] = np.nan
df.loc[df['PERSON_AGE'] > 99, 'PERSON_AGE'] = np.nan

df['PERSON_AGE'].describe().round(2)

"""After this we went back and re-run 1.3.1 to fill all the nan values with "Unknown"-s"""

df['PERSON_AGE'] = df['PERSON_AGE'].fillna(df["PERSON_AGE"].mean()).round()

df['PERSON_AGE'] = df['PERSON_AGE'].fillna(df["PERSON_AGE"].mean()).round()

print(f"Column 'PERSON_AGE'")

df['PERSON_AGE'] = df['PERSON_AGE'].fillna(df["PERSON_AGE"].mean()).round()
print (f"Verifying 0 null values in the 'PERSON_AGE' column: \nnull values in the column:{df['PERSON_AGE'].isnull().sum()}")
# print(f"Unique values:{df['PERSON_AGE'].nunique()}")

"""1.4.7. **Hide unnecessary columns for data analysis**
- Hiding **ID**-s because they simly enumerate the cases, and
- hiding **CRASH_DATE** and **CRASH_TIME** because we've created a single **CRASH_DATE_TIME** column, combining both.
"""

analysis_df = df.drop(columns = ["VEHICLE_ID", "PERSON_ID", "UNIQUE_ID", "COLLISION_ID", "CRASH_DATE", "CRASH_TIME"])

print(df.info())

"""1.5. Logic errors

Here, as you can see, we have recorded helmet on an Bicyclist, lap beld on a pedestrian, and so on.

We will correct those logical errors now
"""

df.groupby('PERSON_TYPE')['SAFETY_EQUIPMENT'].value_counts()

# Bicyclist
df.loc[(df.PERSON_TYPE == "Bicyclist") & (df.SAFETY_EQUIPMENT.isin([
                                                                    'Lap Belt','Harness','Lap Belt & Harness', 'Helmet (Motorcycle Only)'
                                                                    ])), 'SAFETY_EQUIPMENT'] = np.nan

# Occupant
df.loc[(df.PERSON_TYPE == "Occupant") & (df.SAFETY_EQUIPMENT.isin([
                                                                    'Helmet (Motorcycle Only)', 'Helmet Only (In-Line Skater/Bicyclist)',
                                                                    'Helmet/Other (In-Line Skater/Bicyclist)','Pads Only (In-Line Skater/Bicyclist)',
                                                                    'Stoppers Only (In-Line Skater/Bicyclist)'
                                                                    ])), 'SAFETY_EQUIPMENT'] = np.nan
# Other Motorized
df.loc[(df.PERSON_TYPE == "Other Motorized") & (df.SAFETY_EQUIPMENT.isin([
                                                                    'Helmet Only (In-Line Skater/Bicyclist)', 'Helmet/Other (In-Line Skater/Bicyclist)',
                                                                    ])), 'SAFETY_EQUIPMENT'] = np.nan
# Pedestrian
df.loc[(df.PERSON_TYPE == "Pedestrian") & (df.SAFETY_EQUIPMENT.isin([
                                                                    'Lap Belt','Harness','Lap Belt & Harness', 'Helmet (Motorcycle Only)',
                                                                    'Helmet Only (In-Line Skater/Bicyclist)', 'Helmet/Other (In-Line Skater/Bicyclist)'
                                                                    ])), 'SAFETY_EQUIPMENT'] = np.nan

"""The actual code for correcting logic errors.

Note that it is important to go back to 1.3.2. to make all NaN values "Unknown" again.
"""

print(f"\nColumn 'SAFETY_EQUIPMENT'")

df['SAFETY_EQUIPMENT'] = df['SAFETY_EQUIPMENT'].fillna('Unknown')
print (f"Verifying 0 null values in the 'SAFETY_EQUIPMENT' column: \nnull values in the column:{df['SAFETY_EQUIPMENT'].isnull().sum()}")
# print(f"Unique values:{df['SAFETY_EQUIPMENT'].nunique()}")

# final check
df.isnull().sum()

df = df.replace("Does Not Apply", "Unknown")

# remember that
cleaned_df = df.drop(columns = ["VEHICLE_ID", "PERSON_ID", "UNIQUE_ID", "COLLISION_ID", "CRASH_DATE", "CRASH_TIME"])