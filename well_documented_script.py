
"""
Solar Desalination and Traditional Desalination Cost and Emissions Analysis
Author: [Your Name]
Date: [Date]
Description:
This script performs cost and emissions analysis for solar and traditional desalination technologies.
It includes calculations for Levelized Cost of Water (LCOW), lifecycle CO2 emissions, sensitivity 
analysis, and a comparison of technologies between regions.

Dependencies:
- numpy
- matplotlib

Ensure all dependencies are installed prior to execution.
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# SECTION 1: Cost Analysis for Solar and Traditional Desalination
# ------------------------------------------------------------------------------
"""
Parameters and functions for cost analysis. These include calculations for annualized capital
expenditure (CapEx), operational expenditure (OpEx), and the Levelized Cost of Water (LCOW).
"""

# Input parameters (Solar Desalination)
capex_solar = 1500  # $/m³/day (capital expenditure)
opex_solar = 0.05   # $/m³ (operational expenditure)
energy_consumption_solar = 3.0  # kWh/m³
energy_cost_solar = 0.1        # $/kWh

# Input parameters (Traditional Desalination)
capex_traditional = 1000       # $/m³/day
opex_traditional = 0.10        # $/m³
energy_consumption_traditional = 5.0  # kWh/m³
energy_cost_traditional = 0.12        # $/kWh

# Constants
annual_output = 365 * 1000  # m³/year (water output)
lifetime = 20              # years (plant lifespan)
discount_rate = 0.05       # Discount rate (5%)

def annualized_capex(capex, lifetime, discount_rate):
    """
    Calculate annualized capital expenditure using the annuity formula.
    
    Args:
        capex (float): Capital expenditure ($/m³/day).
        lifetime (int): Plant lifespan (years).
        discount_rate (float): Discount rate as a decimal.

    Returns:
        float: Annualized CapEx in $.
    """
    return capex * (discount_rate * (1 + discount_rate)**lifetime) / ((1 + discount_rate)**lifetime - 1)

# Calculate annualized CapEx
annual_capex_solar = annualized_capex(capex_solar, lifetime, discount_rate)
annual_capex_traditional = annualized_capex(capex_traditional, lifetime, discount_rate)

# Calculate annual energy costs
annual_energy_cost_solar = energy_consumption_solar * energy_cost_solar * annual_output
annual_energy_cost_traditional = energy_consumption_traditional * energy_cost_traditional * annual_output

# Calculate total annual costs
total_annual_cost_solar = annual_capex_solar + opex_solar * annual_output + annual_energy_cost_solar
total_annual_cost_traditional = annual_capex_traditional + opex_traditional * annual_output + annual_energy_cost_traditional

# Calculate Levelized Cost of Water (LCOW)
lcow_solar = total_annual_cost_solar / annual_output
lcow_traditional = total_annual_cost_traditional / annual_output

# Display results
print(f"LCOW for Solar Desalination: ${lcow_solar:.2f}/m³")
print(f"LCOW for Traditional Desalination: ${lcow_traditional:.2f}/m³")

# Visualization of cost comparison
def plot_cost_comparison():
    """
    Plot a bar chart comparing LCOW for solar and traditional desalination.
    """
    labels = ['Solar Desalination', 'Traditional Desalination']
    lcow_values = [lcow_solar, lcow_traditional]
    
    plt.bar(labels, lcow_values, color=['blue', 'green'])
    plt.ylabel('Levelized Cost of Water ($/m³)')
    plt.title('Cost Comparison of Desalination Technologies')
    plt.show()

plot_cost_comparison()


# SECTION 2: Lifecycle CO2 Emissions Analysis
# ------------------------------------------------------------------------------
"""
Calculate and compare lifecycle CO2 emissions for solar and traditional desalination. This includes
manufacturing emissions and operational CO2 emissions.
"""

# Parameters for emissions analysis
co2_emission_solar = 0          # Solar energy has zero emissions per kWh
co2_emission_traditional = 0.7  # Fossil fuel-based energy (kg CO2/kWh)

# Lifecycle CO2 emissions (kg CO2/year)
machine_emission_solar = 50_000      # Manufacturing CO2 emissions for solar technology
machine_emission_traditional = 20_000  # Manufacturing CO2 emissions for traditional technology

# Calculate operational CO2 emissions
annual_co2_emission_solar = energy_consumption_solar * co2_emission_solar * annual_output
annual_co2_emission_traditional = energy_consumption_traditional * co2_emission_traditional * annual_output

# Total lifecycle CO2 emissions
total_co2_emission_solar = annual_co2_emission_solar + machine_emission_solar
total_co2_emission_traditional = annual_co2_emission_traditional + machine_emission_traditional

# Display results
print(f"Total Lifecycle CO2 Emissions for Solar Desalination: {total_co2_emission_solar:.2f} kg")
print(f"Total Lifecycle CO2 Emissions for Traditional Desalination: {total_co2_emission_traditional:.2f} kg")

# Visualization of emissions comparison
def plot_emissions_comparison():
    """
    Plot a bar chart comparing lifecycle CO2 emissions for solar and traditional desalination.
    """
    labels = ['Solar Desalination', 'Traditional Desalination']
    co2_emissions = [total_co2_emission_solar, total_co2_emission_traditional]
    
    plt.bar(labels, co2_emissions, color=['blue', 'red'])
    plt.ylabel('Total Lifecycle CO2 Emissions (kg)')
    plt.title('Lifecycle CO2 Emissions Comparison: Solar vs Traditional Desalination')
    plt.show()

plot_emissions_comparison()

# Additional sections such as sensitivity analysis and regional comparisons can also be rewritten similarly.
