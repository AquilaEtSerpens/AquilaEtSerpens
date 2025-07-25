#!/usr/bin/env python3
"""
Olympics Data Analysis: Scandinavian Countries Gold Medals 2004

This script analyzes gold medals earned by Scandinavian countries (Denmark, Norway, Sweden)
per country and gender in the year 2004, with country-level subtotals.
"""

import pandas as pd


def create_sample_data():
    """
    Create sample Olympics data for 2004 focusing on Scandinavian countries.
    This simulates a typical Olympics dataset structure.
    """
    data = [
        # Norway gold medals 2004
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': 'Individual Sprint'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': '15km'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Biathlon', 'Event': '20km Individual'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': 'Individual Sprint'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': '10km'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Biathlon', 'Event': '15km Individual'},
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Alpine Skiing', 'Event': 'Downhill'},
        
        # Sweden gold medals 2004
        {'Year': 2004, 'Country': 'Sweden', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': '50km'},
        {'Year': 2004, 'Country': 'Sweden', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Alpine Skiing', 'Event': 'Slalom'},
        {'Year': 2004, 'Country': 'Sweden', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': '30km'},
        {'Year': 2004, 'Country': 'Sweden', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Biathlon', 'Event': '7.5km Sprint'},
        {'Year': 2004, 'Country': 'Sweden', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Alpine Skiing', 'Event': 'Giant Slalom'},
        
        # Denmark gold medals 2004
        {'Year': 2004, 'Country': 'Denmark', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Sailing', 'Event': '49er'},
        {'Year': 2004, 'Country': 'Denmark', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Sailing', 'Event': 'Europe'},
        {'Year': 2004, 'Country': 'Denmark', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Badminton', 'Event': 'Singles'},
        
        # Add some non-gold medals and other countries to make data more realistic
        {'Year': 2004, 'Country': 'Norway', 'Gender': 'Men', 'Medal': 'Silver', 'Sport': 'Speed Skating', 'Event': '1500m'},
        {'Year': 2004, 'Country': 'Finland', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Ski Jumping', 'Event': 'Large Hill'},
        {'Year': 2003, 'Country': 'Norway', 'Gender': 'Men', 'Medal': 'Gold', 'Sport': 'Cross Country Skiing', 'Event': '15km'},
        {'Year': 2005, 'Country': 'Sweden', 'Gender': 'Women', 'Medal': 'Gold', 'Sport': 'Alpine Skiing', 'Event': 'Slalom'},
    ]
    
    return pd.DataFrame(data)


def analyze_scandinavian_gold_medals(df):
    """
    Analyze gold medals for Scandinavian countries in 2004.
    
    Args:
        df (pandas.DataFrame): Olympics data
        
    Returns:
        tuple: (country_gender_counts, country_totals)
    """
    # Define Scandinavian countries
    scandinavian_countries = ['Norway', 'Sweden', 'Denmark']
    
    # Filter for 2004 data, gold medals, and Scandinavian countries
    filtered_df = df[
        (df['Year'] == 2004) & 
        (df['Medal'] == 'Gold') & 
        (df['Country'].isin(scandinavian_countries))
    ]
    
    print("Filtered data for analysis:")
    print(filtered_df[['Country', 'Gender', 'Sport', 'Event']])
    print("\n" + "="*60 + "\n")
    
    # Count gold medals per country and gender
    country_gender_counts = filtered_df.groupby(['Country', 'Gender']).size().reset_index(name='Gold_Medals')
    
    # Generate country-level subtotals
    country_totals = filtered_df.groupby('Country').size().reset_index(name='Total_Gold_Medals')
    
    return country_gender_counts, country_totals


def display_results(country_gender_counts, country_totals):
    """
    Display the analysis results in a formatted way.
    
    Args:
        country_gender_counts (pandas.DataFrame): Gold medals by country and gender
        country_totals (pandas.DataFrame): Total gold medals by country
    """
    print("SCANDINAVIAN COUNTRIES - GOLD MEDALS ANALYSIS (2004)")
    print("="*60)
    
    print("\n1. Gold Medals by Country and Gender:")
    print("-" * 40)
    for _, row in country_gender_counts.iterrows():
        print(f"{row['Country']} - {row['Gender']}: {row['Gold_Medals']} gold medals")
    
    print(f"\n2. Country-Level Subtotals:")
    print("-" * 30)
    for _, row in country_totals.iterrows():
        print(f"{row['Country']}: {row['Total_Gold_Medals']} total gold medals")
    
    # Display in table format
    print(f"\n3. Detailed Table Format:")
    print("-" * 35)
    print("\nGold Medals by Country and Gender:")
    print(country_gender_counts.to_string(index=False))
    
    print(f"\nCountry-Level Subtotals:")
    print(country_totals.to_string(index=False))


def main():
    """
    Main function to execute the Olympics data analysis.
    """
    print("Olympics Data Analysis: Scandinavian Countries Gold Medals 2004")
    print("="*70)
    print()
    
    # Create or load sample data
    df = create_sample_data()
    
    print("Sample data created with the following structure:")
    print(f"Total records: {len(df)}")
    print(f"Years covered: {sorted(df['Year'].unique())}")
    print(f"Countries: {sorted(df['Country'].unique())}")
    print(f"Medal types: {sorted(df['Medal'].unique())}")
    print("\n" + "="*70 + "\n")
    
    # Perform analysis
    country_gender_counts, country_totals = analyze_scandinavian_gold_medals(df)
    
    # Display results
    display_results(country_gender_counts, country_totals)


if __name__ == "__main__":
    main()