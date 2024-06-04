from enum import Enum
from typing import Generator
from matrix.matrix2Dim import Matrix2Dim
last_positions = []
invalid_positions = []
class NoPathFoundException(Exception):
    def __init__(self, message: str):
        self.message = message

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

def read_alien_file_to_matrix(file_name) -> Matrix2Dim:
    with open(file_name, 'r') as file:
        lines: list[str] = file.readlines()
    return Matrix2Dim(
        (len(lines), len(lines[0].split())),
        [[int(element) if element.isnumeric() else 1 for element in line.split()] for line in lines]
    )

def get_coordinates(matrix: Matrix2Dim) -> tuple[tuple[int,int], tuple[int,int]]:
    coords = []
    pos = 0
    for i in range(matrix.dimensions[0]):
        for j in range(matrix.dimensions[1]):
            if pos == 2:
                break
            val = matrix.elements[i][j]
            if val == 1:
                coords.append((i,j))
            continue
    return tuple(coords)

def shares_common_divisor(a: int, b: int) -> bool:
    if a == 1 or b == 1:
        return True
    try:
        divisor = next(i for i in get_divisors(a) if i in list(get_divisors(b)))
        return True
    except StopIteration:
        pass
    return False

def get_divisors(value: int) -> Generator[int, None, None]:
    return (i for i in range(2, value + 1) if value % i == 0)


def decide_direction(matrix: Matrix2Dim, current_pos, end_pos) -> Generator[Direction, None, None]:
    def is_closer(x, y) -> tuple[int,int]:
        close_x, close_y = abs(end_x - (current_x + x)), abs(end_y - (current_y + y))
        return close_x, close_y
    current_x, current_y = current_pos
    end_x, end_y = end_pos

    possible_directions = list(Direction)
    possible_directions.sort(key=lambda x: is_closer(*x.value))
    for dir in possible_directions:
        yield dir
    

def get_next_position(matrix: Matrix2Dim, current_pos, end_pos) -> tuple[int,int]:
    
    for direction in decide_direction(matrix, current_pos, end_pos):
        x, y = current_pos
        if not (
            x + direction.value[0] >= 0
            and x + direction.value[0] < matrix.dimensions[0]
            and y + direction.value[1] >= 0
            and y + direction.value[1] < matrix.dimensions[1]
            ):
            continue
        new_x, new_y = x + direction.value[0], y + direction.value[1]
        if (new_x, new_y) in invalid_positions or (len(last_positions) > 1 and (new_x, new_y) == last_positions[-2]):
            continue
        if shares_common_divisor(matrix.elements[x][y], matrix.elements[new_x][new_y]):
            return new_x, new_y
    raise NoPathFoundException("No path found")
    

if __name__ == "__main__":
    m = read_alien_file_to_matrix("alien.txt")
    print(m)
    start_pos, end_pos = get_coordinates(m)
    last_positions.append(start_pos)
    while last_positions[-1] != end_pos:
        current_pos = last_positions[-1]
        try:
            next_pos = get_next_position(m, current_pos, end_pos)
            last_positions.append(next_pos)
        except NoPathFoundException as e:
            invalid_positions.append(last_positions.pop())
            pass
    value = lambda x, y: m.elements[x][y].__str__()
    print(f"A valid path would be:\n{' -> '.join([value(i, j)for i, j in last_positions])}")
    