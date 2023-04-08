"""
Creating a list of Python Services
"""

List = [] #Creating an empty list
List.append("Python") #adding AWS Services to our list
List.append("AWS")
List.append("EC2")
List.append("Lambda")
List.append("Glacier")
List.append("Cognito")

list_count = (len(List)) #Counting the number of services

print(list_count, List) #Printing the list and number of services

List.remove("Cognito")
List.remove("Lambda")
list_count = (len(List))

print(list_count, List) #Printing the updated list and number of services

