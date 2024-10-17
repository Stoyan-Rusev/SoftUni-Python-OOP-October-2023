from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_total_sold_books_property(self):
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_setter_unsuccessfully_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_books_limit_setter_unsuccessfully_value_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid", str(ve.exception))

    def test_books_limit_setter_successfully(self):
        self.assertEqual(10, self.store.books_limit)
        self.store.books_limit = 9
        self.assertEqual(9, self.store.books_limit)

    def test_len_when_dict_not_empty(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 3,
                                                           'Lord of the rings': 10}
        self.assertEqual(13, len(self.store))

    def test_len_when_dict_empty(self):
        self.assertEqual(0, len(self.store))

    def test_receive_book_unsuccessful_due_to_capacity_limit_when_dict_empty(self):
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Narnia', 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_unsuccessful_due_to_capacity_limit_when_dict_not_empty(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 9}
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Narnia', 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({'Narnia': 9}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_successful_when_dict_empty(self):
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        result = self.store.receive_book('Narnia', 5)
        self.assertEqual("5 copies of Narnia are available in the bookstore.", result)
        self.assertEqual({'Narnia': 5}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_successful_when_dict_not_empty_and_have_current_book(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5}
        result = self.store.receive_book('Narnia', 5)
        self.assertEqual("10 copies of Narnia are available in the bookstore.", result)
        self.assertEqual({'Narnia': 10}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_successful_when_dict_not_empty_and_doesnt_have_current_book(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5}
        result = self.store.receive_book('Star Wars', 5)
        self.assertEqual("5 copies of Star Wars are available in the bookstore.", result)
        self.assertEqual({'Narnia': 5, 'Star Wars': 5}, self.store.availability_in_store_by_book_titles)

    def test_sell_book_unsuccessful_due_to_book_not_available(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('WoTR', 1)

        self.assertEqual("Book WoTR doesn't exist!", str(ex.exception))
        self.assertEqual({'Narnia': 5}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_sell_book_unsuccessful_due_to_not_enough_amount(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Narnia', 6)

        self.assertEqual(f"Narnia has not enough copies to sell. Left: 5", str(ex.exception))
        self.assertEqual({'Narnia': 5}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_sell_book_successful(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5}

        result = self.store.sell_book('Narnia', 2)

        self.assertEqual("Sold 2 copies of Narnia", result)
        self.assertEqual({'Narnia': 3}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, self.store.total_sold_books)

    def test_str_when_zero_sold_books(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5, 'Star Wars': 6}

        self.assertEqual("Total sold books: 0\nCurrent availability: 11\n - Narnia: 5 copies\n - Star Wars: 6 copies",
                         str(self.store))

    def test_str_when_more_than_zero_sold_books(self):
        self.store.availability_in_store_by_book_titles = {'Narnia': 5, 'Star Wars': 6}
        self.store.sell_book('Narnia', 4)

        self.assertEqual("Total sold books: 4\nCurrent availability: 7\n - Narnia: 1 copies\n - Star Wars: 6 copies",
                         str(self.store))
        self.assertEqual({'Narnia': 1, 'Star Wars': 6}, self.store.availability_in_store_by_book_titles)

    def test_str_when_empty_dict(self):
        self.assertEqual("Total sold books: 0\nCurrent availability: 0",
                         str(self.store))


if __name__ == '__main__':
    main()
