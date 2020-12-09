from configparser import ConfigParser
import math
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import seaborn as sns
sns.set(style="white", color_codes=True)

import plotly.express as px
from matplotlib import *
from matplotlib.gridspec import GridSpec

config = ConfigParser()

config.read("C:/Users/contr/PycharmProjects/HelloWorld/bess_cost_calculator/simulation/config.ini")
print(config.sections())

# New Batteries

new_battery_chemistry = config['NEW_BATTERY']['new_battery_chemistry']
new_battery_installed_capacity = float(config['NEW_BATTERY']['new_battery_installed_capacity'])

if new_battery_chemistry == 'NMC':
    unit_cost_new_battery = 160
elif new_battery_chemistry == 'NCA':
    unit_cost_new_battery = 142
elif new_battery_chemistry == 'LFP':
    unit_cost_new_battery = 100
else:
    raise Exception('Please enter a valid cell chemistry')

total_cost_new_battery = unit_cost_new_battery * new_battery_installed_capacity
print('total cost of new batteries = ' + str(total_cost_new_battery) + ' EUR')

# Used Batteries

used_battery_chemistry = config['USED_BATTERY']['used_battery_chemistry']
used_battery_installed_capacity = float(config['USED_BATTERY']['used_battery_installed_capacity'])

if used_battery_chemistry == 'NMC':
    unit_cost_used_battery = 90
elif used_battery_chemistry == 'NCA':
    unit_cost_used_battery = 85
elif used_battery_chemistry == 'LFP':
    unit_cost_used_battery = 80
else:
    raise Exception('Please enter a valid cell chemistry')

total_cost_used_battery = unit_cost_used_battery * used_battery_installed_capacity
print('total cost of used batteries = ' + str(total_cost_used_battery) + ' EUR')

# Total Battery Cost

total_cost_combined_battery = total_cost_new_battery + total_cost_used_battery
print('total cost of new + used batteries = ' + str(total_cost_combined_battery) + ' EUR')

# Power Electronics

dcdc_power_rating = float(config['POWER_ELECTRONICS']['dcdc_power_rating'])
acdc_power_rating = float(config['POWER_ELECTRONICS']['acdc_power_rating'])

unit_cost_dcdc = round(159.97 * math.log(1000 * dcdc_power_rating) - 477.27, 2)

print('DCDC converter cost = ' + str(unit_cost_dcdc) + ' EUR')

unit_cost_acdc = round(1315.5 * math.log(acdc_power_rating) + 1368.3, 2)
print('ACDC converter cost = ' + str(unit_cost_acdc) + ' EUR')

# HVAC

thermal_power_rating = float(config['HVAC']['thermal_power_rating'])

unit_cost_hvac = round(320.64 * math.exp(0.1798 * thermal_power_rating), 2)
print('HVAC system cost = ' + str(unit_cost_hvac) + ' EUR')

# Container

container_type = config['CONTAINER']['container_type']
container_size = config['CONTAINER']['container_size']
container_condition = config['CONTAINER']['container_condition']

if container_size == '20ft' and container_type == 'Insulated' and container_condition == 'New':
    cost_container = 4200
elif container_size == '20ft' and container_type == 'Insulated' and container_condition == 'Used':
    cost_container = 1500
elif container_size == '20ft' and container_type == 'Reefer' and container_condition == 'New':
    cost_container = 13000
elif container_size == '20ft' and container_type == 'Reefer' and container_condition == 'Used':
    cost_container = 4700
elif container_size == '40ft' and container_type == 'Insulated' and container_condition == 'New':
    cost_container = 7000
elif container_size == '40ft' and container_type == 'Insulated' and container_condition == 'Used':
    cost_container = 2000
elif container_size == '40ft' and container_type == 'Reefer' and container_condition == 'New':
    cost_container = 18000
elif container_size == '40ft' and container_type == 'Reefer' and container_condition == 'Used':
    cost_container = 6000
else:
    raise Exception('Please enter a valid container format')

print('Container cost = ' + str(round(cost_container)) + ' EUR')

# Battery Management System

bms_voltage_rating = config['BATTERY_MANAGEMENT_SYSTEM']['bms_voltage_rating']
bms_current_rating = config['BATTERY_MANAGEMENT_SYSTEM']['bms_current_rating']

# print(bms_current_rating)
# print(bms_voltage_rating)

# Calculate bms costs here
cost_bms = 0

# Energy Management System

ems_placeholder_1 = config['ENERGY_MANAGEMENT_SYSTEM']['ems_placeholder_1']
ems_placeholder_2 = config['ENERGY_MANAGEMENT_SYSTEM']['ems_placeholder_2']

# print(ems_placeholder_1)
# print(ems_placeholder_2)

# Placeholder - Calculate ems costs here
cost_ems = 0

# Refurbishing Costs

cost_refurbishing = 0.25 * total_cost_combined_battery

print('Refurbishing costs = ' + str(cost_refurbishing))

# Calculating Overall BESS Costs

overall_cost_bess = total_cost_combined_battery + unit_cost_acdc + unit_cost_dcdc + unit_cost_hvac + cost_container + \
                    cost_bms + cost_ems + cost_refurbishing

unit_cost_bess = overall_cost_bess/(used_battery_installed_capacity + new_battery_installed_capacity)


print('Overall BESS costs = ' + str(overall_cost_bess) + ' EUR')
print('Costs of BESS per kWh =' + str(unit_cost_bess) + ' EUR/kWh')


# Systematically storing results

results = {'Battery Acquisition': total_cost_combined_battery,
           'DCDC Converter': unit_cost_dcdc,
           'ACDC Converter': unit_cost_acdc,
           'HVAC System': unit_cost_hvac,
           'Container': cost_container,
           'BMS': cost_bms,
           'EMS': cost_ems,
           'Refurbishing': cost_refurbishing
           }

df_results = pd.DataFrame(list(results.items()), columns=['Component', 'Cost'])
df_results = df_results.sort_values(by=['Cost'], ascending=False)

print(df_results)

df_components_cost = df_results['Cost']
df_components_labels = df_results['Component']
print(df_components_cost)
print(df_components_labels)

# Figure plotting using plotly

fig = make_subplots(rows=1, cols=2, subplot_titles=('BESS Cost Compostion', 'Estimated Costs by Component'),
                    specs=[[{"type": "pie"}, {"type": "bar"}]])
fig.add_trace(go.Bar(x=df_components_labels, y=df_components_cost,
                    hovertemplate="<b>%{label}</b><br><br>" +
                    "Component Cost: %{text} EUR<br>" + "<extra></extra>",
                    name='Estimated Costs by Component',
                    text=df_components_cost))
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.add_trace(go.Pie(hole=0.6,
                     values=df_components_cost, labels=df_components_labels,
                     marker={'colors': ['green', 'red', 'blue'],'line': {'color': 'white', 'width': 1}},
                     hovertemplate="%{label}</b><br>Costs share: %{percent} </br>",
                     name='Relative Costs BESS', domain=dict(x=[0, 0.5])))

fig['layout']['xaxis']['title'] = 'BESS component'
fig['layout']['yaxis']['title'] = 'Unit cost (EUR)'

fig.show()
print(df_results)




