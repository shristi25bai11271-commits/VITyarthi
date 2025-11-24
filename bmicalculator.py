import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

def calculate_bmi_value(weight_kg, height_m):
    try:
        if weight_kg <= 0 or height_m <= 0:
            return None
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except:
        return None

def get_bmi_status(bmi):
    """Determines the BMI category and associated color."""
    if bmi is None:
        return "Invalid Input", "black"
        
    if bmi < 18.5:
        return "Underweight⚠️", "#3498db"  
    elif 18.5 <= bmi < 25:
        return "Healthy Weight✨", "#2ecc71" 
    elif 25 <= bmi < 30:
        return "Overweight🍩", "#f39c12"  
    else: 
        return "Obesity🍰⚠️", "#e74c3c"    



def calculate_bmi_gui():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive values.")
            result_label.config(text="") 
            status_label.config(text="")
            return

        bmi_value = calculate_bmi_value(weight, height)
        status, color = get_bmi_status(bmi_value)
    
        result_label.config(text=f"Your BMI is: {bmi_value:.2f}", fg="#2c3e50") 
        status_label.config(text=f"Status: {status}", fg=color)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
        result_label.config(text="") 
        status_label.config(text="")


root = tk.Tk()
root.title("Modern BMI Calculator")
root.geometry("350x300")
root.configure(bg="#f6cee6") 
root.resizable(False, False) 

input_frame = tk.Frame(root, bg="#fcf5ff")
input_frame.pack(pady=20, padx=20)

# 1. Weight Input (Row 0)
tk.Label(input_frame, text="Weight (kg):", bg="#f5dbed", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', padx=5, pady=5)
weight_entry = tk.Entry(input_frame, width=15, font=('Arial', 10))
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# 2. Height Input (Row 1)
tk.Label(input_frame, text="Height (m):", bg="#f5dbed", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', padx=5, pady=5)
height_entry = tk.Entry(input_frame, width=15, font=('Arial', 10))
height_entry.grid(row=1, column=1, padx=5, pady=5)

# 3. Calculation Button (Row 2)
calculate_button = ttk.Button(input_frame, text="Calculate BMI", command=calculate_bmi_gui)
calculate_button.grid(row=2, column=0, columnspan=2, pady=15, sticky='ew') 



input_frame = tk.Frame(root, bg="#fcf5ff")
input_frame = tk.Frame(root, bg="#fcf5ff")
input_frame = tk.Frame(root, bg="#fcf5ff")
result_label = tk.Label(root, text="", font=('Helvetica', 14, 'bold'), bg="#f6cee6")
result_label.pack(pady=5)

status_label = tk.Label(root, text="", font=('Helvetica', 14, 'bold'), bg="#f6cee6")
status_label.pack(pady=5)

root.mainloop()
