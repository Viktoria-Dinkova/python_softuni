
from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer('Gosho', 25, 100)

    def test_correct_init(self):
        self.assertEqual("Gosho", self.tennis_player.name)
        self.assertEqual(25, self.tennis_player.age)
        self.assertEqual(100, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_short_name_raise_valueerror(self):
        expect = "Name should be more than 2 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('G1', 25, 100)

        self.assertEqual(expect, str(ve.exception))

    def test_age_child_rise_valueerror(self):
        expect = "Players must be at least 18 years of age!"

        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Gosho', 15, 100)

        self.assertEqual(expect, str(ve.exception))

    def test_add_new_win_same_tournament_return_mess(self):
        expect = "sameTournament has been already added to the list of wins!"
        self.tennis_player.add_new_win("sameTournament")

        self.assertEqual(expect, self.tennis_player.add_new_win("sameTournament"))
        self.assertEqual(["sameTournament"], self.tennis_player.wins)

    def test_add_new_win_different_tournament(self):
        self.tennis_player.add_new_win("sameTournament")
        self.tennis_player.add_new_win("otherTournament")

        self.assertEqual(["sameTournament", "otherTournament"], self.tennis_player.wins)

    def test_less_then_other_by_point_if_true(self):
        self.other_player = TennisPlayer("pesho", 24, 150)
        expected = 'pesho is a top seeded player and he/she is better than Gosho'

        result = self.tennis_player < self.other_player
        self.assertEqual(expected, result)

    def test_less_then_other_by_point_if_not_true(self):
        self.other_player = TennisPlayer("pesho", 24, 90)
        expected = 'Gosho is a better player than pesho'

        result = self.tennis_player < self.other_player
        self.assertEqual(expected, result)

    def test_str(self):
        expected = "Tennis Player: Gosho\nAge: 25\nPoints: 100.0\nTournaments won: "

        self.assertEqual(expected, self.tennis_player.__str__())



if __name__ == "__main__":
    main()
