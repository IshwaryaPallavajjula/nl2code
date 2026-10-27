from typing import List, TypeVar, Iterable

T = TypeVar('T')

def remove_duplicates(items: List[T]) -> List[T]:
    """
    Return a new list containing the elements of `items` with duplicates removed,
    preserving the original order of first occurrence.
    """
    result: List[T] = []
    seen_hashable = set()
    seen_unhashable: List[T] = []

    for item in items:
        try:
            if item not in seen_hashable:
                seen_hashable.add(item)
                result.append(item)
        except TypeError:
            # Item is unhashable; fall back to linear search in seen_unhashable
            if item not in seen_unhashable:
                seen_unhashable.append(item)
                result.append(item)
    return result
