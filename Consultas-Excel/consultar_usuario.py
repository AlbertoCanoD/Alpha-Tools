import openpyxl

# Carga del excel
excel = openpyxl.load_workbook(filename='C:\ejemplo.xlsx') #//TODO no me carga directamente desde la carpeta

# Carga de la hoja
hoja = excel['Ramas']

# Se imprime una celda en concreto de la Hoja
celda = 'A1'
print(hoja[celda].value)

for row in hoja.iter_rows(min_row=2, max_row=4):
    # Imprime el valor de cada celda de la fila
    for cell in row:
        print(cell.value)

valores_fila = [cell.value for cell in row]

# Concatena los valores de la lista en una cadena de texto, separando cada elemento con una coma
row_string = ','.join(values)

print(row_string)

# Concatena los valores de la lista en una cadena de texto, separando cada elemento con un espacio en blanco
row_string = ' '.join(values)

# Concatena los valores de la lista en una cadena de texto, separando cada elemento con una tabulación
row_string = '\t'.join(values)

