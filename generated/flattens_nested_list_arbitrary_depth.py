from typing import List, Any

def flatten(nested: List[Any]) -> List[Any]:
    """
    Flattens a nested list of arbitrary depth.

    Args:
        nested: A list which may contain other lists nested within it.

    Returns:
        A new list containing all the non-list elements from the original structure,
        preserving their original order.
    """
    result: List[Any] = []
    stack: List[Any] = list(reversed(nested))

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            # Extend the stack with the items of the sublist in reverse order
            # so that they are processed in the original order.
            stack.extend(reversed(item))
        else:
            result.append(item)

    return result
