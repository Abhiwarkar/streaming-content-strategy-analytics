import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("EDA FILE RUNNING")

# -------------------------
# LOAD CLEAN DATASETS
# -------------------------

content = pd.read_csv("../data/cleaned_data/content_clean.csv")
users = pd.read_csv("../data/cleaned_data/users_clean.csv")
watch = pd.read_csv("../data/cleaned_data/watch_history_clean.csv")

print("Datasets Loaded Successfully")

# -------------------------
# MERGE DATASETS
# -------------------------

df = watch.merge(content, on="content_id").merge(users, on="user_id")

print("Merged Dataset Shape:", df.shape)

print(df.head())

# -------------------------
# CONVERT DATE COLUMNS
# -------------------------

df["watch_date"] = pd.to_datetime(df["watch_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

# -------------------------
# BASIC INFO
# -------------------------

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())