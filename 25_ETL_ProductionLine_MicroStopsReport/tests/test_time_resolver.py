
import sys
import os

# Add the parent directory (the root of your project) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from time_resolver import TimeResolver


# parametrize of test
@pytest.mark.parametrize("input_string, expected_output", [
    ("1h 24min", ["1", "h", "24", "min"]),
    ("3h 45min", ["3", "h", "45", "min"]),
    ("2h", ["2", "h"]),
    ("30min", ["30", "min"]),
    ("1", ["1"]),
    (" ", [""]),
])

def test_extract_words_and_numbers_from_given_string(input_string, expected_output):
    string_extract = TimeResolver()
    result = string_extract._extracting_words_and_numbers_from_string(input_string)
    assert result == expected_output

# parametrize of test
@pytest.mark.parametrize("input_string, expected_output", [
    (["1", "h", "24", "min"], [[1,60], [24, 1]]),
    (["3", "h", "45", "min"], [[3, 60], [45, 1]]),
    (["2", "h"], [[2, 60]]),
    (["30", "min"], [[30,1]])
])

def test_extract_time_from_array_of_words_and_numbers(input_string, expected_output):
    time_extract = TimeResolver()
    result = time_extract._extracting_time_from_array_of_words_and_numbers(input_string)
    assert result == expected_output

# parametrize of test
@pytest.mark.parametrize("input_string, expected_output", [
    ("min", 1),
    ("h", 60)
])

def test_retrive_multiplicator_from_word(input_string, expected_output):
    multiplicator = TimeResolver()
    result = multiplicator._retrive_multiplicator_from_word(input_string)
    assert result == expected_output


# parametrize of test
@pytest.mark.parametrize("input_string, expected_output", [
    ([[1, 60], [30, 1]], 90),
])
def test_resolve_time_from_final_array(input_string, expected_output):
    time_resolved = TimeResolver()
    result = time_resolved._resolve_time_from_final_array(input_string)
    assert result == expected_output