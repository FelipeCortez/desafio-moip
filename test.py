import unittest
from stats import parse_file

def load_file(filename: str):
    with open(filename, "rb") as expected:
        return expected.read().decode("utf-8")

class TestParse(unittest.TestCase):

    def test_well_formed(self):
        parse_contents = parse_file("testes/well-formed.txt")
        expected_contents = load_file("testes/well-formed.expected")
        self.assertEqual(parse_contents, expected_contents)

    def test_well_formed_4(self):
        parse_contents = parse_file("testes/well-formed.txt", site_count=4)
        expected_contents = load_file("testes/well-formed-4.expected")
        self.assertEqual(parse_contents, expected_contents)

    def test_mixed(self):
        parse_contents = parse_file("testes/mixedcase.txt")
        expected_contents = load_file("testes/mixedcase.expected")
        self.assertEqual(parse_contents, expected_contents)

    def test_malformed(self):
        with self.assertRaises(ValueError):
            parse_file("testes/malformed.txt")

if __name__ == '__main__':
    unittest.main()
