# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_cm = float(input('Digite o comprimento da aresta do quadrado em cm:'))

lado_m = lado_cm / 100

area_cm2 = lado_cm ** 2

area_m2 = lado_m ** 2

if area_cm2 >= 100:

    print(f'O dobro do valor informado do quadrado tem a área de {2 * area_m2:.2f} m²')

else:
    print(f'O dobro do valor informado do quadrado tem a área de {2 * area_cm2} cm²')