P_Battery = [0.7, 0.3]  # 0=Good, 1=Bad
P_Fuel = [0.8, 0.2]     # 0=Yes, 1=No

P_Start = [
    [0.95, 0.6, 0.4, 0.1],  # Starts
    [0.05, 0.4, 0.6, 0.9]   # Doesn't Start
]

def predict_start(battery, fuel):
    index = battery * 2 + fuel
    return {
        "Starts": P_Start[0][index],
        "Doesn't Start": P_Start[1][index]
    }

result = predict_start(0, 0)

print("P(CarStarts | Battery=Good, Fuel=Yes):")
print(result)



#another
# from pgmpy.models import DiscreteBayesianNetwork
# from pgmpy.inference import VariableElimination
# from pgmpy.factors.discrete import TabularCPD

# model = DiscreteBayesianNetwork([('Battery', 'Start'), ('Fuel', 'Start')])

# cpd_battery = TabularCPD('Battery', 2, [[0.7], [0.3]])  # Good, Bad
# cpd_fuel = TabularCPD('Fuel', 2, [[0.8], [0.2]])  # Yes, No

# cpd_start = TabularCPD('Start', 2,
#                        [[0.95, 0.6, 0.5, 0.1],   # Start = Yes
#                         [0.05, 0.4, 0.5, 0.9]],  # Start = No
#                        evidence=['Battery', 'Fuel'],
#                        evidence_card=[2, 2])

# model.add_cpds(cpd_battery, cpd_fuel, cpd_start)

# infer = VariableElimination(model)
# result = infer.query(variables=['Start'], evidence={'Battery': 0, 'Fuel':0})

# print(result)