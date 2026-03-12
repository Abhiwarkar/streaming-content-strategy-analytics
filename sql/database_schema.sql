CREATE TABLE users (
user_id NUMBER PRIMARY KEY,
country VARCHAR2(50),
age NUMBER,
signup_date DATE,
subscription_type VARCHAR2(20)
);

CREATE TABLE content (
content_id VARCHAR2(20) PRIMARY KEY,
title VARCHAR2(200),
type VARCHAR2(20),
country VARCHAR2(50),
release_year NUMBER,
genre VARCHAR2(200)
);

CREATE TABLE watch_history (
watch_id VARCHAR2(20) PRIMARY KEY,
user_id NUMBER,
content_id VARCHAR2(20),
watch_time_minutes NUMBER,
watch_date DATE,
device VARCHAR2(20)
);

