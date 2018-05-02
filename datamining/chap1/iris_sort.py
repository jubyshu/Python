import numpy as np
from collections import defaultdict
from operator import itemgetter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dataset = load_iris()
x = dataset.data
y_true = dataset.target
n_samples, n_features = x.shape

attribute_means = x.mean(axis=0)
x_d = np.array(x >= attribute_means, dtype='int')

x_train, x_test, y_train, y_test = train_test_split(x_d, y_true, 
random_state=14)

def train_feature_value(x, y_true, feature_index, value):
	class_counts = defaultdict(int)
	for sample, y in zip(x, y_true):
		if sample[feature_index] == value:
			class_counts[y] += 1
	sorted_class_counts = sorted(class_counts.items(), 
	key=itemgetter(1), reverse=True)
	most_frequent_class = sorted_class_counts[0][0]

	incorrect_predictions = [class_count for class_value, class_count
	in class_counts.items() 
	if class_value != most_frequent_class]
	error = sum(incorrect_predictions)
	return most_frequent_class, error

def train_on_feature(x, y_true, feature_index):
	values = set(x[:, feature_index])

	predictors = dict()
	errors = []

	for current_value in values:
		most_frequent_class, error = train_feature_value(x, 
		y_true, feature_index, current_value)
		predictors[current_value] = most_frequent_class
		errors.append(error)
	total_error = sum(errors)
	return predictors, total_error

# for feature_index in range(xd_train.shape[1]):
# 	predictors, total_error = train_on_feature(xd_train, y_train, 
# 	feature_index)
# 	all_predictors[feature_index] = predictors
# 	errors[feature_index] = total_error

all_predictors = {variable: train_on_feature(x_train, y_train, variable) for variable in range(x_train.shape[1])}
errors = {variable: error for variable, (mapping, error) in all_predictors.items()}

best_variabel, best_error = sorted(errors.items(), key=itemgetter(1))[0]
model = {
	'variable': best_variabel,
	'predictor': all_predictors[best_variabel][0],
    }

# variable = model['variable']
# predictor = model['predictor']
# prediction = predictor[int(sample[variable])]

def predict(x_test, model):
	variable = model['variable']
	predictor = model['predictor']
	y_predicted = np.array([predictor[int(sample[variable])] for 
	sample in x_test])
	return y_predicted

y_predicted = predict(x_test, model)
accuracy = np.mean(y_predicted == y_test) * 100
print('The test accuracy is {:.1f}%'.format(accuracy))
