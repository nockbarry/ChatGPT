import numpy as np
from hmmlearn import hmm

# Generate some sample data
transactions = [
    {'amount': 100, 'product': 'clothing', 'location': 'USA'},
    {'amount': 50, 'product': 'grocery', 'location': 'USA'},
    {'amount': 200, 'product': 'clothing', 'location': 'USA'},
    {'amount': 200, 'product': 'electronics', 'location': 'USA'},
    {'amount': 1000, 'product': 'clothing', 'location': 'Russia'},
    {'amount': 500, 'product': 'grocery', 'location': 'Russia'},
    {'amount': 2000, 'product': 'clothing', 'location': 'Russia'},
    {'amount': 2000, 'product': 'electronics', 'location': 'Russia'},
]

# Define the hidden states and observation symbols
hidden_states = ['fraud', 'not fraud']
observation_symbols = ['amount', 'product', 'location']

# Define the transition probabilities
transition_probabilities = [
    [0.9, 0.1],  # from 'fraud' to ['fraud', 'not fraud']
    [0.1, 0.9],  # from 'not fraud' to ['fraud', 'not fraud']
]

# Define the emission probabilities
emission_probabilities = [
    # for 'fraud'
    {
        'amount': [0.2, 0.4, 0.4],  # P(amount | fraud)
        'product': [0.5, 0.5],  # P(product | fraud)
        'location': [0.5, 0.5],  # P(location | fraud)
    },
    # for 'not fraud'
    {
        'amount': [0.6, 0.3, 0.1],  # P(amount | not fraud)
        'product': [0.2, 0.8],  # P(product | not fraud)
        'location': [0.8, 0.2],  # P(location | not fraud)
    },
]

# Create the HMM model
model = hmm.MultinomialHMM(n_components=2)
model.startprob_ = np.array([0.5, 0.5])  # P(fraud) and P(not fraud)
model.transmat_ = np.array(transition_probabilities)
model.emissionprob_ = np.array([
    # for 'fraud'
    [
        # P(amount | fraud)
        emission_probabilities[0]['amount'][0],
        emission_probabilities[0]['amount'][1],
        emission_probabilities[0]['amount'][2],
        # P(product | fraud)
        emission_probabilities[0]['product'][0],
        emission_probabilities[0]['product'][1],
        # P(location | fraud)
        emission_probabilities[0]['location'][0],
        emission_probabilities[0]['location'][1],
    ],
    # for 'not fraud'
    [
        # P(amount | not fraud)
        emission_probabilities[1]['amount'][0],
        emission_probabilities[1]['amount'][1],
        emission_probabilities[1]['amount'][2],
        # P(product | not fraud)
        emission_probabilities[1]['product'][0],
        emission_probabilities[1]['product'][1],
        # P(location | not fraud)
        emission_probabilities[1]['location'][0],
        emission_probabilities[1]['location'][1],
    ],
])

# Split the transactions into a training set and a test set
train_size = int(len(transactions) * 0.8)
train_transactions = transactions[:train_size]
test_transactions = transactions[train_size:]
# Create a dictionary that maps observation symbols to integers
observation_symbol_to_int = {s: i for i, s in enumerate(observation_symbols)}

# Encode the observations as integers using the dictionary
X = [[observation_symbol_to_int[t[f]] for f in observation_symbols] for t in train_transactions]

# Fit the model to the encoded data
lengths = [len(x) for x in X]
model.fit(X, lengths)

# Fit the model to the training data
#X = [[t[f] for f in observation_symbols] for t in train_transactions]
#lengths = [len(x) for x in X]
#model.fit(X, lengths)

# Make predictions on the test data
predictions = []
for t in test_transactions:
    x = [[t[f] for f in observation_symbols]]
    y = model.predict(x)
    predictions.append(hidden_states[y[0]])

# Evaluate the model's performance
accuracy = sum(1 for p, t in zip(predictions, test_transactions) if p == t['label']) / len(predictions)
print(f'Accuracy: {accuracy:.2f}')
