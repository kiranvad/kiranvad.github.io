#!/usr/bin/env python3
"""
Manual Google Scholar Stats Updater
This script provides a simple interface to manually update Google Scholar statistics
when automated fetching fails.
"""

import yaml
from datetime import datetime

# Configuration
DATA_FILE = "_data/scholar_stats.yml"

def get_user_input():
    """Get citation statistics from user input"""
    print("Google Scholar Statistics Updater")
    print("=" * 40)
    print("Please enter your current Google Scholar statistics:")
    print("(You can find these at: https://scholar.google.com/citations?user=GbNEbEkAAAAJ&hl=en)")
    print()
    
    try:
        total_citations = int(input("Total Citations: "))
        h_index = int(input("H-index: "))
        i10_index = int(input("i10-index: "))
        
        print("\nCitation distribution by year:")
        citations_by_year = {}
        current_year = datetime.now().year
        
        for year in range(2019, current_year + 1):
            citations = int(input(f"Citations in {year}: "))
            citations_by_year[year] = citations
        
        return {
            'total_citations': total_citations,
            'h_index': h_index,
            'i10_index': i10_index,
            'citations_by_year': citations_by_year
        }
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return None

def update_data_file(stats):
    """Update the YAML data file with new statistics"""
    if not stats:
        return False
    
    # Load existing data
    try:
        with open(DATA_FILE, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Data file {DATA_FILE} not found")
        return False
    
    # Update statistics
    data['total_citations'] = stats['total_citations']
    data['h_index'] = stats['h_index']
    data['i10_index'] = stats['i10_index']
    data['citations_by_year'] = stats['citations_by_year']
    data['last_updated'] = datetime.now().strftime("%Y-%m-%d")
    
    # Write updated data
    try:
        with open(DATA_FILE, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        print(f"\n✅ Updated {DATA_FILE} with new statistics")
        print(f"Total Citations: {data['total_citations']}")
        print(f"H-index: {data['h_index']}")
        print(f"i10-index: {data['i10_index']}")
        print(f"Last updated: {data['last_updated']}")
        return True
    except Exception as e:
        print(f"Error writing data file: {e}")
        return False

def main():
    """Main function"""
    print("Starting manual Google Scholar stats update...")
    
    # Get user input
    stats = get_user_input()
    
    if stats:
        # Update data file
        success = update_data_file(stats)
        if success:
            print("\n🎉 Google Scholar stats updated successfully!")
        else:
            print("\n❌ Failed to update data file")
    else:
        print("\n❌ No data provided")

if __name__ == "__main__":
    main()
