# main.py
from amateur_radio_calculations import *

def get_user_choice():
    print("Choose an amateur radio formula to calculate:")
    print("1. Ohm's Law")
    print("2. Wavelength to Frequency and Vice Versa")
    print("3. dB Calculations")
    print("4. Antenna Gain")
    print("5. SWR (Standing Wave Ratio)")
    choice = input("Enter the number of your choice (1-5): ")
    return choice

def main():
    choice = get_user_choice()

    if choice == '1':
        current = float(input("Enter current (A): "))
        resistance = float(input("Enter resistance (Ω): "))
        voltage = ohms_law_voltage(current, resistance)
        print(f"Voltage: {voltage} V")

    elif choice == '2':
        sub_choice = input("Convert Wavelength to Frequency (1) or Frequency to Wavelength (2): ")
        if sub_choice == '1':
            wavelength = float(input("Enter wavelength (m): "))
            frequency = wavelength_to_frequency(wavelength)
            print(f"Frequency: {frequency} Hz")
        elif sub_choice == '2':
            frequency = float(input("Enter frequency (Hz): "))
            wavelength = frequency_to_wavelength(frequency)
            print(f"Wavelength: {wavelength} m")
        else:
            print("Invalid choice.")

    elif choice == '3':
        sub_choice = input("Convert Power Ratio to dB (1) or Voltage Ratio to dB (2): ")
        if sub_choice == '1':
            power_ratio = float(input("Enter power ratio: "))
            power_db = power_ratio_to_db(power_ratio)
            print(f"Power in dB: {power_db} dB")
        elif sub_choice == '2':
            voltage_ratio = float(input("Enter voltage ratio: "))
            voltage_db = voltage_ratio_to_db(voltage_ratio)
            print(f"Voltage in dB: {voltage_db} dB")
        else:
            print("Invalid choice.")

    elif choice == '4':
        directivity = float(input("Enter antenna directivity: "))
        efficiency = float(input("Enter antenna efficiency: "))
        gain = antenna_gain(directivity, efficiency)
        print(f"Antenna Gain: {gain}")

    elif choice == '5':
        reflected_power = float(input("Enter reflected power (W): "))
        forward_power = float(input("Enter forward power (W): "))
        swr_value = swr(reflected_power, forward_power)
        print(f"SWR: {swr_value}")

    else:
        print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
