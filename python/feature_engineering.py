import pandas as pd

# Load final dataset
df = pd.read_csv("../data/cleaned_data/watch_history_clean.csv")

# Feature 1: Watch hour
df["watch_hour"] = pd.to_datetime(df["watch_date"]).dt.hour

# Feature 2: Day of week
df["day_of_week"] = pd.to_datetime(df["watch_date"]).dt.day_name()

# Feature 3: Weekend indicator
df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

print("Feature Engineering Completed")
print(df.head())