""" 
Given student marks in 3 subjects:

marks = np.array([
    [78, 85, 90],
    [88, 92, 80],
    [60, 65, 70],
    [95, 98, 100]
])


Find the average marks per student

Find the average marks per subject

Find the highest scoring student
"""
import numpy as np 

# create array 
marks = np.array([
    [78,85,90],
    [88,92,80],
    [60,65,70],
    [95,98,100]
])

# average marks per student
j = 1
for i, student in enumerate(marks):
    print(f"Student {j} average: {np.average(student)} ")
    j+=1

#average marks per subject
print(f"Average per subject: {np.mean(marks,0)}")

# highest scoring atudent
total = np.sum(marks,axis=1)
highest_score = np.argmax(total)
print(f"Student {highest_score+1} highest score is {np.max(total)}")
