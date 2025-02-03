import pytest
from lib.reminder import *


def test_remind_user_to_do_tasks():
    reminder = Reminder("John")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "John! Walk the dog!"


def test_no_task_set():
    reminder = Reminder("John")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"
