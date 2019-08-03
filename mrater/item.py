from dataclasses import dataclass


@dataclass
class Item:
    """Data describing a single movie"""

    id: str
    title: str
    description: str
    rating: float
    poster: str
