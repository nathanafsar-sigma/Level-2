people = [
  {'First name' : 'Jane', 'Last name' : 'Doe', 'Age' : 42, 'Employed':'Yes'},
  {'First name' : 'Tom', 'Last name' : 'Smith', 'Age' : 18, 'Employed':'Yes'},
  {'First name' : 'Mariam', 'Last name' : 'Coulter', 'Age' : 66, 'Employed':'No'},
  {'First name' : 'Gregory', 'Last name' : 'Tims', 'Age' : 8, 'Employed':'No'}
]

def print_people(people):
  for person in people:
    print(f"Name: {person['First name']} {person['Last name']}")
    print(f"Age: {person['Age']}")
    print(f"Employed: {person['Employed']}")
  return

def add_people(people):
  first_name = input("What is their First name: ")
  last_name = input("What is their Last name: ")
  age = int(input("What is their Age: "))
  employed = input("Are they employed 'Yes' or 'No': ")
  people.append({'First name' : first_name, 'Last name' : last_name, 'Age' : age, 'Employed':employed})
  return people

def remove_people(people):
  first_name = input("What is the First name of the person you would like to remove: ")
  for i, person in enumerate(people):
    if first_name == person['First name']:
      people.pop(i)
  return people

while True:
  print_people(people)
  response = input("Would you like to 'Add' or 'Remove': ")
  if response == 'Add':
    people = add_people(people)
  elif response == 'Remove':
    people = remove_people(people)
  else:
    print("That is not a valid response")
