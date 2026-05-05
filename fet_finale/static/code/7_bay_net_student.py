P_Study = [0.6, 0.4]       # 0=Low, 1=High
P_Attendance = [0.7, 0.3]  # 0=Poor, 1=Good

P_Performance = [
    [0.9, 0.6, 0.5, 0.1],  # Fail
    [0.1, 0.4, 0.5, 0.9]   # Pass
]

def predict_performance(study, attendance):
    index = study * 2 + attendance
    return {
        "Fail": P_Performance[0][index],
        "Pass": P_Performance[1][index]
    }

result = predict_performance(1, 1)

print("P(Performance | Study=High, Attendance=Good):")
print(result)


#another
# from pgmpy.models import DiscreteBayesianNetwork
# from pgmpy.inference import VariableElimination
# from pgmpy.factors.discrete import TabularCPD

# # Step 1: Define structure
# model = DiscreteBayesianNetwork([
#     ('Study', 'Pass'),
#     ('Attendance', 'Pass'),
#     ('Difficulty', 'Pass')
# ])

# # Step 2: Define CPTs

# # Study: High(0), Low(1)
# cpd_study = TabularCPD('Study', 2, [[0.6], [0.4]])

# # Attendance: Good(0), Poor(1)
# cpd_attendance = TabularCPD('Attendance', 2, [[0.7], [0.3]])

# # Difficulty: Easy(0), Hard(1)
# cpd_difficulty = TabularCPD('Difficulty', 2, [[0.5], [0.5]])

# # Pass depends on Study, Attendance, Difficulty
# cpd_pass = TabularCPD(
#     'Pass', 2,
#     [
#         # Pass = Yes
#         [0.95, 0.85, 0.80, 0.60, 0.75, 0.50, 0.40, 0.20],
#         # Pass = No
#         [0.05, 0.15, 0.20, 0.40, 0.25, 0.50, 0.60, 0.80]
#     ],
#     evidence=['Study', 'Attendance', 'Difficulty'],
#     evidence_card=[2, 2, 2]
# )

# # Step 3: Add to model
# model.add_cpds(cpd_study, cpd_attendance, cpd_difficulty, cpd_pass)

# # Step 4: Inference
# infer = VariableElimination(model)

# o=int(input("enter study(0/1)high/low : "))
# p=int(input("enter attendace(0/1)good/poor : "))
# q=int(input("enter difficulty(0/1)easy/hard : "))

# # Example: High study, Good attendance, Easy exam
# result = infer.query(
#     variables=['Pass'],
#     evidence={'Study': o, 'Attendance': p, 'Difficulty': q}
# )

# print(result)