import time

def focus_timer(duration):
    print(f"Focus timer started for {duration} minutes.")
    duration_sec = duration * 60
    time.sleep(duration_sec)
    print("Focus timer ended!")

focus_duration = int(input("30："))
focus_timer(focus_duration)
