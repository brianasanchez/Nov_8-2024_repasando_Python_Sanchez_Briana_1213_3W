print(" ") # print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio

nota = float(input("Introduce tu nota: ")) # pide que ingreses tu nota

if 0 <= nota < 5: #abriedno if
    print("reprobado") # print imprime texto
elif 5 <= nota < 6: # abriendo elif
    print("pasate") # print imprime texto
elif 6 <= nota < 7: # abriendo elif
    print("bien") # print imprime texto
elif 7 <= nota < 9: # abriendo elif
    print("muy bien") # print imprime texto
elif 9 <= nota <= 10: # abriendo elif
    print("demasiado bien ") # print imprime texto
else: # ejecuta la parte si es falsa
    print("no valido") # print imprime texto

print(" ") # print imprime un espacio