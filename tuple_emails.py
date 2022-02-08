from doctest import OutputChecker


users = {'rishabh': ['dyfsdshssah2455@gmail.com', 'blabla.com'],
         'avi': ['jidaijdagmail.com', 'duduus.com'],
         'mayank': ['mayank@gmail.com', 'mayank.com']}

emails = ()
usernames = ()
domains = ()

for i in users:
    usernames += (i,)
    emails +=(users[i][0],)
    domains +=(users[i][1],)

print(f"Emails: {emails}")
print(f"Usernames: {usernames}")
print(f"Domains: {emails}")

# OUTPUT 
# Emails: ('dyfsdshssah2455@gmail.com', 'jidaijdagmail.com', 'mayank@gmail.com')
# Usernames: ('rishabh', 'avi', 'mayank')
# Domains: ('dyfsdshssah2455@gmail.com', 'jidaijdagmail.com', 'mayank@gmail.com')


# Code by Rishabh Shah