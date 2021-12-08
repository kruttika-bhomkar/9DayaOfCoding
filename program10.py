# Python3 program to insert
# an element into sorted list

# Function to insert element


def insert(list, n):

	index = len(list)
	# Searching for the position
	for i in range(len(list)):
	if list[i] > n:
		index = i
		break

	# Inserting n in the list
	if index == len(list):
	list = list[:index] + [n]
	else:
	list = list[:index] + [n] + list[index:]
	return list

# Driver function
list = [1, 2, 4]
n = 3

print(insert(list, n))
