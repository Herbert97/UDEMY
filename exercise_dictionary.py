# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

user= {
    'username': 'falcon',
    'age': 20,
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user SOLUTION.
print(user.keys())

# 3 Add a new weapon to your user SOLUTION.
user['weapons']= 'M141A'
print(user['weapons'])

# 4 Add a new key to include 'is_banned'. Set it to false SOLUTION.
user.update({'is_Banned': False})
print(user)

# 5 Ban the user by setting the previous key to True SOLUTION.
user['is_Banned']= True
print(user)

# 6 create a new user2 my copying the previous user and update the age value and username value SOLUTION.
user2=user.copy()
user2.update({
    'age':50,
    'username':'Pepe'
              })
print(user)
print(user2)
