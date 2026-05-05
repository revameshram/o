import random
import matplotlib.pyplot as plt

particles = [random.uniform(0, 100) for _ in range(100)]
true_altitude = 50

def weight(p):
    return 1 / (1 + abs(p - true_altitude))

weights = [weight(p) for p in particles]
new_particles = random.choices(particles, weights=weights, k=100)

estimate = sum(new_particles) / len(new_particles)

plt.hist(particles, bins=20, alpha=0.5, label="Before Resampling")
plt.hist(new_particles, bins=20, alpha=0.5, label="After Resampling")
plt.axvline(true_altitude, linestyle='dashed', label="True Altitude")
plt.axvline(estimate, linestyle='solid', label="Estimated Altitude")

plt.legend()
plt.title("Drone Altitude Estimation using Particle Filter")
plt.xlabel("Altitude")
plt.ylabel("Frequency")
plt.show()

print("Estimated Altitude:", round(estimate, 2))


#to avoid matplot:
# import numpy as np

# N = 100
# particles = np.random.uniform(0, 100, N)

# true_altitude = 50

# def move(particles):
#     return particles + np.random.normal(0, 1, len(particles))

# def measure(true_alt):
#     return true_alt + np.random.normal(0, 2)

# def update(particles, measurement):
#     weights = np.exp(-(particles - measurement)**2 / 10)
#     weights /= np.sum(weights)
#     return weights

# def resample(particles, weights):
#     indices = np.random.choice(len(particles), size=len(particles), p=weights)
#     return particles[indices]

# for t in range(5):
#     true_altitude += np.random.normal(0, 1)
#     particles = move(particles)
#     z = measure(true_altitude)
#     weights = update(particles, z)
#     particles = resample(particles, weights)

#     print(f"Step {t}, Estimated Altitude:", np.mean(particles))
