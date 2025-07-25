#!/usr/bin/env python3
"""
Test script for Olympics data analysis functionality.
"""

import pandas as pd
from olympics_analysis import create_sample_data, analyze_scandinavian_gold_medals


def test_data_structure():
    """Test that the sample data has the expected structure."""
    df = create_sample_data()
    
    # Test basic structure
    assert not df.empty, "Data should not be empty"
    assert 'Year' in df.columns, "Data should have Year column"
    assert 'Country' in df.columns, "Data should have Country column"
    assert 'Gender' in df.columns, "Data should have Gender column"
    assert 'Medal' in df.columns, "Data should have Medal column"
    
    # Test that we have 2004 data for Scandinavian countries
    scandinavian_2004_gold = df[
        (df['Year'] == 2004) & 
        (df['Medal'] == 'Gold') & 
        (df['Country'].isin(['Norway', 'Sweden', 'Denmark']))
    ]
    assert not scandinavian_2004_gold.empty, "Should have 2004 gold medals for Scandinavian countries"
    
    print("✓ Data structure test passed")


def test_analysis_functionality():
    """Test the analysis functions."""
    df = create_sample_data()
    country_gender_counts, country_totals = analyze_scandinavian_gold_medals(df)
    
    # Test country-gender counts
    assert not country_gender_counts.empty, "Country-gender counts should not be empty"
    assert 'Country' in country_gender_counts.columns, "Should have Country column"
    assert 'Gender' in country_gender_counts.columns, "Should have Gender column"
    assert 'Gold_Medals' in country_gender_counts.columns, "Should have Gold_Medals column"
    
    # Test country totals
    assert not country_totals.empty, "Country totals should not be empty"
    assert 'Country' in country_totals.columns, "Should have Country column"
    assert 'Total_Gold_Medals' in country_totals.columns, "Should have Total_Gold_Medals column"
    
    # Test that all three Scandinavian countries are represented
    countries_in_totals = set(country_totals['Country'].tolist())
    expected_countries = {'Norway', 'Sweden', 'Denmark'}
    assert expected_countries.issubset(countries_in_totals), f"Should have all Scandinavian countries: {expected_countries}"
    
    # Test that totals match sum of gender counts for each country
    for _, country_row in country_totals.iterrows():
        country = country_row['Country']
        expected_total = country_row['Total_Gold_Medals']
        
        gender_sum = country_gender_counts[
            country_gender_counts['Country'] == country
        ]['Gold_Medals'].sum()
        
        assert gender_sum == expected_total, f"Gender sum ({gender_sum}) should equal country total ({expected_total}) for {country}"
    
    print("✓ Analysis functionality test passed")


def test_expected_results():
    """Test that we get expected results from the sample data."""
    df = create_sample_data()
    country_gender_counts, country_totals = analyze_scandinavian_gold_medals(df)
    
    # Based on our sample data, we should have:
    # Norway: 3 men + 4 women = 7 total
    # Sweden: 2 men + 3 women = 5 total  
    # Denmark: 1 men + 2 women = 3 total
    
    totals_dict = dict(zip(country_totals['Country'], country_totals['Total_Gold_Medals']))
    
    assert totals_dict['Norway'] == 7, f"Norway should have 7 gold medals, got {totals_dict['Norway']}"
    assert totals_dict['Sweden'] == 5, f"Sweden should have 5 gold medals, got {totals_dict['Sweden']}"
    assert totals_dict['Denmark'] == 3, f"Denmark should have 3 gold medals, got {totals_dict['Denmark']}"
    
    print("✓ Expected results test passed")


def main():
    """Run all tests."""
    print("Running Olympics Analysis Tests...")
    print("=" * 40)
    
    try:
        test_data_structure()
        test_analysis_functionality()
        test_expected_results()
        
        print("\n" + "=" * 40)
        print("✅ All tests passed successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return 1
        
    return 0


if __name__ == "__main__":
    exit(main())