# main_gui.py
import tkinter as tk
from tkinter import ttk
from amateur_radio_calculations import *

def calculate():
    choice = formula_var.get()

    if choice == 'Ohm':
        current = float(current_entry.get())
        resistance = float(resistance_entry.get())
        voltage = ohms_law_voltage(current, resistance)
        result_label.config(text=f"Voltage: {voltage} V")

    elif choice == 'Wavelength':
        sub_choice = wavelength_var.get()
        if sub_choice == 'to_frequency':
            wavelength = float(wavelength_entry.get())
            frequency = wavelength_to_frequency(wavelength)
            result_label.config(text=f"Frequency: {frequency} Hz")
        elif sub_choice == 'to_wavelength':
            frequency = float(frequency_entry.get())
            wavelength = frequency_to_wavelength(frequency)
            result_label.config(text=f"Wavelength: {wavelength} m")

    elif choice == 'dB':
        sub_choice = db_var.get()
        if sub_choice == 'power_ratio':
            power_ratio = float(power_ratio_entry.get())
            power_db = power_ratio_to_db(power_ratio)
            result_label.config(text=f"Power in dB: {power_db} dB")
        elif sub_choice == 'voltage_ratio':
            voltage_ratio = float(voltage_ratio_entry.get())
            voltage_db = voltage_ratio_to_db(voltage_ratio)
            result_label.config(text=f"Voltage in dB: {voltage_db} dB")

    elif choice == 'Antenna Gain':
        directivity = float(directivity_entry.get())
        efficiency = float(efficiency_entry.get())
        gain = antenna_gain(directivity, efficiency)
        result_label.config(text=f"Antenna Gain: {gain}")

    elif choice == 'SWR':
        reflected_power = float(reflected_power_entry.get())
        forward_power = float(forward_power_entry.get())
        swr_value = swr(reflected_power, forward_power)
        result_label.config(text=f"SWR: {swr_value}")

def on_formula_change(*args):
    choice = formula_var.get()
    if choice == 'Ohm':
        formula_frame.grid()
        wavelength_frame.grid_remove()
        db_frame.grid_remove()
        antenna_frame.grid_remove()
        swr_frame.grid_remove()
    elif choice == 'Wavelength':
        formula_frame.grid_remove()
        wavelength_frame.grid()
        db_frame.grid_remove()
        antenna_frame.grid_remove()
        swr_frame.grid_remove()
    elif choice == 'dB':
        formula_frame.grid_remove()
        wavelength_frame.grid_remove()
        db_frame.grid()
        antenna_frame.grid_remove()
        swr_frame.grid_remove()
    elif choice == 'Antenna Gain':
        formula_frame.grid_remove()
        wavelength_frame.grid_remove()
        db_frame.grid_remove()
        antenna_frame.grid()
        swr_frame.grid_remove()
    elif choice == 'SWR':
        formula_frame.grid_remove()
        wavelength_frame.grid_remove()
        db_frame.grid_remove()
        antenna_frame.grid_remove()
        swr_frame.grid()

# Create the main window
root = tk.Tk()
root.title("Amateur Radio Calculations")

# Create a notebook to organize formula pages
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Ohm's Law page
formula_page = ttk.Frame(notebook)
formula_frame = ttk.LabelFrame(formula_page, text="Ohm's Law")
formula_frame.grid(row=0, column=0, padx=10, pady=10)

formula_var = tk.StringVar()
formula_var.set('Ohm')

formula_var.trace('w', on_formula_change)

formula_label = ttk.Label(formula_frame, text="Select a formula:")
formula_label.grid(row=0, column=0, padx=5, pady=5)

formula_menu = ttk.Combobox(formula_frame, textvariable=formula_var, values=('Ohm', 'Wavelength', 'dB', 'Antenna Gain', 'SWR'))
formula_menu.grid(row=0, column=1, padx=5, pady=5)

current_label = ttk.Label(formula_frame, text="Current (A):")
current_label.grid(row=1, column=0, padx=5, pady=5)
current_entry = ttk.Entry(formula_frame)
current_entry.grid(row=1, column=1, padx=5, pady=5)

resistance_label = ttk.Label(formula_frame, text="Resistance (Ω):")
resistance_label.grid(row=2, column=0, padx=5, pady=5)
resistance_entry = ttk.Entry(formula_frame)
resistance_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(formula_frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(formula_frame, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Wavelength and Frequency page
wavelength_page = ttk.Frame(notebook)
wavelength_frame = ttk.LabelFrame(wavelength_page, text="Wavelength and Frequency")
wavelength_frame.grid(row=0, column=0, padx=10, pady=10)

wavelength_var = tk.StringVar()
wavelength_var.set('to_frequency')

wavelength_label = ttk.Label(wavelength_frame, text="Select a conversion:")
wavelength_label.grid(row=0, column=0, padx=5, pady=5)

wavelength_menu = ttk.Combobox(wavelength_frame, textvariable=wavelength_var, values=('to_frequency', 'to_wavelength'))
wavelength_menu.grid(row=0, column=1, padx=5, pady=5)

wavelength_entry = ttk.Entry(wavelength_frame)
wavelength_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

frequency_entry = ttk.Entry(wavelength_frame)
frequency_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

calculate_button_wl = ttk.Button(wavelength_frame, text="Calculate", command=calculate)
calculate_button_wl.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# dB Calculations page
db_page = ttk.Frame(notebook)
db_frame = ttk.LabelFrame(db_page, text="dB Calculations")
db_frame.grid(row=0, column=0, padx=10, pady=10)

db_var = tk.StringVar()
db_var.set('power_ratio')

db_var.trace('w', on_formula_change)

db_label = ttk.Label(db_frame, text="Select a conversion:")
db_label.grid(row=0, column=0, padx=5, pady=5)

db_menu = ttk.Combobox(db_frame, textvariable=db_var, values=('power_ratio', 'voltage_ratio'))
db_menu.grid(row=0, column=1, padx=5, pady=5)

power_ratio_label = ttk.Label(db_frame, text="Power Ratio:")
power_ratio_label.grid(row=1, column=0, padx=5, pady=5)
power_ratio_entry = ttk.Entry(db_frame)
power_ratio_entry.grid(row=1, column=1, padx=5, pady=5)

voltage_ratio_label = ttk.Label(db_frame, text="Voltage Ratio:")
voltage_ratio_label.grid(row=2, column=0, padx=5, pady=5)
voltage_ratio_entry = ttk.Entry(db_frame)
voltage_ratio_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button_db = ttk.Button(db_frame, text="Calculate", command=calculate)
calculate_button_db.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Antenna Gain page
antenna_page = ttk.Frame(notebook)
antenna_frame = ttk.LabelFrame(antenna_page, text="Antenna Gain")
antenna_frame.grid(row=0, column=0, padx=10, pady=10)

directivity_label = ttk.Label(antenna_frame, text="Directivity:")
directivity_label.grid(row=0, column=0, padx=5, pady=5)
directivity_entry = ttk.Entry(antenna_frame)
directivity_entry.grid(row=0, column=1, padx=5, pady=5)

efficiency_label = ttk.Label(antenna_frame, text="Efficiency:")
efficiency_label.grid(row=1, column=0, padx=5, pady=5)
efficiency_entry = ttk.Entry(antenna_frame)
efficiency_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button_antenna = ttk.Button(antenna_frame, text="Calculate", command=calculate)
calculate_button_antenna.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# SWR page
swr_page = ttk.Frame(notebook)
swr_frame = ttk.LabelFrame(swr_page, text="SWR")
swr_frame.grid(row=0, column=0, padx=10, pady=10)

reflected_power_label = ttk.Label(swr_frame, text="Reflected Power (W):")
reflected_power_label.grid(row=0, column=0, padx=5, pady=5)
reflected_power_entry = ttk.Entry(swr_frame)
reflected_power_entry.grid(row=0, column=1, padx=5, pady=5)

forward_power_label = ttk.Label(swr_frame, text="Forward Power (W):")
forward_power_label.grid(row=1, column=0, padx=5, pady=5)
forward_power_entry = ttk.Entry(swr_frame)
forward_power_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button_swr = ttk.Button(swr_frame, text="Calculate", command=calculate)
calculate_button_swr.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Add pages to the notebook
notebook.add(formula_page, text='Ohm\'s Law')
notebook.add(wavelength_page, text='Wavelength and Frequency')
notebook.add(db_page, text='dB Calculations')
notebook.add(antenna_page, text='Antenna Gain')
notebook.add(swr_page, text='SWR')

notebook.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

if __name__ == "__main__":
    root.mainloop()
