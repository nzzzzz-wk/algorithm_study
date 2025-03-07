import numpy as np
def single_neuron_model(features, labels, weights, bias):
    x = np.dot(features,weights)+bias
    probabilities = 1/(1+np.exp(-x))
    mse = np.mean((probabilities - np.array(labels))**2)
    return [round(p,4) for p in probabilities],round(mse,4)


if __name__ == "__main__":
    features = np.array([[1, 2], [2, 3]])
    labels = np.array(eval(input()))
    weights = np.array(eval(input()))
    bias = float(input())
    print(single_neuron_model(features, labels, weights, bias))
