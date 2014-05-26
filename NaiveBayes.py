from sklearn.naive_bayes import GaussianNB
import numpy as np

training_data = np.array([
	[6, 180, 12],
	[5.92, 190, 11],
	[5.58, 170, 12],
	[5.92, 165, 10],
	[5, 100, 6],
	[5.5, 150, 8],
	[5.42, 130, 7], 
	[5.75, 150, 9]])

training_target = np.array([
	'Male',
	'Male',
	'Male',
	'Male',
	'Female',
	'Female',
	'Female',
	'Female'])

sample = np.array([6, 130, 8])

gnb = GaussianNB()

print gnb.fit(training_data, training_target).predict(sample)