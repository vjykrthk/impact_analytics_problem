import pytest

from main import main


@pytest.mark.parametrize("num_of_days, expected", [(5, "14/29"), (10, "372/773")])
def test_university_problem(capsys, num_of_days, expected):
    result = main(num_of_days=num_of_days)
    assert result == expected
