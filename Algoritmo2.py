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


class PDA:
    def __init__(self):
        self.starting_pile_symbol = "S" # We are only going to use the acceptance judgement on the empty stack, so no need to stablish an acceptance state
    
    def is_valid(self, string):
        stack = []
        stack.append(self.starting_pile_symbol)

        if len(string) == 0:
            return True
        
        for char in string:
            if char == "a":
                stack.append(char)
            elif char == "b":
                if len(stack) == 0:
                    return False
                if stack[-1] == "a":
                    stack.pop()
            print(stack)
        

        if len(stack) == 1 and stack[0] == self.starting_pile_symbol:
            stack.pop()
            return True
        
       
pda = PDA()

for string in string_list:
    accepted = pda.is_valid(string)
    if accepted:
        print(f"The string '{string}' is accepted by the grammar")
    else:
        print(f"The string '{string}' is not accepted by the grammar")


