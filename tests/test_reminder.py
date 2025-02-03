from lib.reminder import *


def test_remind_user_to_do_tasks():
    reminder = Reminder("John")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "John! Walk the dog!"
