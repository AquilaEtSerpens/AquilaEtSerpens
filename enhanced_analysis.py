#!/usr/bin/env python3
"""
Enhanced Olympics Data Analysis with Visualization
Demonstrates the analysis with additional formatting and summary statistics.
"""

import pandas as pd
from olympics_analysis import create_sample_data, analyze_scandinavian_gold_medals


def create_summary_table(country_gender_counts, country_totals):
    """
    Create a comprehensive summary table combining gender breakdown and totals.
    
    Args:
        country_gender_counts (pandas.DataFrame): Gold medals by country and gender
        country_totals (pandas.DataFrame): Total gold medals by country
        
    Returns:
        pandas.DataFrame: Combined summary table
    """
    # Pivot the gender counts to have Men and Women as columns
    pivot_table = country_gender_counts.pivot(index='Country', columns='Gender', values='Gold_Medals').fillna(0)
    
    # Ensure we have both Men and Women columns
    if 'Men' not in pivot_table.columns:
        pivot_table['Men'] = 0
    if 'Women' not in pivot_table.columns:
        pivot_table['Women'] = 0
    
    # Add total column
    country_totals_dict = dict(zip(country_totals['Country'], country_totals['Total_Gold_Medals']))
    pivot_table['Total'] = pivot_table.index.map(country_totals_dict)
    
    # Reorder columns
    pivot_table = pivot_table[['Men', 'Women', 'Total']]
    
    # Convert to int for cleaner display
    pivot_table = pivot_table.astype(int)
    
    return pivot_table


def display_enhanced_results(country_gender_counts, country_totals):
    """
    Display results with enhanced formatting and additional insights.
    
    Args:
        country_gender_counts (pandas.DataFrame): Gold medals by country and gender
        country_totals (pandas.DataFrame): Total gold medals by country
    """
    print("🏅 SCANDINAVIAN COUNTRIES - GOLD MEDALS ANALYSIS (2004)")
    print("=" * 65)
    
    # Create summary table
    summary_table = create_summary_table(country_gender_counts, country_totals)
    
    print("\n📊 COMPREHENSIVE SUMMARY TABLE")
    print("-" * 35)
    print(summary_table.to_string())
    
    # Additional statistics
    total_medals = country_totals['Total_Gold_Medals'].sum()
    leading_country = country_totals.loc[country_totals['Total_Gold_Medals'].idxmax(), 'Country']
    leading_count = country_totals['Total_Gold_Medals'].max()
    
    print(f"\n📈 KEY INSIGHTS")
    print("-" * 20)
    print(f"• Total Scandinavian gold medals in 2004: {total_medals}")
    print(f"• Leading country: {leading_country} ({leading_count} gold medals)")
    
    # Gender distribution analysis
    men_total = country_gender_counts[country_gender_counts['Gender'] == 'Men']['Gold_Medals'].sum()
    women_total = country_gender_counts[country_gender_counts['Gender'] == 'Women']['Gold_Medals'].sum()
    
    print(f"• Men's gold medals: {men_total} ({men_total/total_medals*100:.1f}%)")
    print(f"• Women's gold medals: {women_total} ({women_total/total_medals*100:.1f}%)")
    
    # Country rankings
    print(f"\n🏆 COUNTRY RANKINGS")
    print("-" * 20)
    ranked_countries = country_totals.sort_values('Total_Gold_Medals', ascending=False)
    for i, (_, row) in enumerate(ranked_countries.iterrows(), 1):
        print(f"{i}. {row['Country']}: {row['Total_Gold_Medals']} gold medals")


def main():
    """
    Main function for enhanced Olympics data analysis.
    """
    print("Enhanced Olympics Data Analysis")
    print("=" * 40)
    print()
    
    # Load data and perform analysis
    df = create_sample_data()
    country_gender_counts, country_totals = analyze_scandinavian_gold_medals(df)
    
    # Display enhanced results
    display_enhanced_results(country_gender_counts, country_totals)
    
    print(f"\n" + "=" * 65)
    print("Analysis complete! ✨")


if __name__ == "__main__":
    main()