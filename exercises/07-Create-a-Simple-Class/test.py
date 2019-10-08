import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app
import os
import re



@pytest.mark.it('1. The console should print the correct output')
def test_for_file_output(capsys):

    captured = buffer.getvalue()

    assert captured == str(1)+"\n"+str(3)+"\n"+str(1)+"\n" #add \n because the console jumps the line on every print
