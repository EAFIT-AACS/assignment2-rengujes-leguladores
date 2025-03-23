from tabulate import tabulate


with open("generated_strings.txt", "r") as file:
    lines = file.readlines()  # Read all lines from the file

string_list = []  # Initialize an empty list

# Iterate over all lines in the file
for line in lines:
    # Remove spaces at the beginning and end, and the period (.) after the number
    line = line.strip()
    
    # If the line starts with a number and a period, remove them
    if line and line[0].isdigit():  # Check if the line starts with a number
        # Remove the period and any extra spaces after the number
        line = line.split(".", 1)[1].strip() if "." in line else line.strip()
        
        # If the line is not empty after processing, add it to the list
        if line:
            string_list.append(line)
        else:
            string_list.append("")  # If it's empty, add an empty string

# Print the list to verify the results
print(string_list)




class PDA:
    def __init__(self):
        self.starting_pile_symbol = "S" # Give the PDA starting parameters
        self.starting_state = "q0"

    def transitions(self , stack , current_state , char): # Here we define all rules of the automata, taking in to account the production rules of the grammar
        
        if(len(stack) != 0):
            
            if (current_state == "q0" and char == "" and stack[-1] == "S"):
                stack.pop()
                return 1 , current_state
            elif (current_state == "q0" and char == "a" and stack[-1] == "S"):
                stack.pop()
                stack.append("a")
                return 2 , current_state
            elif (current_state == "q0" and char == "a" and stack[-1] == "a"):
                stack.append("a")
                return 3 , current_state
            elif (current_state == "q0" and char == "b" and stack[-1] == "a"):
                stack.pop()
                current_state = "q1"
                return 4 , current_state
            elif (current_state == "q1" and char == "b" and stack[-1] == "a"):
                stack.pop()
                return 5 , current_state
            else:
                return -1 , current_state
        else:
            return -1 , current_state
        
        # In case we dont find any rule that match the current state and char, we return -1, meaning that the string is not valid
 
        
    def is_valid(self, string):
        stack = []
        stack.append(self.starting_pile_symbol) # Start the stack with the starting pile symbol

        if len(string) == 0: # If the string is empty, we return true, because the grammar accepts epsilon
            return True , [1]

        transitions_done = []

        current_state = self.starting_state
        
        for char in string:

            transition , current_state = self.transitions(stack, current_state, char)
            if transition == -1: 
                transitions_done.append(transition) # Break when we find a transition that is not valid
                return False , transitions_done 
            
            transitions_done.append(transition)  # Append every number of the transitions done 
            

        if (len(stack) != 0):
            return False , transitions_done   # If the stack is not empty, we return false, because the string is not valid
        
        return True , transitions_done  # Else, we return true, because the string is valid


pda = PDA()

results = []

for string in string_list:
    accepted , transitions_done = pda.is_valid(string) # Unpack the values of the is_valid function
    
    checkmark = "✅" if accepted else "❌"

    results.append([string, checkmark])
    if accepted:                           # (i)           #aSb                     #q , aaaabbb , a
        
        if len(string) == 0:
            string = "ε"

        set_of_applied_rules = [["", f"q0 , {string} , S"]]

        pile = ""

        for number in transitions_done:
            string = string[1:]

            if len(string) == 0:
                string = "ε"

            if(number == 1):
                set_of_applied_rules.append(["(i)" ,  "q0, ε, ε"])
            elif(number == 2):
                pile = pile + "a"
                set_of_applied_rules.append(["(ii)" , f"q0 , {string} , {pile}"])
                
            elif(number == 3):
                pile = pile + "a"
                set_of_applied_rules.append(["(iii)" , f"q0 , {string} , {pile}"])
                
            elif(number == 4):
                pile = pile[1:]
                if pile == "":
                    pile = "ε"
                set_of_applied_rules.append(["(iv)" , f"q1 , {string} , {pile}"])
                
            elif(number == 5):
                pile = pile[1:]
                if pile == "":
                    pile = "ε"
                set_of_applied_rules.append(["(v)" , f"q1 , {string} , {pile}"])

        print("\n")
                
            

        table = tabulate(set_of_applied_rules, headers=["Rules", "Computation of M on input x"], tablefmt="grid")
        print(table)    
   

# Create table using tabulate
table = tabulate(results, headers=["String", "Result"], tablefmt="grid")

# Export table to a .txt file
with open("results.txt", "w", encoding="utf-8") as output_file:
    output_file.write(table)

print("\n✅ Results exported to 'results.txt'")

