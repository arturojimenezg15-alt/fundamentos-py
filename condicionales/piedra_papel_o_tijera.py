P = 1
PA = 2
T = 3

if 1 > 3:
    print("Piedra gana a tijera")
elif 2 > 1:
    print("Papel gana a piedra")
elif 3 < 2:
    print("Tijera gana a papel")
elif 1 == 2:
    print("Piedra empata con papel")
elif 3 >= 2:
    print("Tijera gana a papel")
elif 1 <= 3:
    print("Piedra gana a tijera")
else:
    print("Ninguna de las condiciones se cumplio")  