from typing import Dict, Any
import numbers

def merge_sum_dicts(dict1: Dict[Any, numbers.Number], dict2: Dict[Any, numbers.Number]) -> Dict[Any, numbers.Number]:
    """
    Merge two dictionaries, summing values for keys that appear in both.
    Non-numeric values raise a TypeError.
    """
    if dict1 is None:
        dict1 = {}
    if dict2 is None:
        dict2 = {}

    result: Dict[Any, numbers.Number] = {}

    for d in (dict1, dict2):
        for key, value in d.items():
            if not isinstance(value, numbers.Number):
                raise TypeError(f"Value for key {key!r} is not numeric: {value!r}")
            result[key] = result.get(key, 0) + value

    return result
