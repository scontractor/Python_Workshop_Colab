import pandas as pd
import matplotlib as plt
import tkinter
from configparser import ConfigParser

new_batteries_acquisition_cost = pd.read_excel("D:/program_codes/battery_system_calculator/new_batteries.xlsx")
print(new_batteries_acquisition_cost)

used_batteries_acquisition_cost = pd.read_excel("D:/program_codes/battery_system_calculator/used_batteries.xlsx")
print(used_batteries_acquisition_cost)

container_cost = pd.read_excel("D:/program_codes/battery_system_calculator/container.xlsx")
print(container_cost)

cooling_cost = pd.read_excel("D:/program_codes/battery_system_calculator/cooling.xlsx")
print(cooling_cost)

acdc_converter_cost = pd.read_excel("D:/program_codes/battery_system_calculator/power_electronics.xlsx", 'summary_acdc')
print(acdc_converter_cost)

dcdc_converter_cost = pd.read_excel("D:/program_codes/battery_system_calculator/power_electronics.xlsx", 'summary_dcdc')
print(dcdc_converter_cost)

