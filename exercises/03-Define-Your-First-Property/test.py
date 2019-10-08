import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re




@pytest.mark.it('1. You should just define a class Person!')
def test_forLuckyNumber(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_def = [s for s in content if "def __init__" in s]
    my_defVar = content.index(my_def[0])
    my_class = [s for s in content if "class Person:" in s]
    my_classVar = content.index(my_class[0])
    my_name = [s for s in content if "self.name" in s]
    my_nameVar = content.index(my_name[0])
    my_last = [s for s in content if "self.last" in s]
    my_lastVar = content.index(my_last[0])
    my_age = [s for s in content if "self.birth" in s]
    my_ageVar = content.index(my_age[0])
    regex_def = r"def __init__(\s*)\(self\)(\s*):"
    regex_class = r"class Person:"
    regex_name = r"self\.name(\s*)=(\s*)\"Bob\""
    regex_last = r"self\.last_name(\s*)=(\s*)\"Dylan\""
    regex_age = r"self\.birth_date(\s*)=(\s*)\"May 24, 1941\""
    assert re.match(regex_class, content[my_classVar])
    assert re.match(regex_def, content[my_defVar])
    assert re.match(regex_name, content[my_nameVar])
    assert re.match(regex_last, content[my_lastVar])
    assert re.match(regex_age, content[my_ageVar])
