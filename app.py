from tkinter import Label, Tk
import time

# Create the main window
root = Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.resizable(False, False)
root.configure(bg="black")

# Function to update the time
def update_clock():
    current_time = time.strftime("%H:%M:%S %p")  # 24-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every 1 second

# Create a label to display the time
label = Label(root, font=("Arial", 40, "bold"), bg="black", fg="cyan")
label.pack(pady=20)

# Start the clock
update_clock()
root.mainloop()
