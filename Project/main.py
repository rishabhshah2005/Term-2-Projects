marks = {"rishabh":[90, 88, 100, 99, 96],
         'drona':[76, 38, 56, 43, 53], 
         'ashmita':[34, 43, 56, 78, 99],
         "avi": [99, 99, 99, 99, 88],
         "sam": [32, 55, 0, 4, 12],
         "ishan": [45, 64, 78 ,98, 44]}

subs = ['Eng', 'Chem', 'Phy', 'Maths', 'CS']

def insert_record():
  name = str(input('name: '))
  if name in marks:
    print('Name already exists. Try again')
  
  else:
    mrks = []
    for i in subs:
      mark = int(input(f'Enter marks of {i}: '))
      mrks.append(mark)
    marks[name] = mrks
    print('Record added')

def update_record():
  name = str(input('Enter name: '))
  if name in marks:
    mrks = []
    for i in subs:
      mark = int(input(f'Enter marks of {i}: '))
      mrks.append(mark)
    marks[name] = mrks
    print('Record updated')
  else:
    print('Name does not exist. Try again')

def display_all():
  for i in marks:
    print(f"{i} : {marks[i]}")

def search_min():
  min_per = int(input("Minimum percentage: "))
  for i in marks:
    per = int((sum(marks[i])/500)*100)
    if per >= min_per:
      print(f"{i} scored {per}%")

def max_marks():
  for i in marks:
    mx = max(marks[i])
    print(f'{i} scored max in {subs[marks[i].index(mx)]} ({mx})')


print('INDEXS \n1. Display all records \n2. Add new record \n3. Update existing record \n4. Search with minimum percentage \n5. Search max marks for each student \n6. EXIT')

while True:
  index = int(input('enter index: '))
  if index==1:
    display_all()
  elif index==2:
    insert_record()
  elif index==3:
    update_record()
  elif index==4:
    search_min()
  elif index == 5:
    max_marks()
  elif index==6:
    break
  else:
    print('Invalid index')
