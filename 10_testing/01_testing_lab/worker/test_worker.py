from unittest import TestCase, main
from worker_code import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker('TestGuy', 10_000, 100)

    def test_correct_initialization(self):
        self.assertEqual('TestGuy', self.worker.name)
        self.assertEqual(10_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_have_energy(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_doesnt_have_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increment_energy_with_one_when_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()
