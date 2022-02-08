contacts = {'rishabh':'9376426806', "sam":'6864267478'}

contact = input("enter name: ")
if contact in contacts:
    print('contact found')
else:
    'contact not found'
    exit()

new = input("Enter New number: ")
contacts[contact] = new

# OUTPUT 
# enter name: sam
# contact found
# Enter New number: 48365264644

# Code by Rishabh Shah