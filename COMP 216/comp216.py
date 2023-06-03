import tkinter as tk

def create_grid(root):
    # Create label
    label = tk.Label(root, text="Welcome")
    label.grid(row=0, column=1)

    # Create buttons
    button_texts = [
        "Button 1", "Button 2", "Button 3",
        "Button 4", "Button 5", "Button 6",
        "Button 7", "Button 8", "Button 9"
    ]
    buttons = []
    for i, text in enumerate(button_texts):
        button = tk.Button(root, text=text)
        button.grid(row=(i // 3) + 1, column=i % 3)

root = tk.Tk()

# Create the grid
create_grid(root)

# Start the main event loop
root.mainloop()