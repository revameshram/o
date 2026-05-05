import random
import matplotlib.pyplot as plt

particles = [(random.uniform(0,10), random.uniform(0,10)) for _ in range(100)]
true_pos = (6, 4)

def weight(p):
    return 1 / (1 + ((p[0]-true_pos[0])**2 + (p[1]-true_pos[1])**2)**0.5)

weights = [weight(p) for p in particles]
new_particles = random.choices(particles, weights=weights, k=100)

x_est = sum(p[0] for p in new_particles) / len(new_particles)
y_est = sum(p[1] for p in new_particles) / len(new_particles)

x_before = [p[0] for p in particles]
y_before = [p[1] for p in particles]

x_after = [p[0] for p in new_particles]
y_after = [p[1] for p in new_particles]

plt.scatter(x_before, y_before, label="Before Resampling")
plt.scatter(x_after, y_after, label="After Resampling")
plt.scatter(*true_pos, marker='x', s=100, label="True Position")
plt.scatter(x_est, y_est, marker='o', s=100, label="Estimated Position")

plt.legend()
plt.title("2D Person Tracking using Particle Filter")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

print("Estimated Position:", (round(x_est,2), round(y_est,2)))



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