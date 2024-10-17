from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Spiderman', 10, 100.0, 100.0)
        self.enemy = Hero('Venom', 10, 100.0, 100.0)

    def test_init(self):
        self.assertEqual('Spiderman', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(100.0, self.hero.damage)

    def test_battle_when_same_usernames_expect_exception(self):
        self.enemy.username = 'Spiderman'

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_zero(self):
        self.hero.health = 0
        expected_message = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_message, str(ve.exception))

    def test_battle_when_health_below_zero(self):
        self.hero.health = -1
        expected_message = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_message, str(ve.exception))

    def test_battle_when_enemy_health_zero(self):
        self.enemy.health = 0
        expected_message = "You cannot fight Venom. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_message, str(ve.exception))

    def test_battle_when_enemy_health_below_zero(self):
        self.enemy.health = -1
        expected_message = "You cannot fight Venom. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_message, str(ve.exception))

    def test_battle_when_draw(self):
        message = self.hero.battle(self.enemy)

        self.assertEqual("Draw", message)

    def test_battle_when_hero_wins(self):
        self.enemy.health = 10
        self.enemy.damage = 1

        message = self.hero.battle(self.enemy)

        self.assertEqual("You win", message)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_when_enemy_wins(self):
        self.hero.health = 10
        self.hero.damage = 1

        message = self.hero.battle(self.enemy)

        self.assertEqual("You lose", message)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str(self):
        expected_string = f"Hero Spiderman: 10 lvl\n" \
               f"Health: 100.0\n" \
               f"Damage: 100.0\n"

        self.assertEqual(expected_string, str(self.hero))


if __name__ == '__main__':
    main()
