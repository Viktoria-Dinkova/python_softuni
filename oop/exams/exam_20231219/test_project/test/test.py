from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "Arm",
            100,
            200,
        )

        self.robot_with_software = ClimbingRobot(
            "Mountain",
            "Arm",
            100,
            200,
        )

        self.robot_with_software.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 51, "memory_consumption": 120},
            {"name": "CLion", "capacity_consumption": 49, "memory_consumption": 80}
        ]

    def test_correct_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Arm", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_is_not_valid_category_raise_valueerror(self):
        expected_result = f"Category should be one of {ClimbingRobot.ALLOWED_CATEGORIES}"

        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'some_category'

        self.assertEqual(expected_result, str(ve.exception))

    def test_get_used_capacity(self):
        used_capacity = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        self.assertEqual(used_capacity, self.robot_with_software.get_used_capacity())

    def test_get_available_capacity(self):
        used_capacity = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        available_capacity = self.robot_with_software.capacity - used_capacity

        self.assertEqual(available_capacity, self.robot_with_software.get_available_capacity())

    def test_get_used_memory(self):
        used_memory = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        self.assertEqual(used_memory, self.robot_with_software.get_used_memory())

    def test_get_available_memory(self):
        used_memory = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        available_memory = self.robot_with_software.memory - used_memory

        self.assertEqual(available_memory, self.robot_with_software.get_available_memory())

    def test_install_software_with_no_available_capacity(self):
        expected = "Software 'PyCharm' cannot be installed on Mountain part."
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 151, "memory_consumption": 120})

        self.assertEqual(expected, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_no_available_memory(self):
        expected = "Software 'PyCharm' cannot be installed on Mountain part."
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 220})

        self.assertEqual(expected, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_succsess(self):
        expected = "Software 'PyCharm' successfully installed on Mountain part."
        result = self.robot.install_software(
                  {"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200}
                 )

        self.assertEqual(expected, result)
        self.assertEqual([{"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200}], self.robot.installed_software)


if __name__ == "__main__":
    main()
