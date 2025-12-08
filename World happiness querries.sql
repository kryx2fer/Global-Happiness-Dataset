-- 1. Top 10 Happiest Countries Across All Years
SELECT Country, Year, Score
FROM happiness
ORDER BY Score DESC
LIMIT 10;

--  2. Average Happiness Score per Year

SELECT Year, AVG(Score) AS Avg_Score
FROM happiness
GROUP BY Year
ORDER BY Year;

--  3. Average Happiness Score per Country (Overall Ranking)
SELECT Country, AVG(Score) AS Avg_Score
FROM happiness
GROUP BY Country
ORDER BY Avg_Score DESC
LIMIT 20;

--  4. Countries with the Largest Improvement from 2015 → 2019
-- Improvement:
SELECT h1.Country,
       h2.Score - h1.Score AS Score_Change
FROM happiness h1
JOIN happiness h2
    ON h1.Country = h2.Country
WHERE h1.Year = 2015
  AND h2.Year = 2019
ORDER BY Score_Change DESC
LIMIT 10;

-- Biggest Decline:
SELECT h1.Country,
       h2.Score - h1.Score AS Score_Change
FROM happiness h1
JOIN happiness h2
    ON h1.Country = h2.Country
WHERE h1.Year = 2015
  AND h2.Year = 2019
ORDER BY Score_Change ASC
LIMIT 10;

--  5. Top 10 Countries by GDP per Capita
SELECT Country, Year, GDP_per_Capita
FROM happiness
ORDER BY GDP_per_Capita DESC
LIMIT 10;

--  6. Top 10 Countries with Highest Social Support
SELECT Country, Year, Social_Support
FROM happiness
ORDER BY Social_Support DESC
LIMIT 10;

-- 7. Average Happiness Score by Region
--(Works only for 2015–2016 where Region exists)

SELECT Region, AVG(Score) AS Avg_Score
FROM happiness
WHERE Region IS NOT NULL
GROUP BY Region
ORDER BY Avg_Score DESC;

--  8. Top 10 Countries with Lowest Corruption
SELECT Country, Year, Perceptions_of_Corruption
FROM happiness
WHERE Perceptions_of_Corruption IS NOT NULL
ORDER BY Perceptions_of_Corruption ASC
LIMIT 10;

--  9. Relationship Between Freedom and Happiness Score
(Useful for charts)
SELECT Country, Year, Freedom, Score
FROM happiness
ORDER BY Freedom DESC;

--  10. Rank Countries by Happiness Score in a Specific Year
--Example for 2018:
SELECT Country, Score
FROM happiness
WHERE Year = 2018
ORDER BY Score DESC;
--Change year as needed.

-- 11. Check Missing Values
SELECT *
FROM happiness
WHERE Country IS NULL
   OR Score IS NULL;

 --12. Get Country’s Happiness Trend Over All Years
--Example: Finland
SELECT Year, Score
FROM happiness
WHERE Country = 'Finland'
ORDER BY Year;
