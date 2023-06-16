import tkinter as tk


def show_text():
    text = entry.get()
    print(f"wprowadzony tekst {text}")


app = tk.Tk()
app.title("Pole wprowadzania")
entry = tk.Entry(app)

entry.pack()

button = tk.Button(app, text="Pokaż tekst", command=show_text)
button.pack(side=tk.BOTTOM)

app.mainloop()
