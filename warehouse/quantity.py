"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a non-negative quantity, raising ValueError for invalid values."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
