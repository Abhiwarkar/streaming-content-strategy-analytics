import pandas as pd
import random
from faker import Faker

fake = Faker()

# -------------------------
# LOAD NETFLIX DATASET
# -------------------------

content = pd.read_csv("../data/raw_data/netflix_titles.csv")

content = content[['show_id','title','type','country','release_year','listed_in']]

content.columns = [
    "content_id",
    "title",
    "type",
    "country",
    "release_year",
    "genre"
]

content.to_excel("../data/raw_data/content_library.xlsx", index=False)

print("Content library created")

# -------------------------
# USERS DATASET
# -------------------------

countries = ["India","USA","UK","Canada","Germany","Japan","Brazil","Australia"]

users = []

for i in range(1,2001):

    users.append([
        i,
        random.choice(countries),
        random.randint(18,60),
        fake.date_between(start_date='-3y', end_date='today'),
        random.choice(["Basic","Standard","Premium"])
    ])

users_df = pd.DataFrame(users,columns=[
    "user_id",
    "country",
    "age",
    "signup_date",
    "subscription_type"
])

users_df.to_excel("../data/raw_data/users.xlsx",index=False)

print("Users dataset created")

# -------------------------
# WATCH HISTORY
# -------------------------

content_ids = content["content_id"].tolist()

watch = []

devices = ["Mobile","TV","Laptop","Tablet"]

for i in range(1,20001):

    watch.append([
        f"W{i}",
        random.randint(1,2000),
        random.choice(content_ids),
        random.randint(10,180),
        fake.date_between(start_date='-1y', end_date='today'),
        random.choice(devices)
    ])

watch_df = pd.DataFrame(watch,columns=[
    "watch_id",
    "user_id",
    "content_id",
    "watch_time_minutes",
    "watch_date",
    "device"
])

watch_df.to_excel("../data/raw_data/watch_history.xlsx",index=False)

print("Watch history dataset created")

print("ALL DATASETS GENERATED SUCCESSFULLY")