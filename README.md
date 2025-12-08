**World Happiness Dataset - Data Analysis Report**

_Using SQLite-Based Insights_

**1\. Overview of the Dataset**

The World Happiness dataset captures global well-being measures using key indicators such as:

- Happiness Score
- GDP per Capita
- Social Support
- Healthy Life Expectancy
- Freedom
- Generosity
- Perceptions of Corruption
- Region (available for some years)

This analysis uses SQL queries to examine trends, rankings, improvements, and relationships between socioeconomic factors and happiness.

**2\. Key Analytical Findings**

**2.1 Top 10 Happiest Countries (Across All Years)**

Countries with the highest recorded happiness scores represent global leaders in well-being.  
These countries often have strong social support, high GDP, low corruption, and healthy life expectancy.

**Insight**

- High-scoring nations maintain exceptional living standards.
- They often appear repeatedly in annual reports, indicating long-term stability rather than temporary surges.

**2.2 Global Happiness Trend Over Time (Yearly Averages)**

Average happiness scores per year reveal whether global happiness is rising, falling, or stable.

**Insight**

- In many global datasets, happiness is remarkably stable year-to-year.
- Declines in certain years often correlate with global crises or economic shocks.

**2.3 Average Happiness Score per Country (Long-Term Rankings)**

Calculating long-term averages helps identify consistently happy countries.

**Insight**

- Countries like Finland, Denmark, Switzerland, Iceland, and Netherlands often remain at the top.
- Stability in happiness is strongly associated with strong institutions, social equality, and strong community trust.

**2.4 Countries With the Largest Change (2015 → 2019)**

Analyzing improvement and decline between two benchmark years reveals significant shifts.

**Improvers Insight**

- Nations with large positive change often experienced:
  - Economic reforms
  - Increased political stability
  - Improved social welfare

**Decliners Insight**

- Negative change may indicate:
  - Conflict or political disruption
  - Economic recession
  - Reduced social security or increased corruption

These comparisons help track progress over medium-term periods.

**2.5 Top Countries by GDP per Capita**

GDP per capita rankings identify the world's wealthiest countries in the dataset.

**Insight**

- Wealth strongly affects happiness but is **not the only driver**.
- Some wealthy countries do not rank high in happiness due to inequality or governance problems.

**2.6 Top Countries with Highest Social Support**

High social support scores reflect strong community bonds and reliable help networks.

**Insight**

- Social support is one of the strongest indicators of happiness.
- Even countries with moderate GDP can achieve high happiness with strong social structures.

**2.7 Average Happiness by Region**

This measures how entire regions perform on average.

**Insight**

- Western Europe and North America typically score highest.
- Sub-Saharan Africa consistently shows lower regional averages due to economic and political challenges.
- Regional variations reflect cultural, economic, and political differences.

**2.8 Lowest Corruption Countries**

Low corruption is measured by low _Perceptions_of_Corruption_ scores.

**Insight**

- Countries with low corruption often rank high in happiness.
- This suggests strong trust in public institutions and effective governance.
- Transparency and fairness contribute heavily to well-being.

**2.9 Freedom vs. Happiness Relationship**

Exploring freedom and happiness together shows how personal and societal freedom impact well-being.

**Insight**

- Higher freedom generally correlates with higher happiness.
- Exceptions occur in countries with high freedom but economic or social instability.

**2.10 Year-Specific Happiness Rankings (Example: 2018)**

Ranking countries within a single year helps highlight top performers and yearly shifts.

**Insight**

- Useful for dashboards, media reports, and year-by-year comparisons.
- Helps identify emerging trends within specific time frames.

**2.11 Missing Data Detection**

Checking for missing values ensures that analysis is reliable and complete.

**Insight**

- Missing values can affect averages, rankings, and correlations.
- Data cleaning is required before advanced modeling.

**2.12 Country-Specific Trends (Example: Finland)**

Examining a single country's scores over all years shows its long-term trajectory.

**Insight**

- Long-term improvement indicates policy success and stable growth.
- Decline highlights stressors such as conflict, inequality, or economic downturn.

**3\. Summary of Findings**

**Overall Patterns**

- Northern European countries dominate global happiness rankings.
- Social support, trust, and freedom are consistently strong predictors of high happiness scores.
- Wealth contributes to happiness, but only when combined with low corruption and strong social systems.

**Trends Over Time**

- Global happiness tends to be stable year-to-year.
- Significant fluctuations are usually tied to major economic or political events.

**Improvement & Decline**

- Some nations show dramatic improvements over multiple years.
- Others experience noticeable declines due to unrest, recession, or governance issues.

**Data Quality**

- Missing data exists and must be addressed before applying machine learning or forecasting.

**4\. Final Conclusion**

This analysis provides a comprehensive view of global happiness, identifying the most influential factors, long-term leaders, rising and declining countries, and regional patterns.

The results support:

- Policy decision-making
- International development research
- Power BI dashboards
- Trend forecasting
- Data storytelling and presentations
