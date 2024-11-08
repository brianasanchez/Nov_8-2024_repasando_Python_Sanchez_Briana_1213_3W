print(" ") # print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio

def tri_recursion(k):# definiendo la funcion 
  if(k > 0): # abriendo if
    result = k + tri_recursion(k - 2) # haciendo secuencia de operaciones
    print(result)# print imprimiendo resultado
  else: # se ejecuta si la parte es falsa
    result = 0 # dando resultado
  return result # terminando ejecucion

print("\n\nRecursion Example Results") # print imprimiendo
tri_recursion(100) # numero de secuencia

print(" ") # print imprime un espacio