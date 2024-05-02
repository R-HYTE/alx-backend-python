#!/usr/bin/env python3
"""Module for safely retrieving values from mappings with type annotations."""

from typing import Any, Mapping, TypeVar, Optional

T = TypeVar('T')  # Generic type for value types within the dictionary


def safely_get_value(dct: Mapping[Any, T],
                     key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """
    Retrieve a value from a dictionary by key with a default fallback.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to find in the dictionary.
        default (Optional[T], optional): Fallback value if the key is absent.
                                            Defaults to None.

    Returns:
        Optional[T]: Value from the dictionary or the default if key is absent.
    """
    return dct.get(key, default)
