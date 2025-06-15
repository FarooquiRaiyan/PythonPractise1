import pynput
from pynput.keyboard import Key, Listener
keys=[]
def on_press(key):
    keys.append(key)
    print("pressed{0}" .format(key)) 
    if key == Key.esc:
        print("Esc typed exiting")
        # Stop listener
        return False

def on_release(key):
    print("released{0}".format(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()