# Abre el archivo starting_letter.txt en modo de lectura
with open("starting_letter.txt", "r") as starting_letter_file:
    # Lee el contenido del archivo y lo almacena en una variable
    starting_letter = starting_letter_file.read()

# Abre el archivo invited_names.txt en modo de lectura
with open("invited_names.txt", "r") as names_file:
    # Inicializa una lista vacía para almacenar los nombres
    list_of_names = []
    # Itera sobre cada línea del archivo
    for line in names_file:
        # Agrega cada nombre a la lista list_of_names
        list_of_names.append(line)

# Elimina los saltos de línea al final de cada nombre y guarda los nombres en una nueva lista
new_list_of_names = []
for name in list_of_names:
    new_list_of_names.append(name.strip())
    
    
#TODO:Escribir los nombres extraidos en el archivo starting_letters    
for name in new_list_of_names:
    # Abre un archivo con el nombre correspondiente a cada nombre en la lista
    with open(f"{name}.txt", "w") as letter:
        # Escribe una carta personalizada para cada nombre, reemplazando el marcador de posición [name] con el nombre real
        letter.write(starting_letter.replace("[name]", name))
