employee = [
    {"ID": 1, "Name" : "John Doe", "Department" : "Sales", "Age" : "30", "Supplier Email" : "john.doe@company.com"},
    {"ID": 2, "Name" : "Jane Smith", "Department" : "Human Resources", "Age" : "25", "Supplier Email" : "jane.smith@company.com"},
    {"ID": 3, "Name": "Mark Johnson", "Department": "IT", "Age": "40", "Supplier Email": "mark.johnson@company.com"},
    {"ID": 4, "Name": "Lisa Wong", "Department": "Marketing", "Age": "28", "Supplier Email": "lisa.wong@company.com"},
    {"ID": 5, "Name": "Paul McDonald", "Department": "Finance", "Age": "35", "Supplier Email": "paul.mcdonald@company.com"}

]
for employees in employee:
  print(f"ID: {employees['ID']}, Name: {employees['Name']}, Department: {employees['Department']}, Age: {employees['Age']}, Supplier Email: {employees['Supplier Email']}")