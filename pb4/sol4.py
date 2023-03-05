import unittest

def Solution(n):

    if n in range(1,2_147_483_647):
        def to_bi(x):
            return bin(x)[2:]

        bit_str = to_bi(n)

        if bit_str.count('1') <= 1:
            return 0

        max_gap = 0

        prev_idex = None

        for current_idex, digit in enumerate(bit_str):
            if digit == '1':
                if prev_idex is not None:
                    max_gap = max(max_gap, current_idex - prev_idex - 1)
                prev_idex = current_idex

        return max_gap
    else:
        return "out of range"

class TestStringMethods(unittest.TestCase):

    def test_binary_gap_1(self):
        actual = Solution(9)
        expect = 2
        self.assertEqual(actual, expect)

    def test_binary_gap_2(self):
        actual = Solution(529)
        expect = 4
        self.assertEqual(actual, expect)

    def test_binary_gap_3(self):
        actual = Solution(20)
        expect = 1
        self.assertEqual(actual, expect)

    def test_binary_gap_4(self):
        actual = Solution(15)
        expect = 0
        self.assertEqual(actual, expect)

    def test_binary_gap_5(self):
        actual = Solution(32)
        expect = 0
        self.assertEqual(actual, expect)

    def test_binary_gap_6(self):
        actual = Solution(1041)
        expect = 5
        self.assertEqual(actual, expect)
    
if __name__ == '__main__':
    unittest.main()
