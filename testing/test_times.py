from times import compute_overlap_time, time_range
import pytest

interval_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
interval_2 = time_range("2010-01-12 13:45:00", "2010-01-12 14:00:00")
interval_3 = time_range("2010-01-12 11:00:00", "2010-01-12 13:45:00")
interval_4 = time_range("2010-01-12 09:45:00", "2010-01-12 11:00:00", 2, 60)
interval_5 = time_range("2010-01-12 09:45:00", "2010-01-12 11:00:00", 3, 60)
interval_6 = time_range("2010-01-12 12:00:00", "2020-01-12 13:00:00")
interval_8 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2, 60)

@pytest.mark.parametrize("test_input",
                            [
                                ([interval_1, interval_2]), 
                                ([interval_1, interval_3])       
                            ]
                        )

def test_no_overlap(test_input):
    result = compute_overlap_time(test_input[0], test_input[1])
    assert result == []

@pytest.mark.parametrize("test_input",
                            [
                                ([interval_4, interval_5]),
                                ([interval_1, interval_4])
                            ]
                        )

def test_multiple_intervals(test_input):
    assert len(test_input[0]) > 1 and len(test_input[1]) > 1

@pytest.mark.parametrize("test_input",
                            [
                                ([interval_1, interval_2]),
                                ([interval_1, interval_6]),
                            ]
                        )

def test_consecutive(test_input):
    assert test_input[0][0][0] == test_input[1][-1][-1] or test_input[0][-1][-1] == test_input[1][0][0]