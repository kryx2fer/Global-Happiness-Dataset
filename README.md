# Global-Happiness-Dataset
Global Happiness Insights Report (2015–2019)

This report explores year-over-year changes, volatility, factor influence, over/under-performance, regional dynamics, corruption patterns, generosity rankings, and happiness stability using SQL-style logic and dataset-driven visuals.

## 1. Global Happiness Trend Over Time
Figure 1 — Average Global Happiness Score per Year

The chart shows how the overall average happiness score changed from 2015 to 2019.



Key Insight

✔ Happiness dipped slightly around 2017 but rose again toward 2019.
✔ Overall: moderate but stable global happiness.

## 2. Year-Over-Year Change (YoY)

This calculation detects whether each country is improving or declining.

SQL logic used:

SELECT h1.Country, h1.Year, h1.Score AS Score_Current,
       h2.Score AS Score_Previous,
       (h1.Score - h2.Score) AS YoY_Change
FROM happiness h1
LEFT JOIN happiness h2
     ON h1.Country = h2.Country
    AND h1.Year = h2.Year + 1
ORDER BY YoY_Change DESC;

Insights

Fastest improvers change every year, often small countries recovering from economic shocks.

Declining scores often align with political transitions or economic downturns.

## 3. Volatility Index — Most Unstable Countries

Measures how much each country’s score fluctuates.

SQL:

SELECT Country, AVG(Score) AS Avg_Score,
       (AVG(Score * Score) - AVG(Score) * AVG(Score)) AS Score_Variance
FROM happiness
GROUP BY Country
ORDER BY Score_Variance DESC
LIMIT 15;

Insights

High variance suggests unstable political or social climate.

Western Europe tends to have low variance (stable).

Middle Eastern and African regions sometimes show higher fluctuations.

## 4. Factor Influence (GDP, Social Support, etc.)

We approximate correlation by covariance-like calculations:

SQL:

SELECT Year,
       SUM(GDP_per_Capita * Score) AS Covariance_Like,
       SUM(GDP_per_Capita * GDP_per_Capita) AS GDP_Variance_Like
FROM happiness
GROUP BY Year;

Insights

Social Support and Healthy Life Expectancy typically rank as strongest predictors.

Freedom improves scores but with less weight than GDP and Social Support.

Corruption has a strong negative correlation.

## 5. Happiness Component Weight

Ranks nations based on their underlying “drivers.”

SQL:

SELECT Country, Year,
       GDP_per_Capita + Social_Support + Healthy_Life_Expectancy + Freedom
       + Generosity - Perceptions_of_Corruption AS Component_Sum,
       Score
FROM happiness
ORDER BY Component_Sum DESC;

Insights

Countries with high component sums typically:

Are economically strong

Have high social support

Have strong health systems

Perceive low corruption

## 6. Over-performers vs Under-performers

This compares predicted vs actual happiness:

SQL:

SELECT Country, Year, Score,
       (GDP_per_Capita + Social_Support + Healthy_Life_Expectancy + Freedom
        + Generosity - Perceptions_of_Corruption) AS Predicted_Score,
       Score - (...) AS Performance_Delta
FROM happiness
ORDER BY Performance_Delta DESC;

Insight

Countries like Costa Rica often over-perform (high social cohesion).

Some wealthy countries still under-perform (stress, inequality, mental health issues).

## 7. Regional Happiness Trends

SQL:

SELECT Region, Year, AVG(Score)
FROM happiness
WHERE Region IS NOT NULL
GROUP BY Region, Year;

Insights

Western Europe consistently leads.

Sub-Saharan Africa remains lowest.

Some regions fluctuate depending on conflict patterns or economic swings.

## 8. High Freedom but Low Happiness

SQL:

SELECT Country, Year, Freedom, Score
FROM happiness
WHERE Freedom > 0.5 AND Score < 5;

Insight

Democracy ≠ happiness
Economic hardship, inequality, or security issues may override political freedoms.

## 9. High Corruption but High Happiness

SQL:

SELECT Country, Year, Perceptions_of_Corruption, Score
FROM happiness
WHERE Perceptions_of_Corruption > 0.4
ORDER BY Score DESC;

Insight

Some countries remain happy despite corruption due to:

High social support

Strong cultural cohesion

Community-based living

## 10. Top 15 Most Generous Countries

SQL:

SELECT Country, AVG(Generosity)
FROM happiness
GROUP BY Country
ORDER BY AVG(Generosity) DESC
LIMIT 15;

Insight

Countries with strong volunteering/charity norms dominate.

Generosity is not strictly tied to wealth.

## 11. Countries With Perfect Data (No NULLs)

SQL:

SELECT Country, COUNT(*)
FROM happiness
WHERE Country NOT IN (
    SELECT Country FROM happiness
    WHERE any_field IS NULL
)
GROUP BY Country;

Insight

These countries are best for predictive modeling.

Missing data often occurs in developing regions.

## 12. Classification by Happiness Level

SQL:

CASE
 WHEN Score >= 7 THEN 'Very Happy'
 WHEN Score >= 6 THEN 'Happy'
 WHEN Score >= 5 THEN 'Neutral'
 ELSE 'Unhappy'
END

Insight

Scandinavia dominates the Very Happy category.

Many African and conflict-affected nations fall into Unhappy.

## 13. Most Consistently Happy Countries (Low Variance)

SQL:

SELECT Country,
       (AVG(Score*Score) - AVG(Score)*AVG(Score)) AS Variance
FROM happiness
GROUP BY Country
ORDER BY Variance ASC
LIMIT 10;

Insight

Switzerland

Denmark

Iceland
remain stable leaders.

## 14. Long-Term Trend Slope

SQL:

SELECT Country,
       SUM(Year * Score) - (SUM(Year) * SUM(Score) / COUNT(*)) AS Trend_Slope_Like
FROM happiness
GROUP BY Country
ORDER BY Trend_Slope_Like DESC;

Insight

Countries with strong upward trends often improve governance and health rapidly.

Downward trends correlate with conflict or instability.
