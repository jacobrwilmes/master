employees = ["\n1 - Jude \n", "2 - Chantelle \n", "3 - Allyson \n", "4 - Jake" ]
presidents = ['\nwashington', '\nadams', '\njefferson', '\nlincoln']

with open("data.txt", "w") as file1:
    file1.write("employees \n")
    
with open("data.txt", "a") as file1:
    file1.writelines(employees)

with open("data.txt", "r+") as file1:
    print(file1.read())

print(7*12)



with open("data_2.txt", "w") as file2:
    file2.write("Here are the presidents: \n")

with open("data_2.txt", "a") as file2:
    file2.writelines(presidents)

for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)
