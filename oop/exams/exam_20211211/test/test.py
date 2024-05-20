from project.team import Team
from unittest import TestCase, main

class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('mine')

    def test_correct_init(self):
        self.assertEqual('mine', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_raise_valueerror_if_name_is_not_only_letters(self):
        expected = "Team Name can contain only letters!"
        with self.assertRaises(ValueError) as ve:
            self.team.name = '123'

        self.assertEqual(expected, str(ve.exception))

    def test_raise_valueerror_if_is_not_name(self):
        expected = "Team Name can contain only letters!"
        with self.assertRaises(ValueError) as ve:
            self.team.name = ''

        self.assertEqual(expected, str(ve.exception))

    def test_add_member_correct(self):
        expected = f"Successfully added: gosho, tosho"
        result = self.team.add_member(gosho=15, tosho=17)
        self.assertEqual(expected, result)

    def test_remove_member_if_not_exist(self):
        expected = f"Member with name gosho does not exist"
        self.assertEqual(expected, self.team.remove_member('gosho'))

    def test_remove_member_with_success(self):
        expected = f"Member gosho removed"
        self.team.add_member(gosho=15)
        self.assertTrue('gosho' in self.team.members)
        self.assertEqual(expected, self.team.remove_member('gosho'))
        self.assertFalse('gosho' in self.team.members)

    def test_gt(self):
        self.team.add_member(gosho=15, tosho=17)
        other = Team('num')
        other.add_member(pesho=17)

        self.assertTrue(self.team > other)
        self.assertFalse(other > self.team)

    def test_len(self):
        self.team.add_member(gosho=15, tosho=17)

        self.assertTrue(2, len(self.team))

    




if __name__ == '__main__':
    main()