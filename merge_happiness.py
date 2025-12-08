import pandas as pd

# List of years
years = [2015, 2016, 2017, 2018, 2019]

# Dictionary to map original column names to standardized names for each year
column_mappings = {
    2015: {
        'Country': 'Country',
        'Region': 'Region',
        'Happiness Rank': 'Rank',
        'Happiness Score': 'Score',
        'Standard Error': 'Standard_Error',
        'Economy (GDP per Capita)': 'GDP_per_Capita',
        'Family': 'Social_Support',
        'Health (Life Expectancy)': 'Healthy_Life_Expectancy',
        'Freedom': 'Freedom',
        'Trust (Government Corruption)': 'Perceptions_of_Corruption',
        'Generosity': 'Generosity',
        'Dystopia Residual': 'Dystopia_Residual'
    },
    2016: {
        'Country': 'Country',
        'Region': 'Region',
        'Happiness Rank': 'Rank',
        'Happiness Score': 'Score',
        'Lower Confidence Interval': 'Lower_CI',
        'Upper Confidence Interval': 'Upper_CI',
        'Economy (GDP per Capita)': 'GDP_per_Capita',
        'Family': 'Social_Support',
        'Health (Life Expectancy)': 'Healthy_Life_Expectancy',
        'Freedom': 'Freedom',
        'Trust (Government Corruption)': 'Perceptions_of_Corruption',
        'Generosity': 'Generosity',
        'Dystopia Residual': 'Dystopia_Residual'
    },
    2017: {
        'Country': 'Country',
        'Happiness.Rank': 'Rank',
        'Happiness.Score': 'Score',
        'Whisker.high': 'Whisker_High',
        'Whisker.low': 'Whisker_Low',
        'Economy..GDP.per.Capita.': 'GDP_per_Capita',
        'Family': 'Social_Support',
        'Health..Life.Expectancy.': 'Healthy_Life_Expectancy',
        'Freedom': 'Freedom',
        'Generosity': 'Generosity',
        'Trust..Government.Corruption.': 'Perceptions_of_Corruption',
        'Dystopia.Residual': 'Dystopia_Residual'
    },
    2018: {
        'Overall rank': 'Rank',
        'Country or region': 'Country',
        'Score': 'Score',
        'GDP per capita': 'GDP_per_Capita',
        'Social support': 'Social_Support',
        'Healthy life expectancy': 'Healthy_Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions_of_Corruption'
    },
    2019: {
        'Overall rank': 'Rank',
        'Country or region': 'Country',
        'Score': 'Score',
        'GDP per capita': 'GDP_per_Capita',
        'Social support': 'Social_Support',
        'Healthy life expectancy': 'Healthy_Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Perceptions_of_Corruption'
    }
}

# List to hold dataframes
dfs = []

for year in years:
    # Read the Excel file (assuming files are named like '2015.xlsx')
    file_name = f'{year}.csv'
    df = pd.read_csv(file_name)
    
    # Rename columns using the mapping
    mapping = column_mappings[year]
    df = df.rename(columns=mapping)
    
    # Add Year column
    df['Year'] = year
    
    # Append to list
    dfs.append(df)

# Concatenate all dataframes
merged_df = pd.concat(dfs, ignore_index=True, sort=False)

# Save the merged dataframe to a new Excel file
merged_df.to_excel('merged_happiness_data.xlsx', index=False)

print("Merged dataset saved as 'merged_happiness_data.xlsx'")