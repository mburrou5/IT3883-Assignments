# Program Name: Assignment3.py
	# Course: IT3883
	# Student Name: Michael Burrough
	# Assignment Number: Lab1
	# Due Date: 10/10/ 2026
	# Purpose: Program will convert mpg to kmpl
	# Resources: https://github.com/Omarr-kh/miles_to_km_converter/blob/master/main.py
    #https://medium.com/@amaithichirasan.s/your-first-simple-python-gui-program-miles-to-kilometer-converter-using-tkinter-beginner-level-c8b94e758c2
    #https://www.youtube.com/watch?v=Ih-01sTq1A0
    
    
    
    
import tkinter as tk




#Function
def convert(*args):
    try:
        mpg = float(entry.get())

        kmpl = mpg * 0.425144
        result_label.config(text=f"{mpg} MPG = {kmpl:.2f} km/L")
    except ValueError:
        result_label.config(text="Please enter a valid number")

#Window
root = tk.Tk()
root.title("MPG to km/L Converter")
root.geometry("300x300")

label = tk.Label(root, text="Enter MPG:", font=("Arial", 11))
label.pack(pady=10)

entry_var = tk.StringVar()
entry_var.trace_add("write", convert)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 12), justify="center")
entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=15)
root.mainloop()
