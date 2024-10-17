from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.cat = Mammal('Tom', 'cat', 'meow')

    def test_init(self):
        self.assertEqual('Tom', self.cat.name)
        self.assertEqual('cat', self.cat.type)
        self.assertEqual('meow', self.cat.sound)
        self.assertEqual('animals', self.cat.get_kingdom())

    def test_make_sound(self):
        self.assertEqual(f"Tom makes meow", self.cat.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.cat.get_kingdom())

    def test_info(self):
        self.assertEqual("Tom is of type cat", self.cat.info())


if __name__ == '__main__':
    main()
