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
    my_print = [s for s in content if "class Person:" in s]
    my_printVar = content.index(my_print[0])
    regex = r"class Person:"
    assert re.match(regex, content[my_printVar])
