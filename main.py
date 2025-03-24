from ALGORITHM_1_LFCO_2025_AT_SS import StringGenerator
from ALGORITHM_2_LFCO_2025_AT_SS import PDA
from ALGORITHM_3_LFCO_2025_AT_SS import Rules_table

stringGenerator = StringGenerator()
pda = PDA()
rules_table = Rules_table()

set_of_strings = stringGenerator.generateStrings()

for string in set_of_strings:
    accepted, transitions_done = pda.is_valid(string)
    if accepted:
        print(f"The string {string} is valid")
    else:
        print(f"The string {string} is invalid")


for string in set_of_strings:
    rules_table.aplied_rules(string)




