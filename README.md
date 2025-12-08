# Global-Happiness-Dataset
## 1. Executive Summary

This report presents a complete analytical exploration of global happiness trends between 2015 and 2019, using SQL-driven insights and statistical interpretation.
Key areas examined include:

Year-over-year changes

Happiness volatility

Factor influence (GDP, social support, corruption, etc.)

Predicted vs actual happiness performance

Regional comparisons

Classification and clustering

Trend analysis

Findings show that global happiness remained moderately stable, with small fluctuations driven by economic cycles.
Scandinavian countries consistently rank highest, while conflict-affected and economically strained regions remain lowest.

# 2. Dataset Overview

The dataset contains the following fields (per country per year):

Score — Overall happiness index

GDP_per_Capita

Social_Support

Healthy_Life_Expectancy

Freedom

Generosity

Perceptions_of_Corruption

Region, Rank, Year, confidence intervals, etc.

Total records: Multiple countries × 5 years (2015–2019).

# 3. Global Trends
### 3.1 Average Happiness Over Time

A figure was generated from the uploaded dataset showing year-by-year global averages.

Key Findings:

Happiness scores show mild decline from 2016 to 2017, aligning with global political uncertainty.

From 2017 to 2019, global happiness steadily improved.

Overall, happiness scores remain within a very narrow range (±0.05), suggesting global stability.

# 4. Year-Over-Year Happiness Change

Using SQL joins across consecutive years, each country’s improvement or decline was computed.

Insights:

Countries with strong economies or recovery programs (e.g., Eastern Europe, parts of Latin America) show strong positive YoY growth.

Sharp declines usually correlate with:

Political crises

Recession

Conflict

Institutional instability

Countries with consistently positive YoY change are prime candidates for deeper case studies on stable governance and policy effectiveness.

# 5. Volatility Index (Stability of Happiness)

Volatility was measured using variance of happiness scores per country.

Interpretation:

High-variance countries tend to experience:

Conflict (e.g., Middle East, parts of Africa)

Economic swings (e.g., oil-dependent economies)

Political instability

Low-variance countries (stable happiness):

Switzerland

Denmark

Iceland

Netherlands
These show long-term social and institutional stability.

# 6. Influence of Key Happiness Factors

A correlation-like analysis was performed (covariance approximations due to SQLite limitations).

Most influential predictors:

Social Support

Healthy Life Expectancy

GDP per Capita

Freedom

Weaker or more mixed predictors:

Generosity — varies widely culturally

Perceptions of Corruption — strong negative effect but inconsistent across regions

Insight:
Countries with strong community bonds, health systems, and wealth rank highest overall.

# 7. Component Score Analysis

Each country received a “Component Strength Score,” calculated as:

Sum of all positive variables – corruption

Interpretation:

Countries with strong components match expected high happiness (Finland, Switzerland).

Some countries have strong components but underperform emotionally or socially.

This led to the next stage of analysis.

# 8. Overperformers vs Underperformers

Comparing predicted vs actual happiness:

Overperformers

Countries happier than expected for their economic and social levels.
Common patterns include:

Strong cultural unity

High resilience

Community-centered living

Lower income inequality despite lower GDP

Examples often include:
Costa Rica, Mexico, some Southeast Asian nations.

Underperformers

Countries with strong GDP and infrastructure but lower emotional well-being.
Common patterns include:

High stress

Inequality

Institutional distrust

Mental health challenges

Examples include some wealthy but high-pressure countries.

# 9. Regional Happiness Analysis
Top Regions (Highest Avg Scores)

Western Europe

North America & ANZ

Latin America & Caribbean

Lowest Regions

Sub-Saharan Africa

South Asia

Middle East & North Africa (impacted by conflict cycles)

Trends by Region

Western Europe is consistently stable.

MENA shows large swings linked to geopolitical instability.

Africa remains lowest due to sustained structural challenges.

# 10. Anomalies: Freedom vs Happiness

SQL filtering showed countries with high freedom (>0.5) but low happiness (<5).

Insight:
High political freedom does not guarantee happiness.
Economic hardship, unemployment, insecurity, and poor healthcare can overshadow democratic structures.

# 11. High Corruption but High Happiness

This fascinating anomaly highlights countries scoring:

Corruption > 0.4

Happiness among the top global ranks

These nations often:

Prioritize family and social bonds

Emphasize cultural happiness norms

Compensate for institutional weakness with strong community support

# 12. Generosity Ranking

The top 15 most generous countries were computed by average generosity.

Key Insight:
Generosity is not tied strongly to GDP.
Many of the most generous countries are mid-income nations with strong cultural norms of giving and community support.

# 13. Consistency: The 10 Most Stable Countries

By computing variance, the analyst can identify countries with the least fluctuation in happiness.

These nations tend to have:

Strong rule of law

Predictable governance

Equitable economic distribution

Strong welfare and support systems

These characteristics make them ideal benchmarks for policy studies.

# 14. Long-Term Trend Slope (2015–2019)

Trend slope calculations rate each country as:

Improving long-term

Declining long-term

Statistically stable

Improving Countries

Often developing countries experiencing growth and stability.

Declining Countries

Often wealthy countries dealing with:

Rising inequality

Stress and burnout

Declining trust

Stable Countries

Mostly Nordic countries and a few Western European nations.

# 15. Final Conclusions
Global Findings

Global happiness is stable but unevenly distributed.

Scandinavian countries consistently lead due to strong institutions, social cohesion, and healthcare.

Conflict regions experience predictable declines.

Economic factors matter, but social support and wellbeing are stronger predictors.

Analyst Recommendations

Further machine learning modeling could provide predictive accuracy for next-year scores.

Regional case studies can uncover qualitative factors beyond numerical indicators.

Power BI dashboards can visualize:

Trends

Regional disparities

Component contributions

Outliers
