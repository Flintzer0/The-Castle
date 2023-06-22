import sys, time

def text_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(speed)