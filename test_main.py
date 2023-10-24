import pytest

from main import main
from _pytest.capture import CaptureResult


@pytest.mark.parametrize("num_of_days, result", [(5, "14/29"), (10, "372/773")])
def test_university_problem(capsys, num_of_days, result):
    main(num_of_days=num_of_days)
    captured: CaptureResult[AnyStr] = capsys.readouterr()
    assert captured.out == result
