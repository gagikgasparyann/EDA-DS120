import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data_cleaning import cleaned_df

"""# **2. Classes**

# **2.1. Data Analyzer**
"""

class Analyzer:
  """
    A class to perform analysis for our cleaned dataframe
  """
  def __init__(self, df, name):
    """
        Initializing the Analyzer class with reference to our cleaned dataframe
        Args used: df (dataframe) that is our cleaned dataframe
                   name (string) that is the title of cleaned dataframe
    """
    self.df = df
    self.name = name
    # Two attributes: 1st the dataframe itself, 2nd the name of that dataframe

  def crashes_every_month(self):
    """
    Returns the statistics of crashes for every month of the given dataframe.
    """
    month_names = self.df['CRASH_DATE_TIME'].dt.month_name()
    print(month_names)
    result = month_names.value_counts()
    return result


  def crashes_by_person_type(self):
    """
    Returns the statistics of crashes based on person type of the given dataframe.
    """
    # Statistics of crashes based on person type, e.g. bicyclist, pedestrian
    result = self.df.groupby("PERSON_TYPE").size().copy()
    return result

  def crashes_by_age_sex(self):
    """
    Returns the difference of statistics of crashes' mean, median, mode for male and female of the given dataframe.
    """
    # Statistics of person's age mean, median and mode of crashes and the difference between male and female
    result = self.df.groupby("PERSON_SEX")["PERSON_AGE"].agg(["mean", "median", pd.Series.mode]).drop("U").copy()
    # Dropping the row of unknown sex
    return result

  def cor_role_injury(self):
    """
    Returns the correlation of person's role and injury type of the given dataframe.
    """
    # Correlation between person's role and injury
    result = self.df[["PERSON_INJURY", "PED_ROLE"]].copy()
    # result["PERSON_INJURY"] = result["PERSON_INJURY"].map({"Killed": 1, "Injured": 0})
    result = pd.get_dummies(result, columns=["PED_ROLE"])
    result = pd.get_dummies(result, columns=["PERSON_INJURY"])
    # heatmap can be created for this
    result = result.corr()
    result = result.loc[
      [col for col in result.columns if "PED_ROLE" in col],
      [col for col in result.columns if "PERSON_INJURY" in col]
    ]
    return result

  def cor_emotional_status_injury(self):
    """
    Returns the correlation of person's emotional status and injury type of the given dataframe.
    """
    # Correlation between emotional status and injury
    result = self.df[["PERSON_INJURY", "EMOTIONAL_STATUS"]].copy()
    # result["PERSON_INJURY"] = result["PERSON_INJURY"].map({"Killed": 1, "Injured": 0})
    result = pd.get_dummies(result, columns=["EMOTIONAL_STATUS"])
    result = pd.get_dummies(result, columns=["PERSON_INJURY"])
    # heatmap can be created for this
    result = result.corr()
    result = result.loc[
      [col for col in result.columns if "EMOTIONAL_STATUS" in col],
      [col for col in result.columns if "PERSON_INJURY" in col]
    ]
    return result

  def cor_factor_injury(self):
    """
    Returns the correlation of the contributing factor and injury type of the given dataframe.
    """
    # Correlation between contributing factor and injury
    result = self.df[["PERSON_INJURY", "CONTRIBUTING_FACTOR_1"]].copy()
    # result["PERSON_INJURY"] = result["PERSON_INJURY"].map({"Killed": 1, "Injured": 0})
    result = pd.get_dummies(result, columns=["CONTRIBUTING_FACTOR_1"])
    result = pd.get_dummies(result, columns=["PERSON_INJURY"])
    # heatmap can be created for this
    result = result.corr()
    result = result.loc[
      [col for col in result.columns if "CONTRIBUTING_FACTOR_1" in col],
      [col for col in result.columns if "PERSON_INJURY" in col]
    ]
    return result

nyc = Analyzer(cleaned_df, "NYC Collisions")
# Creating an instance of Analyzer class to be later used

