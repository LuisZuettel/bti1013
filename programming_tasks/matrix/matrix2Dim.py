class NonNumericValues(Exception):
    pass

class Matrix2Dim:
    """
    Two-dimensional matrix based on a list of lists of items and a tuple that defines the dimensions
    of the matrix (number of rows and number of columns).
    """

    def __init__(self, dimensions: tuple[int, int], elements=None) -> None:
        """ Constructor
        :param dimensions: tuple (pair) of the size of both the dimensions.
        (first item of dimensions corresponds to the rows, second item to the columns)
        Important: the dimensions must be greater or equal to 1.
        :param elements: content of the matrix (list of lists of elements).
        """
        if elements is None:
            elements = []
        self.dimensions = dimensions
        self.elements = elements

    def initialize(self, value: float) -> None:
        """
        Initialize the content of the matrix with given value.
        :param value: value assigned to all the elements of matrix.
        """
        self.elements = []
        xs = [value] * self.dimensions[1]
        for i in range(self.dimensions[0]):
            self.elements.append(xs.copy())

    def __str__(self):
        """
        Defines the way that class instance should be displayed. The __str__ method is called when
        the following functions are invoked on the object and return a string: print() and str().
        Without this function print() displays a class instance as an object and not as a human-readable way.
        :return: the human-readable string of a class instance (object).
        """
        output = "(" + str(self.dimensions[0]) + ", " + str(self.dimensions[1]) + ")" + "\n"
        for line in self.elements:
            for element in line:
                output += "|" + str(element) + "|"
            output += "\n"
        return output

    def transpose(self):
        """
        Performs the matrix transposition based on swapping row and column.
        :return: the transposed matrix.
        """
        return Matrix2Dim((self.dimensions[1], self.dimensions[0]),[[self.elements[j][i] for j in range(len(self.elements))] for i in range(len(self.elements[0]))])

    def is_symmetric(self) -> bool:
        """
        Determine if a matrix is symmetric or not.
        :return: true if the matrix is symmetric, false otherwise.
        """
        return self.dimensions[0] == self.dimensions[1] and self.elements == self.transpose().elements

    def total(self) -> float:
        """
        :return: the sum of all the elements of the matrix.
        """
        try:
            return sum([sum(line) for line in self.elements])
        except TypeError:
            raise NonNumericValues("Matrix elements must be numeric") 
    
    def size(self) -> int:
        """
        :return: the number of elements in the matrix.
        """
        return self.dimensions[0] * self.dimensions[1]

    def average(self) -> float:
        """
        :return: the average of the elements of the matrix.
        """
        return self.total() / self.size()

    def stddeviation(self) -> float:
        """
        :return: the standard deviation of all the elements of the matrix.
        """
        mean = self.average()
        return (sum([sum([(element - mean) ** 2 for element in line]) for line in self.elements]) / self.size()) ** 0.5

    def is_coherent(self):
        """
        Determine if the matrix is coherent.  A matrix is coherent if and only if all the lines (sub-lists) of
        elements have the same number of elements which is the number of lines in the dimension tuple and the
        number of sub-lists of elements is the same as the number of columns in the dimension tuple.
        :return: true if the matrix is coherent, false otherwise.
        """
        if len(self.elements) != self.dimensions[0]:
            return False
        for line in self.elements:
            if len(line) != self.dimensions[1]:
                return False
        return True

def main():
    matrix = Matrix2Dim((2, 3), [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
    print(matrix)
    matrix2 = Matrix2Dim((3, 3))
    matrix2.initialize(0.0)
    print(matrix2)


if __name__ == "__main__":
    main()

