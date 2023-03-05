import unittest

def Solution(N):
       
        map = {
            1: "I",
            4: "IV",
            5: "V",   
            9: "IX",
            10: "X",  
            40: "XL",
            50: "L",  
            90: "XC",
            100: "C",  
            400: "CD",
            500: "D",  
            900: "CM",
            1000: "M", 
        }
        
        result = ''

        table = [e for e in map.keys()]
        table.reverse()
   
        for n in table:
            while n <= N:
                result += map[n]
                N-=n
        return result


class TestStringMethods(unittest.TestCase):

    def test_integer_to_roman_1(self):
        actual = Solution(3)
        expect = "III"
        self.assertEqual(actual, expect)

    def test_integer_to_roman_2(self):
        actual = Solution(58)
        expect = "LVIII"
        self.assertEqual(actual, expect)

    def test_integer_to_roman_3(self):
        actual = Solution(1994)
        expect = "MCMXCIV"
        self.assertEqual(actual, expect)
    
if __name__ == '__main__':
    unittest.main()
