#ARMANDO UNA MOCHILA DE EMERGENCIA hola


#Para formalizar las categorias se crea un diccionarios con categorias predeterminadas
Categorias = {1:'Higiene', 2:'Ropa',3: 'Botiquin',4: 'Alimentos no perecibles', 5:'Herramientas Basicas', 6: 'Dinero y documentos'}

#Una persona promedio puede cargar hasta 8 kilos, esto con el fin de que no ralentize cuando se necesite correr
#Ojo se puede editar para ver diferentes resultados
pesoMaximo = 5


def IngresarDatos():
  Objetos = []
  while True:
    try:
      nombre = input('Ingrese el nombre del objeto: ')
      peso = float(input('Ingrese el peso del objeto: '))
      valor = int(input('Ingrese el valor del objeto: '))
      print('Las categorias son: ')
      for i in Categorias.keys():
        print(i, Categorias[i])
      cat = int(input('Ingrese la categoria del objeto: '))
      if cat < 1 or cat > 6:
        print('Categoria no valida')
        continue
    except:
      print('Error en los datos ingresados')
      continue
    
    categoria = Categorias[cat]
    Objetos.append({'NOMBRE': nombre, 'PESO': peso, 'VALOR': valor, 'CATEGORIA':categoria})
    opcion = input('Desea ingresar otro objeto? (s/n): ')
    if opcion.lower() == 'n':
      print('v'*40)
      break
  return Objetos
'''
objetos = IngresarDatos()

if objetos:
  print('Los objetos ingresados son: ')
  for objeto in objetos:
    print(objeto)
else:
  print('No se ingresaron objetos')
'''




def SolucionBruta(PRODUCTOS = []):
   if(len(PRODUCTOS) == 0):
     return []
   mejor_valor = 0
   mejor_peso = 0
   mejor_combinacion = []

   def obtener_combinaciones(elementos, k):
     # Si el tamaño del grupo es 0, devolvemos una lista con un grupo vacío
     if k == 0:
         return [[]]

     combinaciones = []

     # Recorremos los elementos
     for i in range(len(elementos)):
         actual = elementos[i]

         # Obtenemos el resto de la lista para no repetir elementos
         resto = elementos[i + 1:]

         # Llamamos a la función de forma recursiva
         for combinacion_resto in obtener_combinaciones(resto, k - 1):
             combinaciones.append([actual] + combinacion_resto)

     return combinaciones


   #Bucle anidado 
   for r in range(1, len(PRODUCTOS) + 1):
           #Este bucle recorre  las combinaciones de tamaño n 
           for combinacion in obtener_combinaciones(PRODUCTOS, r):

               peso_total = sum(objeto['PESO'] for objeto in combinacion)
               valor_total = sum(objeto['VALOR'] for objeto in combinacion)

               # Verificar si entra en la mochila
               if peso_total <= pesoMaximo:
                   # Verificar si es mejor que la solución anterior
                   if valor_total > mejor_valor:
                       mejor_valor = valor_total
                       mejor_peso = peso_total
                       mejor_combinacion = combinacion

   print("Mejor combinación:")
   for objeto in mejor_combinacion:
       print(objeto)
   print(f"Peso total: {mejor_peso}")
   print(f"Valor total: {mejor_valor}")
   print("xvx"*15)


Objetosde = [
  {'NOMBRE': 'Shampoo', 'PESO': 1, 'VALOR': 5, 'CATEGORIA': 'Higiene'},
  {'NOMBRE': 'Jabón', 'PESO': 2, 'VALOR': 7, 'CATEGORIA': 'Higiene'},
  {'NOMBRE': 'Pantalones', 'PESO': 3, 'VALOR': 10, 'CATEGORIA': 'Ropa'},
  {'NOMBRE': 'Camisa', 'PESO': 2, 'VALOR': 10, 'CATEGORIA': 'Ropa'},
  {'NOMBRE': 'Ibuprofeno', 'PESO': 0.100, 'VALOR': 20, 'CATEGORIA': 'Botiquin'},
  {'NOMBRE': 'Aspirina', 'PESO': 0.1, 'VALOR': 20, 'CATEGORIA': 'Botiquin'},
  {'NOMBRE': 'Arroz', 'PESO': 4, 'VALOR': 15, 'CATEGORIA': 'Alimentos no perecibles'},
  {'NOMBRE': 'Galletas Proteicas', 'PESO': 0.25, 'VALOR': 12, 'CATEGORIA': 'Alimentos no perecibles'},
  {'NOMBRE': 'Cuerda', 'PESO': 2, 'VALOR': 8, 'CATEGORIA': 'Herramientas Basicas'},
  {'NOMBRE': 'Encendedor', 'PESO': 0.5, 'VALOR': 7, 'CATEGORIA': 'Herramientas Basicas'},
  {'NOMBRE': 'Billetera', 'PESO': 0.5, 'VALOR': 8, 'CATEGORIA': 'Dinero y documentos'},
  {'NOMBRE': 'Venda', 'PESO': 2, 'VALOR': 15, 'CATEGORIA': 'Botiquin'},
  {'NOMBRE': 'Alcohol', 'PESO': 1, 'VALOR': 20, 'CATEGORIA': 'Botiquin'},
  {'NOMBRE': 'Agua', 'PESO': 1, 'VALOR': 15, 'CATEGORIA': 'Alimentos no perecibles'},
  {'NOMBRE': 'Cuchillo', 'PESO': 0.5, 'VALOR': 5, 'CATEGORIA': 'Herramientas Basicas'},
  {'NOMBRE': 'Tijera', 'PESO': 0.5, 'VALOR': 5, 'CATEGORIA': 'Herramientas Basicas'}
]

SolucionBruta(Objetosde)
    
