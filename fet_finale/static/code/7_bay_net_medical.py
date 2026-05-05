P_Fever = [0.5, 0.5]   # 0=No, 1=Yes
P_Cough = [0.6, 0.4]   # 0=No, 1=Yes

P_Disease = [
    [0.9, 0.7, 0.6, 0.2],  # No Disease
    [0.1, 0.3, 0.4, 0.8]   # Disease
]

def predict_disease(fever, cough):
    index = fever * 2 + cough
    return {
        "No Disease": P_Disease[0][index],
        "Disease": P_Disease[1][index]
    }

result = predict_disease(1, 1)

print("P(Disease | Fever=Yes, Cough=Yes):")
print(result)

#another

#First, Bayesian Network calculates probability of COVID for a person with symptoms.
#Then we scale it to a group by multiplying with number of people having those symptoms.


# from pgmpy.models import DiscreteBayesianNetwork
# from pgmpy.inference import VariableElimination
# from pgmpy.factors.discrete import TabularCPD

# # Step 1: Model
# model = DiscreteBayesianNetwork([('COVID', 'Fever'), ('COVID', 'Cough')])

# cpd_covid = TabularCPD('COVID', 2, [[0.1], [0.9]])

# cpd_fever = TabularCPD('Fever', 2,
#                        [[0.85, 0.2],
#                         [0.15, 0.8]],
#                        evidence=['COVID'],
#                        evidence_card=[2])

# cpd_cough = TabularCPD('Cough', 2,
#                        [[0.8, 0.3],
#                         [0.2, 0.7]],
#                        evidence=['COVID'],
#                        evidence_card=[2])

# model.add_cpds(cpd_covid, cpd_fever, cpd_cough)

# infer = VariableElimination(model)

# # -------- USER INPUT --------
# total_people = int(input("Enter total number of people: "))
# fever_prob = float(input("Enter probability of Fever (0-1): "))
# cough_prob = float(input("Enter probability of Cough (0-1): "))

# # Step 2: Convert probability → number of people
# fever_people = int(total_people * fever_prob)
# cough_people = int(total_people * cough_prob)

# # Estimate overlap (people having both symptoms)
# both_symptoms = min(fever_people, cough_people)

# # Step 3: Bayesian inference (for one person with both symptoms)
# result = infer.query(
#     variables=['COVID'],
#     evidence={'Fever': 0, 'Cough': 0}   # Yes, Yes
# )

# covid_prob = result.values[0]

# # Step 4: Final estimation
# estimated_infected = both_symptoms * covid_prob

# # -------- OUTPUT --------
# print("\n--- Results ---")
# print("People with Fever:", fever_people)
# print("People with Cough:", cough_people)
# print("People with both symptoms:", both_symptoms)
# print("P(COVID | symptoms):", round(covid_prob, 3))
# print("Estimated infected people:", round(estimated_infected))