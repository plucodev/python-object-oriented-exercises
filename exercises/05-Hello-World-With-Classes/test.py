import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re


@pytest.mark.it('1. You should create a new object instance of the class Printer ')
def test_for_my_printer_instance(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "my_printer" in s]
    my_printVar = content.index(my_print[0])
    regex = r"my_printer(\s*)=(\s*)Printer\(\)"
    assert re.match(regex, content[my_printVar])
@pytest.mark.it('2. Call the function printer_test of the class Printer and store the result in a variable called test_result ')
def test_for_test_result_variable(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_print = [s for s in content if "test_result" in s]
    my_printVar = content.index(my_print[0])
    regex = r"test_result(\s*)=(\s*)my_printer\.printer_test\(\)"
    assert re.match(regex, content[my_printVar])
@pytest.mark.it('3. Print the test_result content ')
def test_for_test_result_print(capsys):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    content_length = len(content)
    print(content_length)
    my_print = [s for s in content if "print(test_result)" in s]
    print(my_print)
    my_printVar = content.index(my_print[0])
    regex = r"print(\s*)\((\s*)test_result(\s*)\)"
    assert re.match(regex, content[my_printVar])
