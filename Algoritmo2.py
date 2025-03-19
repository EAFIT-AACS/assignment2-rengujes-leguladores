from tabulate import tabulate


with open("generated_strings.txt", "r") as file:
    lines = file.readlines()  # Open the file

string_list = []  # Initialize an empty list

for line in lines:
    parts = line.strip().split(maxsplit=1)  # Split to make it easier to read later (by index, space, and content)
    if len(parts) > 1 and parts[0].isdigit():
        string_list.append(parts[1])

for line in lines[4:]:  
    parts = line.strip().split(maxsplit=1)  
    if len(parts) > 1:
        string_list.append(parts[1])  # Add strings where the shape is correct


class PDA:
    def __init__(self):
        self.starting_pile_symbol = "S"  # We use the empty stack for acceptance
        self.starting_state = "q0"

    def transitions(self, stack, current_state, char):
        if len(stack) != 0:
            if current_state == "q0" and char == "" and stack[-1] == "S":
                stack.pop()
                return 1
            elif current_state == "q0" and char == "a" and stack[-1] == "S":
                stack.pop()
                stack.append("a")
                return 2
            elif current_state == "q0" and char == "a" and stack[-1] == "a":
                stack.append("a")
                return 3
            elif current_state == "q0" and char == "b" and stack[-1] == "a":
                stack.pop()
                current_state = "q1"
                return 4
            elif current_state == "q1" and char == "b" and stack[-1] == "a":
                stack.pop()
                return 5
            else:
                return -1
        else:
            return -1

    def is_valid(self, string):
        stack = []
        stack.append(self.starting_pile_symbol)

        if len(string) == 0:
            return True

        transitions_done = []

        for char in string:
            transitions_done.append(self.transitions(stack, self.starting_state, char))

        for transition in transitions_done:
            if transition == -1:
                return False

        return len(stack) == 0


pda = PDA()

results = []

for string in string_list:
    accepted = pda.is_valid(string)
    checkmark = "✅" if accepted else "❌"
    results.append([string, checkmark])

# Create table using tabulate
table = tabulate(results, headers=["String", "Result"], tablefmt="grid")

# Export table to a .txt file
with open("results.txt", "w", encoding="utf-8") as output_file:
    output_file.write(table)

print("\n✅ Results exported to 'results.txt'")
