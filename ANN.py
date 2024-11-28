def calculate_weighted_sum(inputs, weights, bias):
    """Calculates the weighted sum for the inputs."""
    return sum(i * w for i, w in zip(inputs, weights)) + bias

def activation_function(weighted_sum, threshold):
    """Applies the activation function."""
    return 1 if weighted_sum >= threshold else -1

def compute_difference(expected, actual):
    """Calculates the difference between expected and actual output."""
    return expected - actual

def adjust_weights(weights, error, inputs, learning_rate):
    """Updates the weights based on the error."""
    return [w + learning_rate * error * inp for w, inp in zip(weights, inputs)]

def adjust_bias(bias, error, learning_rate):
    """Updates the bias based on the error."""
    return bias + learning_rate * error

def adaline_training_step(inputs, weights, expected_outputs, threshold, bias, learning_rate):
    """Performs a single training step using the Adaline algorithm."""
    actual_outputs = []
    for input_vector, expected in zip(inputs, expected_outputs):
        weighted_sum = calculate_weighted_sum(input_vector, weights, bias)
        actual_output = activation_function(weighted_sum, threshold)
        actual_outputs.append(actual_output)
        
        error = compute_difference(expected, weighted_sum)
        if error != 0:
            weights = adjust_weights(weights, error, input_vector, learning_rate)
            bias = adjust_bias(bias, error, learning_rate)
    
    return actual_outputs, weights, bias

def train_adaline(inputs, expected_outputs, weights, threshold, bias, learning_rate):
    """Trains the model until actual outputs match expected outputs."""
    iteration_count = 0
    actual_outputs = []
    
    while actual_outputs != expected_outputs:
        iteration_count += 1
        actual_outputs, weights, bias = adaline_training_step(
            inputs, weights, expected_outputs, threshold, bias, learning_rate
        )
    
    print(f"Training completed in {iteration_count} iterations.")
    return inputs, expected_outputs, weights, threshold, bias, learning_rate

# OR gate training
print("Training OR Gate")
train_adaline([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 1], [0.1, 0.1], 0.5, 0, 0.2)
train_adaline([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 1], [0.9, 0.8], 0.5, 0, 0.2)
train_adaline([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 1], [0.5, 0.5], 0.5, 0, 0.2)
train_adaline([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 1], [0.2, 0.4], 0.5, 0, 0.2)
train_adaline([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 1], [-0.3, -0.5], 0.5, 0, 0.2)
