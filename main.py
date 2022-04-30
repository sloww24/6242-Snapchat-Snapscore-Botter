try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time
   from datetime import datetime
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """
        ░█████╗░██████╗░░░██╗██╗██████╗░
        ██╔═══╝░╚════██╗░██╔╝██║╚════██╗
        ██████╗░░░███╔═╝██╔╝░██║░░███╔═╝
        ██╔══██╗██╔══╝░░███████║██╔══╝░░
        ╚█████╔╝███████╗╚════██║███████╗
        ░╚════╝░╚══════╝░░░░░╚═╝╚══════╝"""
class snapchat:

    def __init__(self):
        self.sent_snaps = 0

    def get_positions(self):
        self.print_console("Move your mouse to the camera button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the take picture button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the arrow down button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.arrow_down = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Multi Snaps button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.multi_snap = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Edit & Send button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.edit_send = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Send To button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to your shortcut, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to select all in shortcut, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.select_all = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to send snap button, then press E.")
        while True:
            if keyboard.is_pressed("E"):
                self.send_snap_button = pyautogui.position()
                break
    
    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)
        pyautogui.moveTo(self.switch_to_camera)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(self.take_picture)
        for i in range(7):
            pyautogui.click()
            time.sleep(0.3)
        pyautogui.moveTo(self.edit_send)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        self.sent_snaps += 7
        self.update_title(shortcut_users)
    
    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        ctypes.windll.kernel32.SetConsoleTitleW(f"Snapchat Score Botter | Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by slowwwwwww.w#6242")

    def print_console(self, arg):
        print(f"\n       {Fore.WHITE}[{Fore.BLUE}Console{Fore.WHITE}] {arg}")
    
    def main(self):
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score Botter | Developed by slowwwwwww.w#6242")
        print(Fore.BLUE + ascii_text)
        self.get_positions()
        shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.BLUE}Console{Fore.WHITE}] How many people are in this shortcut: "))
        self.print_console("Go to your chats, then press E when you're ready.")
        while True:
            if keyboard.is_pressed("E"):
                break
        os.system("cls")
        print(Fore.BLUE + ascii_text)
        self.print_console("Sending snaps...")
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("F4"):
                break
            self.send_snap(shortcut_users)
            time.sleep(4)
        self.print_console("Finished sending {self.sent_snaps} snaps.")

obj = snapchat()
obj.main()
