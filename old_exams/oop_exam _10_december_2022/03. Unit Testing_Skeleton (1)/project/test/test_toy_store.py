from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_unsuccessful_due_to_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('H', 'car')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_unsuccessful_due_to_toy_already_in_shelf(self):
        self.store.toy_shelf['A'] = 'car'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'car')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_unsuccessful_due_to_shelf_already_taken(self):
        self.store.toy_shelf['A'] = 'car'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'lego')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

        result = self.store.add_toy("A", 'car')

        self.assertEqual("Toy:car placed successfully!", result)
        self.assertEqual({
            "A": 'car',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_remove_toy_unsuccessfully_due_to_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('H', 'car')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_unsuccessfully_due_to_toy_doesnt_exist_in_shelf(self):
        self.store.toy_shelf['A'] = 'car'
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'lego')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.store.toy_shelf['A'] = 'car'
        result = self.store.remove_toy('A', 'car')
        self.assertEqual("Remove toy:car successfully!", result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)


if __name__ == '__main__':
    main()
