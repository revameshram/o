measurements = [1, 2, 3, 4, 5]

x = 0
P = 1
Q = 0.1
R = 0.5

print("Tracking Moving Object:\n")

for z in measurements:
    x_pred = x
    P_pred = P + Q

    K = P_pred / (P_pred + R)

    x = x_pred + K * (z - x_pred)
    P = (1 - K) * P_pred

    print("Measured Position:", z, "Estimated Position:", round(x, 2))
