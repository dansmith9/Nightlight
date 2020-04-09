from blinkt import set_pixel, set_brightness, show, clear
import datetime
import time

while True:
	set_brightness(0.2)
	current_state = "off"
	t = datetime.datetime.now()
	print("Current time: ", t)
	if (t.hour >= 18 and current_state != "night") or t.hour < 6:
		current_state = "night"
		clear()
		set_all(255, 255, 0)
		show()
	elif t.hour > 5 and t.hour <= 9 and current_state != "morning":
		current_state = "morning"
		clear()
		set_all(0, 255, 0)
		show()
	else:
		current_state = "off"
		clear()
		show()
	time.sleep(600)
