states = ["Sunny", "Rainy"]
observations = ["Dry", "Wet"]

start_prob = {"Sunny": 0.6, "Rainy": 0.4}

transition_prob = {
    "Sunny": {"Sunny": 0.7, "Rainy": 0.3},
    "Rainy": {"Sunny": 0.4, "Rainy": 0.6}
}

emission_prob = {
    "Sunny": {"Dry": 0.8, "Wet": 0.2},
    "Rainy": {"Dry": 0.3, "Wet": 0.7}
}


def forward(obs_seq):
    alpha = {}

    for state in states:
        alpha[state] = start_prob[state] * emission_prob[state][obs_seq[0]]

    for t in range(1, len(obs_seq)):
        new_alpha = {}

        for curr_state in states:
            total = 0

            for prev_state in states:
                total += alpha[prev_state] * transition_prob[prev_state][curr_state]

            new_alpha[curr_state] = total * emission_prob[curr_state][obs_seq[t]]

        alpha = new_alpha

    return sum(alpha.values())


obs_sequence = ["Dry", "Wet", "Wet"]

print("Observation Sequence:", obs_sequence)
print("Probability:", forward(obs_sequence))




#another if not work

# import numpy as np
# # HMM parameters
# states = ['S', 'R']
# observations = ['D', 'W']

# start_prob = {'S':0.6, 'R':0.4}

# trans_prob = {
#     'S': {'S':0.7, 'R':0.3},
#     'R': {'S':0.4, 'R':0.6}
# }
# emit_prob = {
#     'S': {'D':0.9, 'W':0.1},
#     'R': {'D':0.2, 'W':0.8}
# }
# # Observation sequence: Dry, Wet, Dry
# obs_seq = ['D','W','D']

# # Forward algorithm
# def forward(obs_seq, states, start_prob, trans_prob, emit_prob):
#     fwd = [{}]
#     # Initialize
#     for s in states:
#         fwd[0][s] = start_prob[s] * emit_prob[s][obs_seq[0]]
    
#     # Recursion
#     for t in range(1, len(obs_seq)):
#         fwd.append({})
#         for s in states:
#             fwd[t][s] = sum(fwd[t-1][prev_s] * trans_prob[prev_s][s] * emit_prob[s][obs_seq[t]] for prev_s in states)
    
#     # Termination
#     prob = sum(fwd[len(obs_seq)-1][s] for s in states)
#     return prob

# prob_sequence = forward(obs_seq, states, start_prob, trans_prob, emit_prob)
# print("Probability of observing sequence {}: {:.5f}".format(obs_seq, prob_sequence))