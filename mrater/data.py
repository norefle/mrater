import uuid

from mrater.item import Item
from typing import List, Optional, Tuple


def load(page: int) -> Optional[Tuple[Item, List[Item]]]:
    if 1 < page or page < 0:
        return None

    db = {
        0: (
            Item(
                id=str(uuid.uuid4()),
                title="Attack of 50 foot woman",
                description="""Attack of the 50 Foot Woman is a 1958 independently made
American black-and-white science fiction film, produced by Bernard Woolner,
directed by Nathan H. Juran (credited as Nathan Hertz), that stars Allison
Hayes, William Hudson and Yvette Vickers. The screenplay was written by Mark
Hanna, and the original music score was composed by Ronald Stein. The film was
distributed in the United States by Allied Artists as a double feature with War
of the Satellites.""",
                rating=3.4,
                poster="poster-sm-wiki-4.jpg",
            ),
            [
                Item(
                    id=str(uuid.uuid4()),
                    title="Blockbuster",
                    description="Movie of the year",
                    rating=4.4,
                    poster="poster-sm-wiki-2.png",
                ),
                Item(
                    id=str(uuid.uuid4()),
                    title="This gun for hire",
                    description="Best movie ever",
                    rating=3.2,
                    poster="poster-sm-wiki-3.jpg",
                ),
                Item(
                    id=str(uuid.uuid4()),
                    title="Unknown",
                    description="No description",
                    rating=4.8,
                    poster="poster-sm-wiki-1.png",
                ),
            ],
        ),
        1: (
            Item(
                id=str(uuid.uuid4()),
                title=f"Броненосец Потёмкин",
                description="""Battleship Potemkin (Russian: Бронено́сец «Потёмкин»,
Bronenosets Potyomkin), sometimes rendered as Battleship Potyomkin,
is a 1925 Soviet silent film directed by Sergei Eisenstein and produced
by Mosfilm. It presents a dramatized version of the mutiny that occurred
in 1905 when the crew of the Russian battleship Potemkin rebelled against
its officers.

Battleship Potemkin was named the greatest film of all time at the Brussels
World's Fair in 1958.[1][2][3] In 2012, the British Film Institute named
it the eleventh greatest film of all time.[4]
""",
                rating=3.4,
                poster="poster-sm-wiki-6.jpg",
            ),
            [
                Item(
                    id=str(uuid.uuid4()),
                    title="Hunterwali",
                    description="Something to watch?",
                    rating=2.0,
                    poster="poster-sm-wiki-5.jpg",
                ),
                Item(
                    id=str(uuid.uuid4()),
                    title="Hunterwali",
                    description="Something to watch?",
                    rating=3.1,
                    poster="poster-sm-wiki-2.png",
                ),
            ],
        ),
    }

    return db[page]
