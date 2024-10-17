from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_a = Student('A')
        self.student_b = Student('B',
                                 {'Python': ['a', 'b'],
                                  'JS': ['c']})

    def test_init_without_courses(self):
        self.assertEqual('A', self.student_a.name)
        self.assertEqual({}, self.student_a.courses)

    def test_init_with_courses(self):
        self.assertEqual('B', self.student_b.name)
        self.assertEqual({'Python': ['a', 'b'], 'JS': ['c']},
                         self.student_b.courses)

    def test_enroll_when_course_name_in_dict(self):
        result = self.student_b.enroll('Python', ['c', 'd'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['a', 'b', 'c', 'd'], self.student_b.courses['Python'])

    def test_enroll_when_add_course_notes_is_y(self):
        result = self.student_a.enroll('Python', ['test'], 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['test'], self.student_a.courses['Python'])

    def test_enroll_when_add_course_notes_is_empty(self):
        result = self.student_a.enroll('Python', ['test'], '')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['test'], self.student_a.courses['Python'])

    def test_enroll_when_course_not_in_dict_and_add_notes_not_y_or_empty(self):
        result = self.student_a.enroll('Python', ['.py'], 'A')

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_a.courses['Python'])

    def test_add_notes_when_course_found(self):
        result = self.student_b.add_notes('Python', '.py')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['a', 'b', '.py'], self.student_b.courses['Python'])

    def test_add_notes_when_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student_a.add_notes('Python', '.py')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_found(self):
        result = self.student_b.leave_course('Python')

        self.assertEqual("Course has been removed", result)
        self.assertEqual({ 'JS': ['c']}, self.student_b.courses)

    def test_leave_course_when_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student_b.leave_course('Some course')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
