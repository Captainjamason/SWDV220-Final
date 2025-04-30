import tkinter as tk

# Place the GUI elements in the main window.
def placeElements(root):
    # Application Label.
    name = tk.Label(root, text="Creature Creator")
    name.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=3)

    # Create the first frame for the first creature.
    creatureOneFrame = tk.Frame(root)
    creatureOneFrame.grid(row=1, column=0, sticky="w", padx=10, pady=15)
    # Populate the first frame with a label and an entry.
    label1 = tk.Label(creatureOneFrame, text="Creature 1:")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(creatureOneFrame)
    entry1.grid(row=0, column=1)

    # Create the second frame for the second creature.
    creatureTwoFrame = tk.Frame(root)
    creatureTwoFrame.grid(row=2, column=0, sticky="w", padx=10)
    # Populate the second frame with a label and an entry.
    label2 = tk.Label(creatureTwoFrame, text="Creature 2:")
    label2.grid(row=0, column=0)
    entry2 = tk.Entry(creatureTwoFrame)
    entry2.grid(row=0, column=1)

    # Create an empty "go" button.
    goButton = tk.Button(root, text="Go!", width=25, height=4, command=lambda: print("Button clicked!"))
    goButton.grid(row=3, column=0, pady=15, padx=30)

    # Create an empty square frame with a gray background.
    outputFrame = tk.Frame(root, bg="grey", width=250, height=200)
    outputFrame.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=25)
    outputFrame.grid_propagate(False)  # Prevent the frame from resizing to fit its contents.


def startGui():
    root = tk.Tk()
    root.title("Creature Creator")
    root.geometry("600x250")

    placeElements(root)

    root.mainloop()
