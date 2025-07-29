import numpy as np

gamma = 0.9

r = np.array([1, 7, 9, 15, 3])

P = np.array([[0.3, 0.05, 0.25, 0.1, 0.3],
              [0.5, 0.15, 0.1, 0.05, 0.2],
              [0.5, 0.0, 0.3, 0.0, 0.2],
              [0.3, 0.15, 0.15, 0.0, 0.4],
              [0.25, 0.5, 0.25, 0.0, 0.0]])

v = np.linalg.inv(np.eye(5) - gamma * P)  @ r

print(v)
print("-----------------------")
v_it = np.array([0, 0, 0, 0, 0])
for i in range(101):
    if i % 10 == 0 or i == 1:
        print(v_it)
    v_it = r + gamma*P@v_it
