#  Global Happiness Analysis Report (2015–2019)
Dataset: Global Happiness Survey (Merged Multi-Year Dataset)
## 1. Executive Summary

This report provides a complete analytical exploration of global happiness trends between 2015 and 2019, leveraging SQL analysis techniques across 14 key insights. The analysis covers:

Year-over-year changes

Volatility and stability

Influence of GDP, social support, corruption, and freedom

Predicted vs actual happiness performance

Regional dynamics

Classification and clustering

Long-term trends

Core findings show that global happiness is stable overall, but disparities between regions remain significant. Nordic countries repeatedly lead the rankings, while conflict-affected and economically stressed countries remain lowest.

## 2. Dataset Overview

The dataset contains multiple country-level indicators, including:

Score — Overall happiness index

GDP_per_Capita

Social_Support

Healthy_Life_Expectancy

Freedom

Generosity

Perceptions_of_Corruption

Region, Rank, Year

The dataset covers approximately 5 years (2015–2019) across dozens of countries.

## 3. Global Average Happiness Trend
Figure: Average Happiness Score per Year (Generated from dataset)

(Shown earlier by the system — line chart)

Insight

Global happiness experienced:

A mild dip around 2017

A steady rise toward 2019

Overall stable scores within a narrow range, indicating global emotional resilience

## 4. Year-Over-Year Happiness Change

Tracks performance changes at the country level.

SQL Query
SELECT 
    h1.Country,
    h1.Year,
    h1.Score AS Score_Current,
    h2.Score AS Score_Previous,
    (h1.Score - h2.Score) AS YoY_Change
FROM happiness h1
LEFT JOIN happiness h2
     ON h1.Country = h2.Country
    AND h1.Year = h2.Year + 1
ORDER BY YoY_Change DESC;

Insight

Positive YoY change indicates improving national conditions.

Negative YoY change often correlates with political turmoil, recession, or conflict.

## 5. Volatility Index (Happiness Stability)

Measures the variance of happiness scores across years for each country.

SQL Query
SELECT 
    Country,
    AVG(Score) AS Avg_Score,
    (AVG(Score * Score) - AVG(Score) * AVG(Score)) AS Score_Variance
FROM happiness
GROUP BY Country
ORDER BY Score_Variance DESC
LIMIT 15;

Insight

High volatility → unstable regions (political/economic shocks)

Low volatility → consistently high performers (Nordic nations)

## 6. Influence of Key Happiness Factors

Correlation approximations (due to SQLite limitations) were computed for GDP.

SQL Query (GDP influence example)
SELECT 
    Year,
    SUM(GDP_per_Capita * Score) AS Covariance_Like,
    SUM(GDP_per_Capita * GDP_per_Capita) AS GDP_Variance_Like
FROM happiness
GROUP BY Year
ORDER BY Covariance_Like DESC;

Insight

Top predictors of happiness:

Social Support

Healthy Life Expectancy

GDP per Capita

Freedom

Corruption has a strong negative association.

## 7. Component Strength Score

Combines all positive contributors into a single metric.

SQL Query
SELECT 
    Country,
    Year,
    GDP_per_Capita + Social_Support + Healthy_Life_Expectancy + Freedom
         + Generosity - Perceptions_of_Corruption AS Component_Sum,
    Score
FROM happiness
ORDER BY Component_Sum DESC;

Insight

Countries with strong component scores tend to be the happiest (e.g., Western Europe).

## 8. Overperformers vs Underperformers

Compares actual vs expected happiness based on components.

SQL Query
SELECT 
    Country,
    Year,
    Score,
    (GDP_per_Capita + Social_Support + Healthy_Life_Expectancy + Freedom
      + Generosity - Perceptions_of_Corruption) AS Predicted_Score,
    Score - (GDP_per_Capita + Social_Support + Healthy_Life_Expectancy + Freedom
      + Generosity - Perceptions_of_Corruption) AS Performance_Delta
FROM happiness
ORDER BY Performance_Delta DESC;

Insight

Overperformers → happiness driven by culture, social cohesion

Underperformers → wealthy but high-stress or unequal countries

## 9. Regional Happiness Trends
SQL Query
SELECT 
    Region,
    Year,
    AVG(Score) AS Avg_Score
FROM happiness
WHERE Region IS NOT NULL
GROUP BY Region, Year
ORDER BY Year, Avg_Score DESC;

Insight

Western Europe leads globally.

Sub-Saharan Africa consistently ranks lowest.

Middle East shows large fluctuations tied to conflict cycles.

## 10. High Freedom but Low Happiness
SQL Query
SELECT 
    Country,
    Year,
    Freedom,
    Score
FROM happiness
WHERE Freedom > 0.5 AND Score < 5
ORDER BY Freedom DESC;

Insight

Freedom alone does not guarantee happiness; economic pressures and insecurity can dominate.

## 11. High Corruption but High Happiness
SQL Query
SELECT 
    Country,
    Year,
    Perceptions_of_Corruption,
    Score
FROM happiness
WHERE Perceptions_of_Corruption > 0.4
ORDER BY Score DESC;

Insight

Cultural cohesion and strong social networks can offset institutional weaknesses.

## 12. Top 15 Most Generous Countries
SQL Query
SELECT 
    Country,
    AVG(Generosity) AS Avg_Generosity
FROM happiness
GROUP BY Country
ORDER BY Avg_Generosity DESC
LIMIT 15;

Insight

Generosity is not directly tied to GDP; many generous nations are mid-income countries.

## 13. Strong Social Support but Low Happiness
SQL Query
SELECT 
    Country,
    Year,
    Social_Support,
    Score
FROM happiness
WHERE Social_Support > 1 AND Score < 5
ORDER BY Social_Support DESC;

Insight

Strong support systems may be offset by safety concerns, unemployment, or governance issues.

## 14. Countries With Perfect Data (No Missing Values)
SQL Query
SELECT Country, COUNT(*) AS Records
FROM happiness
WHERE Country NOT IN (
    SELECT Country FROM happiness
    WHERE GDP_per_Capita IS NULL
       OR Social_Support IS NULL
       OR Healthy_Life_Expectancy IS NULL
       OR Freedom IS NULL
       OR Perceptions_of_Corruption IS NULL
)
GROUP BY Country;

Insight

Countries with perfect data are best suited for predictive or machine learning models.

## 15. Happiness Classification (Simple Clustering)
SQL Query
SELECT 
    Country,
    Year,
    Score,
    CASE
        WHEN Score >= 7 THEN 'Very Happy'
        WHEN Score >= 6 THEN 'Happy'
        WHEN Score >= 5 THEN 'Neutral'
        ELSE 'Unhappy'
    END AS Happiness_Level
FROM happiness;

Insight

Scandinavian countries dominate the “Very Happy” class; African and conflict nations dominate “Unhappy”.

## 16. Most Consistently Happy Countries
SQL Query
SELECT 
    Country,
    (AVG(Score * Score) - AVG(Score) * AVG(Score)) AS Variance,
    AVG(Score) AS Avg_Score
FROM happiness
GROUP BY Country
ORDER BY Variance ASC
LIMIT 10;

Insight

Low-variance nations are happiness-stable (Switzerland, Denmark, Iceland, etc.).

## 17. Long-Term Trend Slope
SQL Query
SELECT 
    Country,
    SUM(Year * Score) AS Num,
    SUM(Year) AS Sum_Year,
    SUM(Score) AS Sum_Score,
    COUNT(*) AS N,
    (SUM(Year * Score) - (SUM(Year) * SUM(Score) / COUNT(*))) AS Trend_Slope_Like
FROM happiness
GROUP BY Country
ORDER BY Trend_Slope_Like DESC;

Insight

Positive slopes → long-term improvement

Negative slopes → societal or economic deterioration

Most Nordic countries remain stable

## 18. Final Conclusions
Key Findings

Global happiness is stable, but highly uneven across regions.

The strongest predictors are Social Support and Healthy Life Expectancy.

Overperformers succeed culturally rather than economically.

Underperformers struggle emotionally despite strong infrastructures.

Stability is highest in Europe; volatility highest in conflict regions.

Analyst Recommendations

Use this dataset for forecasting, regional policy analysis, or Power BI dashboards.

Include trend and volatility metrics in predictive models.

Compare cultural vs economic determinants in future studies.
