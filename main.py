from PIL import ImageGrab
import pyautogui
import tkinter as tk
from tkinter import ttk
from threading import Thread


class Bot():
    def __init__(self, coordinates_rect: list, coordinates_bird: list):
        super().__init__()
        self.x1, self.y1, self.z1 = coordinates_rect
        self.x2, self.y2, self.z2 = coordinates_bird

    def start(self):
        img = ImageGrab.grab().convert('L')
        data = img.load()
        self.checKCollision(data)
            
    # Possible change, duplicate this loop and specify pixel behaviour (bird/rectangle)
    def checKCollision(self, data):
        for i in range(self.x1, self.y1):
            for j in range(self.y1, self.z1):
                print(data[i, j])
                if data[i, j] < 100:
                    self.click('down')
                    
                    return
        for i in range(self.x2, self.y2):
            for j in range(self.y2, self.z2):
                if data[i, j] < 170:
                    self.click('up')
                   
                    return
        return

    def stop(self):
        self.isOn = False

    def click(self, arg):
        pyautogui.press(arg)


class Aplication(tk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title('Bot dinosaur GUI')
        Coordinates_rect_cactus = [0, 40, 60] #Change these values
        Coordinates_rect_bird = [40, 60, 80]  #Change these values
        self.bot = Bot(Coordinates_rect_cactus, Coordinates_rect_bird)
        self.botOn = False

    def draw(self):
        self.mainframe = tk.Frame(main_window)
        self.titlelabel = ttk.Label(
            self.mainframe, text="Google Dino Bot", font=('castellar', 20))
        self.startBtn = ttk.Button(
            self.mainframe, text='Start Bot', command=lambda: self.checker(True))
        self.stopBtn = ttk.Button(
            self.mainframe, text='Stop bot', command=lambda: self.checker(False))
        self.startBarTest = ttk.Button(
            self.mainframe, text='Open progress bar', command=self.startProgressBar)
        self.step = tk.DoubleVar()
        self.progressbar = ttk.Progressbar(self.mainframe, orient='horizontal', variable=self.step)
        self.mainframe.pack(anchor='center', pady=10)
        self.titlelabel.pack(anchor='center', pady=10)
        self.startBtn.pack(anchor='center', pady=10)
        self.stopBtn.pack(anchor='center', pady=10)
        self.startBarTest.pack(anchor='center', pady=10)
        self.progressbar.pack(anchor='center', pady=10)
        self.botOn = False
        self.startBot()
              
    def startBot(self):   
        #play_thread = Thread(target=self.bot.start(), name="Updater", daemon=True)
        #play_thread.start()
        
        if self.botOn is True:
            self.bot.start()

        self.after(50, self.startBot)
    
    def checker(self, value):
        self.botOn = value  

    def startProgressBar(self):
        
        new_value = self.step.get()
        new_value += 10
        if new_value > 100:
            new_value = 0
        self.step.set(new_value)
        self.progressbar["value"] = new_value

        main_window.after(1000, self.startProgressBar)  # Update every 1000 milliseconds (1 second)
     
"""
        for i in range(self.x1, self.y1):
            for j in range(self.y1, self.z1):
                data[i, j] = 0

        for i in range(self.x2, self.y2):
            for j in range(self.y2, self.z2):
                data[i, j] = 150
"""

if __name__ == '__main__':
    main_window = tk.Tk()
    App = Aplication(main_window)
    App.draw()
    main_window.mainloop()
