import unittest

from matrix.matrix2Dim import Matrix2Dim, NonNumericValues


class Matrix2DimTest(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or variables for your tests
        self.m = Matrix2Dim((2, 3),[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])

    def tearDown(self):
        # Clean up any resources after running your tests
        self.m = None
        
    def test_is_coherent(self):
        # Write your test cases here
        self.assertTrue(self.m.is_coherent())
        self.assertFalse(Matrix2Dim((2, 2), self.m.elements).is_coherent())

    def test_total(self):
        self.assertEqual(self.m.total(), 15.0)
        self.assertRaises(NonNumericValues, Matrix2Dim((2, 2), [[0.0, 1.0], [1.0, 'a']]).total)

    def test_size(self):
        self.assertEqual(self.m.size(), 6)
    
    def test_average(self):
        self.assertEqual(self.m.average(), 2.5)
    
    def test_stddeviation(self):
        self.assertAlmostEqual(self.m.stddeviation(), 1.708, 3)

    def test_transpose(self):
        self.assertEqual(self.m.transpose().elements, Matrix2Dim((3, 2), [[0.0, 3.0], [1.0, 4.0], [2.0, 5.0]]).elements)

    def test_is_symmetric(self):
        self.assertFalse(self.m.is_symmetric())
        self.assertTrue(Matrix2Dim((2, 2), [[0.0, 1.0], [1.0, 0.0]]).is_symmetric())
        
if __name__ == '__main__':
    unittest.main()