import sys


class TelephoneKeypad:
    phonenumber = ""

    def press(self, key: str):
        self.phonenumber += key

    def backspace(self):
        self.phonenumber = self.phonenumber[:-1]
    
    def clear(self):
        self.phonenumber = ""
    
    def dial(self):
        if len(self.phonenumber) >= 10:
            print(f"\tDialing {self.phonenumber}")

    def handle_keypressed(self, key: str):
        match key:
            case "d":
                self.dial()
            case "b":
                self.backspace()
            case "c":
                self.clear()
            case "q":
                sys.stdout.write("\033c")
                sys.exit()
            case other:
                if not other.isdigit():
                    return
                self.press(other)
        

if __name__ == "__main__":
    sys.stdout.write("\033c")
    telephoneKeypad = TelephoneKeypad()
    key = ""
    while True:
        sys.stdout.write("\033c")
        telephoneKeypad.handle_keypressed(key)
        print(f"Current pressed phonenumber: {telephoneKeypad.phonenumber}")
        key = input("Press a key: ")
    