paquete1 = [40, 35, 30]
paquete2 = [50, 50, "hola"]
paquete3 = [0, 51, "texto"]

# TODO 1: retornar el subtotal correcto.
def calcular_subtotal(total_paginas, precio_pagina):
    subtotal = total_paginas * precio_pagina
    return subtotal

paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]

PRECIO_PAGINA = 2
PORCENTAJE_DESCUENTO = 0.10

total_paginas = 0
cantidad_paquetes_aceptados = 0

for indice in range(len(paquetes)):
    print(f"Paquete actual: {paquetes[indice]}")

    try:
        paginas = int(input("Cantidad de páginas (1 a 50): "))
    except ValueError:
        print("Error: debes escribir un número entero. Paquete omitido.")
        continue

    # TODO 2:
    # Si paginas está fuera del rango 1 a 50,
    # mostrar un mensaje y omitir este paquete con continue.
    if paginas < 1 or paginas > 50:
        print("Error: la cantidad de páginas debe estar entre 1 y 50. Paquete omitido.")
        continue


    # TODO 3:
    # Acumular las páginas y aumentar los paquetes aceptados.
    total_paginas += paginas
    cantidad_paquetes_aceptados += 1

subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
descuento = 0

# TODO 4:
# Aplicar 10% de descuento solo si total_paginas supera 100.
if total_paginas > 100:
    descuento = subtotal * PORCENTAJE_DESCUENTO
    returned_total = subtotal - descuento
else:
    returned_total = subtotal


print("Resumen del pedido: {paquetes_aceptados} paquetes aceptados, {total_paginas} páginas, subtotal: ${subtotal:.2f}, descuento: ${descuento:.2f}, total a pagar: ${returned_total:.2f}".format(
    paquetes_aceptados=cantidad_paquetes_aceptados,
    total_paginas=total_paginas,
    subtotal=subtotal,
    descuento=descuento,
    returned_total=returned_total
))
"""
 TODO 5: Mostrar un mensaje si no se aceptó ningún paquete. 
 E imprimir el resumen del pedido con la cantidad de paquetes aceptados, 
 total de páginas, subtotal, descuento y total a pagar.
"""





        