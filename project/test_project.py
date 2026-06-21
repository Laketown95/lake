import unittest
from project import suggest_by_height, suggest_by_smell, suggest_by_color

class TestFlowerSuggestion(unittest.TestCase):
    def test_suggest_by_height(self):
        self.assertEqual(suggest_by_height('tall'), 'Sunflower')
        self.assertEqual(suggest_by_height('meidum'), 'Rose')
        self.assertEqual(suggest_by_height('short'), 'Daisy')
        self.assertEqual(suggest_by_height('unknown'), 'Unknown height preference')

    def test_suggest_by_smell(self):
        self.assertEqual(suggest_by_smell('strong'), 'Jasmine')
        self.assertEqual(suggest_by_smell('mild'), 'Lavender')
        self.assertEqual(suggest_by_smell('none'), 'Cactus')
        self.assertEqual(suggest_by_smell('unknown'), 'Unknown smell preference')

    def test_suggest_by_color(self):
        self.assertEqual(suggest_by_color('red'), 'Rose')
        self.assertEqual(suggest_by_color('yellow'), 'Sunflower')
        self.assertEqual(suggest_by_color('white'), 'Lily')
        self.assertEqual(suggest_by_color('unknown'), 'Unknown color preference')



if __name__ == "__main__":
    unittest.main
