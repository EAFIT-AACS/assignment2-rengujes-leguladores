with open("generated_strings.txt", "r") as file:
    lines = file.readlines()  #Open the file

string_list = [] #Inicializate a empty list

for line in lines:
    parts = line.strip().split(maxsplit=1)  #Split strings to be easier to read later(by index, space and contend)
    if len(parts) > 1 and parts[0].isdigit():  
        string_list.append(parts[1])  


for line in lines[4:]:  
    parts = line.strip().split(maxsplit=1)  
    if len(parts) > 1:
        string_list.append(parts[1])  #Add strings where the shape is correct

print(string_list)

