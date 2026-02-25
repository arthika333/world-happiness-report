import pandas as pd


def preprocess_data():
    # Load main dataset
    happy = pd.read_csv('Data+for+Figure+2.1+(2011–2024).csv')

    # Remove unnecessary empty columns
    happy.drop(happy.columns[13:28], axis=1, inplace=True)

    # Remove rows where all values are NaN
    happy = happy.dropna(how='all')

    # Sort by Year (descending) and Rank (ascending)
    happy.sort_values(by=['Year', 'Rank'], ascending=[False, True], inplace=True)

    # Save cleaned full dataset
    happy.to_csv('happinessranksforeachyear.csv', index=False)

    # Filter years after 2018 (for modeling convenience)
    happy2 = happy[happy['Year'] > 2018]
    happy2.to_csv('happinessranksforeachyearremoved.csv', index=False)

    # Generate Top 10 countries for 2024
    topten2024 = (
        happy2[happy2['Year'] == 2024]
        .sort_values(by=['Ladder score'], ascending=False)
        .head(10)
        .reset_index(drop=True)
    )

    topten2024.to_csv('toptencountries2024.csv', index=False)

    # Merge continent information
    continents = pd.read_csv('Countries by continents.csv')
    continents.rename({'Country': 'Country name'}, axis=1, inplace=True)

    happy2024 = pd.merge(happy2, continents, on='Country name')

    # Merge population data
    popu = pd.read_csv('World Population by country 2024.csv')
    popu.rename({'Country': 'Country name'}, axis=1, inplace=True)

    happy2024 = pd.merge(
        happy2024,
        popu[['Country name', 'Population 2024']],
        on='Country name'
    )

    # Save final merged dataset
    happy2024.to_csv('happiness2024.csv', index=False)


if __name__ == "__main__":
    preprocess_data()
