import random
def valid (num_letters):
    # Genera una cadena con "a" seguida de "b"
    sub_string_a = "a" * num_letters
    sub_string_b = "b" * num_letters
    generated_string = sub_string_a + sub_string_b
    return generated_string
def invalid (num_letters):
    generated_string = "".join(random.choice(["a", "b"]) for _ in range(num_letters))
    return generated_string

# Solicitar al usuario cuántas cadenas generar
num_strings = int(input("Please enter how many strings you want to generate: ")) 
string_set = set()  # Usamos un set para evitar duplicados

# Generar cadenas únicas
while len(string_set) < num_strings:
    option = random.choice([0, 1])
    num_letters = random.randint(0, 10)  # Asegura que haya al menos 1 letra
    
    if option == 1:
        generated_string = valid(num_letters)
    else:
        # Caso donde se genera una cadena con letras aleatorias "a" o "b"
        generated_string = invalid(num_letters)
    
    # Agregar solo si no está en el set
    if generated_string not in string_set:
        string_set.add(generated_string)  

# Crear el contenido del archivo .txt
txt_content = "============================\n"
txt_content += "       GENERATED STRINGS     \n"
txt_content += "============================\n\n"

# Agregar cada cadena con numeración
for i, string in enumerate(string_set, start=1):
    txt_content += f"{i}. {string}\n"

# Guardar el contenido en un archivo .txt
with open("generated_strings.txt", "w", encoding="utf-8") as file:
    file.write(txt_content)

print("The generated strings have been saved in 'generated_strings.txt'.")

