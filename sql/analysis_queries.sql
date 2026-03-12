---//BASIC 4--//

Most popular genre--

SELECT genre,
SUM(watch_time_minutes) AS total_watch_time
FROM watch_history w
JOIN content c
ON w.content_id = c.content_id
GROUP BY genre
ORDER BY total_watch_time DESC;

Movie vs Series engagement----

SELECT type,
SUM(watch_time_minutes) watch_time
FROM watch_history w
JOIN content c
ON w.content_id = c.content_id
GROUP BY type;

Top 10 content----

SELECT title,
SUM(watch_time_minutes) watch_time
FROM watch_history w
JOIN content c
ON w.content_id = c.content_id
GROUP BY title
ORDER BY watch_time DESC
FETCH FIRST 10 ROWS ONLY;

Country wise watch time---

SELECT country,
SUM(watch_time_minutes) watch_time
FROM watch_history w
JOIN users u
ON w.user_id = u.user_id
GROUP BY country
ORDER BY watch_time DESC;

----///ADVANCED QUERIES---///

Average Watch Time per User---Purpose- identify high engagement users

SELECT user_id,
AVG(watch_time_minutes) AS avg_watch_time
FROM watch_history
GROUP BY user_id
ORDER BY avg_watch_time DESC;

Most Active Users (Top 10)---Purpose-- power users identify

SELECT user_id,
COUNT(*) AS total_views
FROM watch_history
GROUP BY user_id
ORDER BY total_views DESC
FETCH FIRST 10 ROWS ONLY;

Watch Time by Device--Purpose--mobile vs TV usage
SELECT device,
SUM(watch_time_minutes) AS total_watch_time
FROM watch_history
GROUP BY device
ORDER BY total_watch_time DESC;

Average Watch Time by Country--Purpose---country engagement comparison

SELECT country,
AVG(watch_time_minutes) AS avg_watch_time
FROM watch_history w
JOIN users u
ON w.user_id = u.user_id
GROUP BY country
ORDER BY avg_watch_time DESC;

Content Released per Year--Purpose content production trends

SELECT release_year,
COUNT(*) AS total_content
FROM content
GROUP BY release_year
ORDER BY release_year;

Genre Popularity by Number of Titles--Genre Popularity by Number of Titles
SELECT genre,
COUNT(*) AS total_titles
FROM content
GROUP BY genre
ORDER BY total_titles DESC;

Average Watch Time by Genre---Purpose--genre engagement quality

SELECT genre,
AVG(watch_time_minutes) AS avg_watch_time
FROM watch_history w
JOIN content c
ON w.content_id = c.content_id
GROUP BY genre
ORDER BY avg_watch_time DESC;

Monthly Watch Time Trend--Purpose--watching trend over time

SELECT 
TO_CHAR(watch_date,'YYYY-MM') AS month,
SUM(watch_time_minutes) AS total_watch_time
FROM watch_history
GROUP BY TO_CHAR(watch_date,'YYYY-MM')
ORDER BY month;



