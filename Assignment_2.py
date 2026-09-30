# Program Name: Assignment2.py
	# Course: IT3883
	# Student Name: Michael Burrough
	# Assignment Number: Lab1
	# Due Date: 1022/ 2026
    # Purpose: Program will take input data from individuals and find avg. Program will display avg of individuals in descending order
    #Resources: https://www.w3schools.com/python/python_file_open.asp
    #https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
    #https://stackoverflow.com/questions/27550785/python-descending-order-from-text-file

with open("Assignment2input.txt", "r") as file:


     students = {}

     for line in file:

          parts = line.strip().split(' ')
          if not parts or parts[0] == '':
               continue

          name = parts[0]
          scores = [float(score) for score in parts[1:]]


          avg  = sum(scores) / len(scores)
          students[name] = avg

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)



for name, avg in sorted_students:
    print(f"{name}: {avg:.2f}")
