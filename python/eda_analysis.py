import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

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

# -------------------------
# CONVERT DATE COLUMNS
# -------------------------

df["watch_date"] = pd.to_datetime(df["watch_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

# -------------------------
# CLEAN GENRE COLUMN
# -------------------------

df["genre"] = df["genre"].str.split(", ")
df = df.explode("genre")

# -------------------------
# BASIC INFO
# -------------------------

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------
# CHART 1 — GENRE VS WATCH TIME
# -------------------------

genre_watch = df.groupby("genre")["watch_time_minutes"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=genre_watch.index, y=genre_watch.values)

plt.title("Top Genres by Watch Time")
plt.xlabel("Genre")
plt.ylabel("Total Watch Time")
plt.xticks(rotation=45)

plt.show()

# -------------------------
# CHART 2 — MOVIE VS SERIES
# -------------------------

type_watch = df.groupby("type")["watch_time_minutes"].sum()

plt.figure(figsize=(6,6))
plt.pie(type_watch, labels=type_watch.index, autopct='%1.1f%%')

plt.title("Movies vs TV Shows Watch Time")

plt.show()

# -------------------------
# CHART 3 — WATCH TIME BY COUNTRY
# -------------------------

country_watch = df.groupby("country_y")["watch_time_minutes"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=country_watch.index, y=country_watch.values)

plt.title("Watch Time by User Country")
plt.xlabel("Country")
plt.ylabel("Total Watch Time")

plt.show()

# -------------------------
# CHART 4 — DEVICE ANALYSIS
# -------------------------

device_watch = df.groupby("device")["watch_time_minutes"].sum()

plt.figure(figsize=(8,6))
sns.barplot(x=device_watch.index, y=device_watch.values)

plt.title("Watch Time by Device")
plt.xlabel("Device")
plt.ylabel("Watch Time")

plt.show()

# -------------------------
# CHART 5 — TOP 10 CONTENT
# -------------------------

top_content = df.groupby("title")["watch_time_minutes"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_content.values, y=top_content.index)

plt.title("Top 10 Most Watched Content")
plt.xlabel("Watch Time")
plt.ylabel("Content Title")

plt.show()

# -------------------------
# CHART 6 — AGE VS ENGAGEMENT
# -------------------------

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["age"], y=df["watch_time_minutes"])

plt.title("User Age vs Watch Time")
plt.xlabel("Age")
plt.ylabel("Watch Time")

plt.show()

# -------------------------
# CHART 7 — MONTHLY TREND
# -------------------------

df["month"] = df["watch_date"].dt.to_period("M")

monthly_watch = df.groupby("month")["watch_time_minutes"].sum()

plt.figure(figsize=(12,6))
monthly_watch.plot()

plt.title("Monthly Streaming Trend")
plt.xlabel("Month")
plt.ylabel("Watch Time")

plt.show()

# -------------------------
# CHART 8 — GENRE DISTRIBUTION
# -------------------------

df = df.reset_index(drop=True)

plt.figure(figsize=(10,6))
sns.countplot(y="genre", data=df, order=df["genre"].value_counts().index[:10])

plt.title("Top Genres Distribution")

plt.show()
df.to_csv("../data/final_streaming_dataset.csv", index=False)

print("\nEDA Completed Successfully")