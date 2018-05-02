import numpy as np
from collections import defaultdict
from operator import itemgetter

dataset_filename = 'affinity_dataset.txt'
X = np.loadtxt(dataset_filename)
n_samples, n_features = np.shape(X) # X: 100*5
features = ['bread', 'milk', 'cheese', 'apple', 'banana']

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)

for sample in X:
	for premise in range(5):
		if sample[premise] == 0:
			continue
		num_occurances[premise] += 1

		# 跳过结论和条件相同的地方
		for conclusion in range(n_features):
			if premise == conclusion:
				continue

			if sample[conclusion] == 1:
				valid_rules[(premise, conclusion)] += 1
			else:
				invalid_rules[(premise, conclusion)] += 1

support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
	rule = (premise, conclusion)
	confidence[rule] = valid_rules[rule] / num_occurances[premise]

def print_rule(premise, conclusion, support, confidence, features):
	premise_name = features[premise]
	conclusion_name = features[conclusion]
	print('Rules: If a person buys {0} they will also buy {1}'.format(premise_name, conclusion_name))
	print(' - Support: {0}'.format(support[(premise,conclusion)]))
	print(' - Confidence: {0:.3f}'.format(confidence[(premise,conclusion)]))

sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
for index in range(5):
	print('Rule #{0}'.format(index+1))
	premise, conclusion = sorted_support[index][0]
	print_rule(premise, conclusion, support, confidence, features)

# sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)
# for index in range(5):
# 	print('Rule #{0}'.format(index+1))
# 	premise, conclusion = sorted_confidence[index][0]
# 	print_rule(premise, conclusion, support, confidence, features)





