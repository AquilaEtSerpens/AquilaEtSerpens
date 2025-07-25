# Olympics Data Analysis: Scandinavian Countries 2004

This project analyzes gold medals earned by Scandinavian countries (Denmark, Norway, Sweden) per country and gender in the year 2004, with country-level subtotals.

## Features

- ✅ Count gold medals awarded per country and gender
- ✅ Generate country-level gold award counts  
- ✅ Focus on three Scandinavian countries (Denmark, Norway, Sweden)
- ✅ Year 2004 specific analysis
- ✅ Excludes gender-level subtotals as requested

## Requirements

- Python 3.7+
- pandas

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run the Analysis

```bash
python3 olympics_analysis.py
```

This will output:
1. Filtered data showing the gold medals for analysis
2. Gold medals count by country and gender
3. Country-level subtotals
4. Results in both narrative and table format

### Run Tests

```bash
python3 test_olympics_analysis.py
```

## Sample Output

```
SCANDINAVIAN COUNTRIES - GOLD MEDALS ANALYSIS (2004)
============================================================

1. Gold Medals by Country and Gender:
----------------------------------------
Denmark - Men: 1 gold medals
Denmark - Women: 2 gold medals
Norway - Men: 3 gold medals
Norway - Women: 4 gold medals
Sweden - Men: 2 gold medals
Sweden - Women: 3 gold medals

2. Country-Level Subtotals:
------------------------------
Denmark: 3 total gold medals
Norway: 7 total gold medals
Sweden: 5 total gold medals
```

## Data Structure

The analysis expects Olympics data with the following columns:
- `Year`: Competition year
- `Country`: Country name
- `Gender`: 'Men' or 'Women'
- `Medal`: Medal type ('Gold', 'Silver', 'Bronze')
- `Sport`: Sport category
- `Event`: Specific event name

## Implementation Details

- **Scandinavian Countries**: Denmark, Norway, Sweden
- **Year Filter**: 2004 only
- **Medal Filter**: Gold medals only
- **Grouping**: By country and gender, with country-level aggregation
- **Output**: Both detailed breakdown and summary totals

## Files

- `olympics_analysis.py`: Main analysis script
- `test_olympics_analysis.py`: Test suite
- `requirements.txt`: Python dependencies
- `README_Olympics.md`: This documentation