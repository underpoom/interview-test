import unittest

def Solution(A =[], K = 0 ):
 
    if ( all(isinstance(x, (int)) for x in A) and (len(A) in range(0,101)) and  ( min(A)>= -1000 and max(A)<= 1000) and (K in range (0,101)) ):
        
        K = K % len(A)
        A.reverse()
        new_list = A
        new_list[:K] = reversed(new_list[:K])
        new_list[K:] = reversed(new_list[K:])
        return new_list
    
    else :
        return "out of range"

class TestStringMethods(unittest.TestCase):

    def test_rotation_1(self):
        actual = Solution([3, 8, 9, 7, 6],3)
        expect = [9, 7, 6, 3, 8]
        self.assertEqual(actual, expect)

    def test_rotation_2(self):
        actual = Solution([0, 0, 0],1)
        expect = [0, 0, 0]
        self.assertEqual(actual, expect)

    def test_rotation_3(self):
        actual = Solution([1, 2, 3, 4],4)
        expect = [1, 2, 3, 4]
        self.assertEqual(actual, expect)

    def test_rotation_4(self):
        actual = Solution([1, 2, 3, 4],100)
        expect = [1, 2, 3, 4]
        self.assertEqual(actual, expect)

    def test_rotation_5(self):
        actual = Solution([1, 2, 3, 4],0)
        expect = [1, 2, 3, 4]
        self.assertEqual(actual, expect)
    
if __name__ == '__main__':
    unittest.main()