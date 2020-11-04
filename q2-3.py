#Q2: create a loop with a range that asks for names and appends to list_names
body_count = int(input("How many people are present? "))
list_names = []
for j in range(body_count):
    print('Enter a name')
    name1 = str(input())
    list_names.append(name1.title())
print(list_names)


#Q3: make a loop that iterated over each name in list_name and
# format's it into lowercase in a new variable called list_names_lower

list_names_lower = []
for a in list_names:
    list_names_lower.append(a.lower())
print(list_names_lower)

#Q4: Iterate over the list of values to find if the are even
