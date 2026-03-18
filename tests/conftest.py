import pytest
import pandas as pd

@pytest.fixture
def sample_df():
    sample_dict = {"id": [1, 2], "state": ["CANCELED", "CANCELED"]}
    return pd.DataFrame(sample_dict)