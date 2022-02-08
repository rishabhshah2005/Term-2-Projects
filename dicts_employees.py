employees = {'rishabh':[5000, 8000, 50000],
             'avi':[10000, 20000, 100000],
             'sam':[200, 4000, 20000]}

for i in employees:
    print(f"The total salary of {i} is ${sum(employees[i])}")

# OUTPUT 
# The total salary of rishabh is $63000
# The total salary of avi is $130000
# The total salary of sam is $24200

# Code by Rishabh Shah 