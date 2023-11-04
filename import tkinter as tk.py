import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display.get()
    new_text = current_text + value
    display.set(new_text)

# Function to evaluate the expression and update the display
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.set(result)
    except Exception as e:
        display.set("Error")
        print(e)

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create a text variable to store and update the display
display = tk.StringVar()

# Entry widget to display the current input and result
entry = tk.Entry(app, textvariable=display, justify='right', font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Function to handle button clicks
def button_click(value):
    if value == 'C':
        display.set("")
    elif value == '=':
        calculate()
    else:
        update_display(value)

# Create and place the calculator buttons
row, col = 1, 0
for button in buttons:
    tk.Button(app, text=button, width=6, height=2, command=lambda v=button: button_click(v)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI main loop
app.mainloop()
