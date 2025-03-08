import tkinter as tk
from tkinter import ttk, messagebox

def length_converter(value, from_unit, to_unit):
    length_units = {
        'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001,
        'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kg': 1, 'g': 0.001, 'mg': 0.000001, 'lb': 0.453592, 'oz': 0.0283495
    }
    kilograms = value * weight_units[from_unit]
    return kilograms / weight_units[to_unit]

def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()
        
        if category == "Length":
            result = length_converter(value, from_unit, to_unit)
        else:
            result = weight_converter(value, from_unit, to_unit)
        
        label_result.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

app = tk.Tk()
app.title("Unit Converter")
app.geometry("700x600")
app.configure(bg="#e3f2fd")

frame = tk.Frame(app, bg="#ffffff", padx=40, pady=40, relief=tk.GROOVE, borderwidth=5)
frame.pack(pady=40)

tk.Label(frame, text="Unit Converter", font=("Arial", 28, "bold"), bg="#ffffff", fg="#1565c0").grid(row=0, column=0, columnspan=2, pady=20)

combo_category = ttk.Combobox(frame, values=["Length", "Weight"], state="readonly", font=("Arial", 16))
combo_category.set("Length")
combo_category.grid(row=1, column=0, columnspan=2, pady=20)

entry_value = tk.Entry(frame, font=("Arial", 18), width=14, justify="center", relief=tk.SOLID, borderwidth=2)
entry_value.grid(row=2, column=0, pady=20)

tk.Label(frame, text="to", font=("Arial", 18), bg="#ffffff").grid(row=2, column=1, padx=20)

combo_from = ttk.Combobox(frame, state="readonly", font=("Arial", 16))
combo_from.grid(row=3, column=0, pady=20)

combo_to = ttk.Combobox(frame, state="readonly", font=("Arial", 16))
combo_to.grid(row=3, column=1, pady=20)

button_convert = tk.Button(frame, text="Convert", font=("Arial", 18, "bold"), bg="#1e88e5", fg="white", padx=20, pady=10, relief=tk.RAISED, borderwidth=3, command=convert)
button_convert.grid(row=4, column=0, columnspan=2, pady=30)

label_result = tk.Label(frame, text="Result: ", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1565c0")
label_result.grid(row=5, column=0, columnspan=2, pady=20)

def update_units(event):
    units = {
        "Length": ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in'],
        "Weight": ['kg', 'g', 'mg', 'lb', 'oz']
    }
    selected = combo_category.get()
    combo_from.config(values=units[selected])
    combo_to.config(values=units[selected])
    combo_from.set(units[selected][0])
    combo_to.set(units[selected][1])

combo_category.bind("<<ComboboxSelected>>", update_units)
update_units(None)

app.mainloop()
