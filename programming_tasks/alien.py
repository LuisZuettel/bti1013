from matrix.matrix2Dim import Matrix2Dim
last_positions = []
invalid_positions = []

class NoPathFoundException(Exception):
    def __init__(self, message: str):
        self.message = message

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

def is_prime_number(value: int) -> bool:
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def is_valid_pos(matrix: Matrix2Dim, x: int, y: int) -> bool:
    if (x, y) not in last_positions and (x, y) not in invalid_positions:
        return True

def get_next_position(matrix: Matrix2Dim, x: int, y: int) -> tuple[int,int]:
    
    # UP
    if x - 1 >= 0 and is_valid_pos(matrix, x-1,y) and not is_prime_number(matrix.elements[x-1][y]):
        return x-1, y
    # DOWN
    if x + 1 < matrix.dimensions[0] and is_valid_pos(matrix, x+1,y) and not is_prime_number(matrix.elements[x+1][y]):
        return x+1, y
    # LEFT
    if y - 1 >= 0 and is_valid_pos(matrix, x,y-1) and not is_prime_number(matrix.elements[x][y-1]):
        return x, y-1
    # RIGHT
    if y + 1 < matrix.dimensions[1] and is_valid_pos(matrix, x, y+1) and not is_prime_number(matrix.elements[x][y+1]):
        return x, y+1
    raise NoPathFoundException("No path found")
    

if __name__ == "__main__":
    m = read_alien_file_to_matrix("alien.txt")
    print(m)
    start_pos, end_pos = get_coordinates(m)
    last_positions.append(start_pos)
    while last_positions[-1] != end_pos:
        i, j = last_positions[-1]
        try:
            next_pos = get_next_position(m, i, j)
            last_positions.append(next_pos)
        except NoPathFoundException as e:
            invalid_positions.append(last_positions.pop())
    value = lambda x, y: m.elements[x][y].__str__()
    print(f"A valid path would be:\n{' -> '.join([value(i, j)for i, j in last_positions])}")
    