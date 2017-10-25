from typing import Dict, List

# A dictionary where the keys are strings and the values are ints

name_counts: Dict[str, int] = {
    "Adam": 10,
    "Guido": 12
}

# A list of integers

numbers: List[int] = [1, 2, 3, 4, 5, 6]

# A list that holds dicts that each hold a string key / int value

list_of_dicts: List[Dict[str, int]] = [
    {"key1": 1},
    {"key2": 2}
]

from typing import Tuple

my_data: Tuple[str, int, float] = ("Adam", 10, 5.7)

from typing import List, Tuple

LatLngVector = List[Tuple[float, float]]

points: LatLngVector = [
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477)
]
