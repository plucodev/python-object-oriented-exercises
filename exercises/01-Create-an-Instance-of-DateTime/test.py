import io
import sys
sys.stdout = buffer = io.StringIO()
# from app import current_date
import pytest
import app

import datetime

@pytest.mark.it('Your code needs to print the current date on the console with this format: Today is: MM-DD-YYYY')
def test_for_file_output(capsys):

    captured = buffer.getvalue()
    today_date = datetime.datetime.today()
    assert captured == "Today is: "+ today_date.strftime('%m-%d-%Y')+"\n" #add \n because the console jumps the line on every print

