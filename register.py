
# coding: utf-8

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime
from chinese_calendar import is_workday, is_holiday

T = datetime.datetime.now()
april_last = datetime.date(T.year, T.month, T.day)

if(is_workday(april_last)):
	m = PyMouse()

	m.click(220,700,1)
	time.sleep(2)
	m.click(150,80,1)
	time.sleep(3)
	m.click(600,430,1)
	time.sleep(3)
	m.click(420,140,1)
	time.sleep(3)
	m.click(300,200,1)

