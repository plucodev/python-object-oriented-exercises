import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it('1. You should create a new function called get_model which returns the printer model')
def test_for_my_printer_instance(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "get_model" in s]
    my_printVar = content.index(my_print[0])
    regex = r"def get_model(\s*)\((\s*)self(\s*)\)(\s*):"
    assert re.match(regex, content[my_printVar])
    my_ret = [s for s in content if "return self" in s]
    my_retVar = content.index(my_ret[0])
    regex_ret = r"return self\.model"
    assert re.match(regex_ret, content[my_retVar])
@pytest.mark.it('2. The console should print the correct output')
def test_for_file_output(capsys):

    captured = buffer.getvalue()

    assert captured == "The model of the printer is : TX-200\n" #add \n because the console jumps the line on every print
