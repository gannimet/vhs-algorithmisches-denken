import matplotlib.pyplot as plt

def train_perceptron(training_data):
    w0 = 0
    w1 = 0
    b = 0
    total_num_points = len(training_data[0][1]) + len(training_data[1][1])
    max_num_iterations = 100_000

    for i in range(max_num_iterations):
        d_b = 0
        d_w0 = 0
        d_w1 = 0
        total_error = 0;

        for (y, points) in training_data:
            for (x0, x1) in points:
                z = w0 * x0 + w1 * x1 + b
                a = 1 if z > 0 else 0
                error = y - a
                d_w0 += error * x0
                d_w1 += error * x1
                d_b += error
                total_error += error ** 2

        if total_error == 0:
            print(f"Finished after {i+1} iterations.")
            return (w0, w1, b)

        d_w0 = d_w0 / total_num_points
        d_w1 = d_w1 / total_num_points
        d_b = d_b / total_num_points

        w0 += d_w0
        w1 += d_w1
        b += d_b

    print(f"Giving up after {max_num_iterations} iterations.")
    return (w0, w1, b)


classified_points = [
    (0, [(0.54, 0.31), (0.37, 0.48), (0.46, 0.42), (0.56, 0.25), (0.77, 0.22), (0.42, 0.46)]),
    (1, [(0.54, 0.60), (0.71, 0.62), (0.51, 0.63), (0.67, 0.44), (0.37, 0.81), (0.65, 0.54)])
]

(w0, w1, b) = train_perceptron(classified_points)

m = -(w0 / w1)
n = -(b / w1)

print(f"Final weights: (b, w0, w1) = {(b, w0, w1)}")
print(f"Linear function params (m, n) = {(m, n)}")

plt.scatter(*zip(*classified_points[0][1]), color='blue', label='Iris Setosa')
plt.scatter(*zip(*classified_points[1][1]), color='red', label='Iris Versicolor')
plt.legend()

X = [0, 1]
Y = [m * x + n for x in X]
plt.plot(X, Y, color='green')

plt.xlabel('x_0')
plt.ylabel('x_1')
plt.grid()
plt.tight_layout()
plt.show()

