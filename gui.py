import tkinter as tk

# Place the GUI elements in the main window.
def placeElements(root):
    # Application Label.
    name = tk.Label(root, text="Creature Creator")
    name.pack(side="top", anchor="w", padx=5, pady=5)

    # Create the first frame for the first creature.
    creatureOneFrame = tk.Frame(root)
    creatureOneFrame.pack(side="top", anchor="w", padx=30, pady=10)
    # Populate the first frame with a label and an entry.
    label1 = tk.Label(creatureOneFrame, text="Creature 1:")
    label1.pack(padx=5, pady=5)
    entry1 = tk.Entry(creatureOneFrame)
    entry1.pack(pady=3)

    # Create the second frame for the second creature.
    creatureTwoFrame = tk.Frame(root)
    creatureTwoFrame.pack(side="top", anchor="w", padx=30, pady=5)
    # Populate the second frame with a label and an entry.
    label2 = tk.Label(creatureTwoFrame, text="Creature 2:")
    label2.pack(padx=5, pady=5)
    entry2 = tk.Entry(creatureTwoFrame)
    entry2.pack(pady=3)

    # Create an empty "go" button.
    goButton = tk.Button(creatureTwoFrame, text="Go!", width=10, command=lambda: print("Button clicked!"))
    goButton.pack(side="top", padx=10, pady=20)


# Call and create the main window
def startGui():
    root = tk.Tk()
    root.title("Creature Creator")
    root.geometry("600x250")

    placeElements(root)

    root.mainloop()
