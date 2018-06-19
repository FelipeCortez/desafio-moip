import unittest
from stats import parse_file

class TestParse(unittest.TestCase):

    def test_well_formed(self):
        parse_contents = parse_file("testes/well-formed.txt")
        print(parse_contents)

        with open("testes/well-formed.expected", "rb") as expected:
            expected_contents = expected.read().decode("utf-8")
            print(expected_contents)
            self.assertEqual(parse_contents, expected_contents)

    def test_malformed(self):
        with self.assertRaises(ValueError):
            parse_file("testes/malformed.txt")

if __name__ == '__main__':
    unittest.main()
