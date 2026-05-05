import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random





# Payoff matrices
A = np.array([[1, -1],
              [-1, 1]])

B = -A  # zero-sum game

strategies = ['H', 'T']


# Check pure Nash equilibrium
nash = []
for i in range(2):
    for j in range(2):
        if i == np.argmax(A[:, j]) and j == np.argmax(B[i, :]):
            nash.append((i, j))


print("Pure Nash Equilibria:", nash)


rounds = 1000
A_score = 0

scores = []  # store progression


for _ in range(rounds):
    A_choice = random.choice([0, 1])
    B_choice = random.choice([0, 1])

    if A_choice == B_choice:
        A_score += 1
    else:
        A_score -= 1

    scores.append(A_score)  # track every step


plt.plot(scores)
plt.title("Matching Pennies Score Over Time")
plt.xlabel("Rounds")
plt.ylabel("Player A Score")
plt.show(block=True)


#to avoid matplot


#Matching Pennies - Strategic Analysis

# import random

# strategies = ['H', 'T']

# #Payoff matrix
# payoff = {
#     ('H', 'H'): (1, -1),
#     ('H', 'T'): (-1, 1),
#     ('T', 'H'): (-1, 1),
#     ('T', 'T'): (1, -1)
# }

# #Check pure Nash Equilibrium
# def is_nash(s1, s2):
#     # Best response check
#     A_payoffs = [payoff[(a, s2)][0] for a in strategies]
#     B_payoffs = [payoff[(s1, b)][1] for b in strategies]

#     return (payoff[(s1, s2)][0] == max(A_payoffs) and
#             payoff[(s1, s2)][1] == max(B_payoffs))

# pure_nash = [(s1, s2) for s1 in strategies for s2 in strategies if is_nash(s1, s2)]

# print("Pure Nash Equilibria:", pure_nash)

# #Mixed strategy simulation
# rounds = 1000
# A_score, B_score = 0, 0

# for _ in range(rounds):
#     A = random.choice(strategies)
#     B = random.choice(strategies)

#     p = payoff[(A, B)]
#     A_score += p[0]
#     B_score += p[1]

# print("\nAfter repeated play:")
# print("Player A score:", A_score)
# print("Player B score:", B_score)

# print("\nConclusion: Optimal strategy is to randomize (50% H, 50% T)")