from name_function import get_formatted_name
from name_function import get_formatted_name_with_middle
from name_function import get_formatted_name_with_optional_middle


# successful test
def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


# failed test
def test_first_middle_last_name():
    formatted_name = get_formatted_name_with_middle('michael', 'fox')
    assert formatted_name == 'Michael J. Fox'


# successful test
def test_first_optional_middle_last_name_1():
    formatted_name = get_formatted_name_with_optional_middle('david', 'heyworth')
    assert formatted_name == 'David Heyworth'


def test_first_optional_middle_last_name_2():
    formatted_name = get_formatted_name_with_optional_middle('david', 'heyworth', 'jude')
    assert formatted_name == 'David Jude Heyworth'
