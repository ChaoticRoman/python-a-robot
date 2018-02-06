import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Convert inches to centimeters")

        self.inputText = tk.Entry(self)
        self.inputText["justify"] = "right"
        self.inputText.pack(side="left")
        self.inputText.insert(0, '0')

        self.inchLabel = tk.Label(self)
        self.inchLabel["text"] = '"'
        self.inchLabel.pack(side="left")

        self.convertButton = tk.Button(self)
        self.convertButton["text"] = "Convert"
        self.convertButton["command"] = self.convert
        self.convertButton.pack(side="left")

        self.resultLabel = tk.Label(self)
        self.resultLabel["width"] = 10
        self.resultLabel.pack(side="left")

        self.quit = tk.Button(self, text="Quit", command=root.destroy)
        self.quit.pack(side="right")

        self.convert()

    def convert(self):
        input_val = float(self.inputText.get())
        self.resultLabel["text"] = str(input_val * 2.54) + ' cm'

root = tk.Tk()
app = Application(master=root)
app.mainloop()

