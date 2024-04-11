"""
Create a class called Integer. Upon initialization, it should receive a single parameter value (int). It should have 3 additional methods:
•	from_float(float_value) - creates a new instance by flooring the provided floating number. If the value is not a float, return the message "value is not a float"
•	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
•	from_string(value) - creates a new instance by converting the string to an integer (if the value cannot be converted, return a message "wrong type")
"""
from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> int or str:
        if isinstance(float_value, float):
            return cls(floor(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_string(cls, value: str) -> int or str:
        if isinstance(value, str):
            try:
                return cls(int(value))
            except ValueError:
                pass
        return "wrong type"
    @classmethod
    def from_roman(cls, value: str):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(value)):
            if i > 0 and roman_dict[value[i]] > roman_dict[value[i - 1]]:
                result += roman_dict[value[i]] - 2 * roman_dict[value[i - 1]]
            else:
                result += roman_dict[value[i]]

        return cls(result)


# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
