# amateur_radio_calculations.py
import math

speed_of_light = 299792458  # m/s

def ohms_law_voltage(current, resistance):
    return current * resistance

def ohms_law_current(voltage, resistance):
    return voltage / resistance

def ohms_law_resistance(voltage, current):
    return voltage / current

def wavelength_to_frequency(wavelength):
    return speed_of_light / wavelength

def frequency_to_wavelength(frequency):
    return speed_of_light / frequency

def power_ratio_to_db(power_ratio):
    return 10 * math.log10(power_ratio)

def voltage_ratio_to_db(voltage_ratio):
    return 20 * math.log10(voltage_ratio)

def antenna_gain(directivity, efficiency):
    return directivity * efficiency

def swr(reflected_power, forward_power):
    return (1 + math.sqrt(reflected_power / forward_power)) / (1 - math.sqrt(reflected_power / forward_power))
