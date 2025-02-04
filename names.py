#prompt user to enter the names
names = input("Enter a list of number seperated by commas:  ")

#split the names into a list
name_list= names.split(", ")

#to remove any duplicate names
unique_name = set(name_list)

#To sort in alphabetical order
unique_sorted_names = sorted(unique_name)

#Displays the sorted names
print("Final sorted list: ",unique_sorted_names)

#counts and displays the number of names
print("The total number of names is: ", len(name_list))