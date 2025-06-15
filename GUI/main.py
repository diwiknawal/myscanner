import tkinter as tk

root = tk.Tk()
root.title("The Grid Geometry Manager")
root.geometry("400x300")

tk.Button(root, text="Span 2 columns", height=5).grid(
    row=3,
    column=0,
    columnspan=2,
    sticky="ew",
)

tk.Button(root, text="Span 2 rows", width=10, height=10).grid(
    row=4,
    column=0,
    rowspan=2,
    sticky="ns",
)

root.mainloop()