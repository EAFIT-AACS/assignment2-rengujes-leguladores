from tabulate import tabulate
from ALGORITHM_2_LFCO_2025_AT_SS import PDA

pda = PDA()

class Rules_table:
    def aplied_rules(self , string):
            
        accepted , transitions_done = pda.is_valid(string)
    
                  

        if accepted:             

            set_of_applied_rules = [["", f"q0 , {string} , S"]]              
            
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

            table = tabulate(set_of_applied_rules, headers=["Rules", "Computation of M on input x"], tablefmt="grid")
            print(table) 

            print("\n")
