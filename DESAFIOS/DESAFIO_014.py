# Escrava um programa que converta uma temperatura digitada em °C e converta para °F.

print(f"{'DESAFIO 014':=^25} \n"+"Conversor de Temperaturas")

TEMP_C = float(input("Infome a temperatura em °C: "))

print(f"A temperatura de {TEMP_C}°C corresponde a {( (TEMP_C * ( 9 / 5 )) + 32 ):.2f}°F !")
