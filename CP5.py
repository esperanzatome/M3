"""
Exercise 1: 
Create a dictionary called student with the keys: name, age, major, year, and classes.
"""
student= {
  'name': 'Esperanza',
  'age': 41,
  'major': 'Python',
  'year': 2023,
  'classes': ['css','html']
}
print(student)
"""
Exercise 2:
Use the get method to print the value of the key “name”.
"""
student.get('name')
print(student.get('name'))
"""
Exercise 3:
Use the pop method to remove “year” from the dictionary.
"""
student.pop('year')
print(student)
"""
Exercise 4:
Add the key/value pair of “gpa” : 3.9 to the dictionary.
"""
student ['gpa'] = 3.9
print(student)
"""
Exercise 5:
Change the “gpa” value from 3.9 to 4.0
"""
student['gpa'] = 4.0
print(student)
"""
Exercise 6:
Create a new dictionary with the name collegeStudents and make it so the keys are name, age, major, year, and gpa. The values are in a list, where each index in the list is a student. Next, add a few students.
"""
students=[
['Esperanza',41,'Python',2023,['css','html'],3.9],
['Perico',39,'Python',2022,['word'],4.0],
['Maria',32,'Python',2022,['css','word'],3.8]
] 
for student in students:
  collegeStudents= {
    'name':student[0],
    'age':student[1],
    'major':student[2],
    'year':student[3],
    'classes':student[4],
    'gpa':student[5]
  }
  print(collegeStudents.items())
"""
Exercise 7:
Sort the dictionary
"""
students=[
['Esperanza',41,'Python',2023,['css','html'],3.9],
['Perico',39,'Python',2022,['word'],4.0],
['Maria',32,'Python',2022,['css','word'],3.8]
] 
for student in sorted(students):
  collegeStudents= {
    'name':student[0],
    'age':student[1],
    'major':student[2],
    'year':student[3],
    'classes':student[4],
    'gpa':student[5]
  }
  print(collegeStudents.items())
