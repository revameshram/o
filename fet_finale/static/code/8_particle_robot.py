import random
import matplotlib.pyplot as plt

particles = [random.randint(0, 9) for _ in range(100)]
true_position = 5

def weight(p):
    return 1 / (1 + abs(p - true_position))

weights = [weight(p) for p in particles]
new_particles = random.choices(particles, weights=weights, k=100)

estimate = sum(new_particles) / len(new_particles)

plt.hist(particles, bins=10, alpha=0.5, label="Before Resampling")
plt.hist(new_particles, bins=10, alpha=0.5, label="After Resampling")
plt.axvline(true_position, linestyle='dashed', label="True Position")
plt.axvline(estimate, linestyle='solid', label="Estimated Position")

plt.legend()
plt.title("1D Robot Tracking using Particle Filter")
plt.xlabel("Position")
plt.ylabel("Frequency")
plt.show()

print("Estimated Position:", round(estimate, 2))


# #if 2d comes:
# import numpy as np

# N = 200
# particles = np.random.rand(N, 2) * 10

# true_pos = np.array([5.0, 5.0])

# def move(particles):
#     return particles + np.random.normal(0, 0.5, particles.shape)

# def measure(true_pos):
#     return true_pos + np.random.normal(0, 1, 2)

# def update(particles, measurement):
#     dist = np.linalg.norm(particles - measurement, axis=1)
#     weights = np.exp(-dist)
#     weights /= np.sum(weights)
#     return weights

# def resample(particles, weights):
#     indices = np.random.choice(len(particles), size=len(particles), p=weights)
#     return particles[indices]

# for t in range(5):
#     true_pos += np.random.normal(0, 1, 2)
#     particles = move(particles)
#     z = measure(true_pos)
#     weights = update(particles, z)
#     particles = resample(particles, weights)

#     print(f"Step {t}, Estimated Position:", np.mean(particles, axis=0))









# #if 1d comes
# import numpy as np

# # number of particles
# N = 100
# particles = np.random.randint(0, 10, N)

# true_position = 5

# def move(particles):
#     return particles + np.random.choice([-1, 0, 1], size=len(particles))

# def measure(true_pos):
#     return true_pos + np.random.normal(0, 1)

# def update(particles, measurement):
#     weights = np.exp(-(particles - measurement)**2)
#     weights /= np.sum(weights)
#     return weights

# def resample(particles, weights):
#     indices = np.random.choice(len(particles), size=len(particles), p=weights)
#     return particles[indices]

# for t in range(5):
#     true_position += np.random.choice([-1, 1])
#     particles = move(particles)
#     z = measure(true_position)
#     weights = update(particles, z)
#     particles = resample(particles, weights)

#     print(f"Step {t}, Estimated Position:", np.mean(particles))