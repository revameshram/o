import numpy as np
import matplotlib.pyplot as plt


# Payoff matrices
A = np.array([[3, 0],
              [5, 1]])

B = np.array([[3, 5],
              [0, 1]])

strategies = ['C', 'D']


# Find best responses
def best_response_A(j):
    return np.argmax(A[:, j])


def best_response_B(i):
    return np.argmax(B[i, :])


# Find Nash Equilibrium
nash = []
for i in range(2):
    for j in range(2):
        if i == best_response_A(j) and j == best_response_B(i):
            nash.append((i, j))


print("Nash Equilibrium:", [(strategies[i], strategies[j]) for i, j in nash])


fig, ax = plt.subplots()

matrix = np.array([[3, 0],
                   [5, 1]])

ax.imshow(matrix)

for i in range(2):
    for j in range(2):
        ax.text(j, i, f"A:{A[i,j]}\nB:{B[i,j]}", ha='center', va='center')


ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['C', 'D'])
ax.set_yticklabels(['C', 'D'])


plt.title("Prisoner's Dilemma Payoff Matrix")
plt.show()

#to avoid matplot


#Prisoner's Dilemma - Strategic Analysis

# import itertools

# #Strategies
# strategies = ['C', 'D']

# #Payoff matrix
# payoff = {
#     ('C', 'C'): (3, 3),
#     ('C', 'D'): (0, 5),
#     ('D', 'C'): (5, 0),
#     ('D', 'D'): (1, 1)
# }

# # Function to get best response
# def best_response(player, opponent_strategy):
#     best_payoff = -float('inf')
#     best_strategies = []

#     for s in strategies:
#         if player == 0:
#             p = payoff[(s, opponent_strategy)][0]
#         else:
#             p = payoff[(opponent_strategy, s)][1]

#         if p > best_payoff:
#             best_payoff = p
#             best_strategies = [s]
#         elif p == best_payoff:
#             best_strategies.append(s)

#     return best_strategies

# x=input("enter strategy by player 1 (C/D) : ")
# print("best choice for his oponent is : ",best_response(0,x))

# #Find Nash Equilibria
# nash_equilibria = []

# for s1, s2 in itertools.product(strategies, strategies):
#     br1 = best_response(0, s2)
#     br2 = best_response(1, s1)

#     if s1 in br1 and s2 in br2:
#         nash_equilibria.append((s1, s2))

# print("-"*111)
# print("Nash Equilibria can be occured at :", nash_equilibria)