import pytest

@pytest.fixture
def sample_data():
    var = [1, 2, 3]
    var.append(4)
    return var 