# Rain -> WetGrass <- Sprinkler

import matplotlib.pyplot as plt
import networkx as nx

P_Rain = 0.2
P_Sprinkler = 0.4

P_WetGrass = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.80,
    (False, False): 0.0
}

def joint_probability(rain, sprinkler, wet):
    p_r = P_Rain if rain else 1 - P_Rain
    p_s = P_Sprinkler if sprinkler else 1 - P_Sprinkler
    p_w = P_WetGrass[(rain, sprinkler)] if wet else 1 - P_WetGrass[(rain, sprinkler)]
    return p_r * p_s * p_w


def compute_values():
    numerator = 0
    for s in [True, False]:
        numerator += joint_probability(True, s, True)

    denominator = 0
    for r in [True, False]:
        for s in [True, False]:
            denominator += joint_probability(r, s, True)

    posterior = numerator / denominator

    print(f"\nNumerator: {numerator:.3f}")
    print(f"Denominator: {denominator:.3f}")
    print("P(Rain | WetGrass=True) =", round(posterior, 4))


def visualize_network():
    G = nx.DiGraph()
    G.add_edges_from([
        ("Rain", "WetGrass"),
        ("Sprinkler", "WetGrass")
    ])

    pos = {
        "Rain": (-1, 1),
        "Sprinkler": (1, 1),
        "WetGrass": (0, 0)
    }

    nx.draw(G, pos, with_labels=True,
            node_size=5000,
            node_color="lightgrey",
            font_size=12,
            font_weight="bold",
            arrowsize=20)

    plt.title("Bayesian Network: Rain -> WetGrass <- Sprinkler")
    plt.show()


while True:
    print("\nChoose an option:")
    print("1. Compute Probability Values")
    print("2. Visualize Bayesian Network")
    print("3. Do Both")
    print("4. Exit")

    choice = input("Enter choice : ")

    match choice:
        case "1":
            compute_values()
        case "2":
            visualize_network()
        case "3":
            compute_values()
            visualize_network()
        case "4":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice. Please try again.")
# py -m pip install networkx matplotlib






#to avoid matplot use this

# # Bayesian Network: Lecture Scenario with Posterior Probability
# from pgmpy.models import DiscreteBayesianNetwork
# from pgmpy.factors.discrete import TabularCPD
# from pgmpy.inference import VariableElimination

# # --- 1) Define Network Structure ---
# # L (Lecture) depends on A (Patil Mam) and H (H.O.D)
# model = DiscreteBayesianNetwork([('A','L'), ('H','L')])

# # --- 2) Define Probabilities ---

# # Prior probabilities
# cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.3],[0.7]])  # A=0 (absent), A=1 (present)
# cpd_H = TabularCPD(variable='H', variable_card=2, values=[[0.4],[0.6]])  # H=0 (absent), H=1 (present)

# # Conditional Probability Table for Lecture
# cpd_L = TabularCPD(
#     variable='L', variable_card=2,
#     values=[[0.05, 0.2, 0.4, 0.9],    # L=0 (Lecture not held)
#             [0.95, 0.8, 0.6, 0.1]],   # L=1 (Lecture held)
#     evidence=['A','H'],
#     evidence_card=[2,2]
# )

# # --- 3) Add CPDs to model ---
# model.add_cpds(cpd_A, cpd_H, cpd_L)

# # Validate model
# assert model.check_model(), "Model is incorrect!"

# # --- 4) Perform Inference ---
# infer = VariableElimination(model)

# # Example Query: P(A | L=True)
# posterior_A = infer.query(variables=['A'], evidence={'L':1})
# print("P(Patil Mam present | Lecture occurred):\n", posterior_A)