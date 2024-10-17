from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.int_list = IntegerList("A", 3.5, False, 1, 2, 3)

    def test_init_and_get_data_expect_only_int_list(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_correct_type_expect_list_with_new_item(self):
        expected_data = self.int_list.get_data() + [4]
        self.int_list.add(4)
        self.assertEqual(expected_data, self.int_list.get_data())

    def test_add_incorrect_type_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add(4.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_when_index_in_range_expect_remove_and_return_item(self):
        i = 1
        expected_removed_item = self.int_list.get_data()[i]
        expected_new_list = [1, 3]

        self.assertEqual(expected_removed_item, self.int_list.remove_index(i))
        self.assertEqual(expected_new_list, self.int_list.get_data())

    def test_remove_index_when_index_out_of_range_expect_index_error(self):
        i = 10

        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(i)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_by_index_when_correct_index_expect_returned_item(self):
        index = 2
        expected_item = self.int_list.get_data()[index]

        self.assertEqual(expected_item, self.int_list.get(index))

    def test_get_when_index_out_of_range_expect_index_error(self):
        index = 10

        with self.assertRaises(IndexError) as ie:
            self.int_list.get(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_when_correct_index_and_correct_el_type_expect_inserted_el(self):
        index = 2
        el = 4
        expected_list = [1, 2, 4, 3]

        self.int_list.insert(index, el)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_insert_when_incorrect_index_expect_index_error(self):
        index = 10

        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(index, 2)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_when_incorrect_value_type_expect_value_error(self):
        el = 3.4

        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, el)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_expect_biggest_num(self):
        expected_el = 3

        self.assertEqual(expected_el, self.int_list.get_biggest())

    def test_get_index_expect_index_of_given_el(self):
        expected_index = 0

        self.assertEqual(expected_index, self.int_list.get_index(1))


if __name__ == '__main__':
    main()
