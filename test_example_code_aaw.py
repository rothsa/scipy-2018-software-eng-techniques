"""Tests for example_code_aaw.py"""

import example_code_aaw as eca

def test_load_file():
    """Test that sf_restaurant_scores_subset.csv loads as expected."""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')

    # Assert that there are 10 rows of data in the dataset.
    assert len(data) == 10
    # Assert that for a given row, it has 17 datapoints.
    assert len(data[0]) == 17


def test_filter_by_inspection_type():
    """Test that only records with 'inspection_type' == 'Routine - Unscheduled' remain"""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')
    filtered_data = eca.filter_by_inspection_type(data)

    # Assert that all 9 rows with 'Routine - Unscheduled' inspections remain
    assert len(filtered_data) == 9
    # Assert that for every row, inspection_type is 'Routine - Unscheduled'
    assert all(row['inspection_type'] == 'Routine - Unscheduled' for row in filtered_data)


def test_filter_by_month():
    """Test filter by specific month"""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')
    filtered_data = eca.filter_by_inspection_type(data)
    month_data = eca.filter_by_month(filtered_data, '12', '2017')

    assert len(month_data) == 3


def test_count_restaurants_by_risk_score():
    """Test that we aggregate risk scores properly"""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')
    filtered_data = eca.filter_by_inspection_type(data)
    aggregated_data = eca.count_restaurants_by_risk_score(filtered_data)

    assert aggregated_data == {
        'Low Risk': 2,
        'Moderate Risk': 2,
        'High Risk': 3,
        'No Violations': 1,
    }


def test_calculate_risk_categories():
    """Integration test"""
    final_data = eca.calculate_risk_categories(
        filename='data/sf_restaurant_scores_subset.csv',
        input_month='12',
        input_year='2017',
    )

    assert final_data == {
        'High Risk': 1,
        'Moderate Risk': 1,
        'No Violations': 1,
    }
