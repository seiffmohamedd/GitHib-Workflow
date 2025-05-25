import pytest
from extract import extract
from transform import transform

def test_api_response():
    data = extract()
    assert isinstance(data, list)
    assert len(data) > 0
    # Test keys expected in each dict
    keys = {'userId', 'id', 'title', 'body'}
    for item in data:
        assert keys.issubset(item.keys())

def test_transform_sample():
    sample_data = [
        {"userId": 1, "id": 1, "title": "title1", "body": "body1"},
        {"userId": 1, "id": 2, "title": "title2", "body": "body2"},
        {"userId": 2, "id": 3, "title": "title3", "body": "body3"},
        {"userId": 2, "id": 3, "title": "title3", "body": "body3"}  # duplicate row
    ]
    clean_df, agg_df = transform(sample_data)
    # Check duplicate removal
    assert len(clean_df) == 3
    # Check aggregation counts
    user1_count = agg_df[agg_df['userId'] == 1]['post_count'].values[0]
    user2_count = agg_df[agg_df['userId'] == 2]['post_count'].values[0]
    assert user1_count == 2
    assert user2_count == 1
