import streamlit as st

#Función de saludo simple
def saludo(nombre:str)->str: 
    return f"Hola, {nombre}."

#Función de suma de dos números
def sumar(num1:int,num2:int)->float: 
    return num1 + num2

#Función del área de un triángulo
def calcular_area_triangulo(base:int,altura:int)->float: 
    return (base*altura)/2

#Función que calcula descuentos
def calcular_precio_final(precio:int,descuento=10,impuesto=16)->float: 
    descuento_final =  precio * (descuento / 100)
    precio -=  descuento_final
    impuesto_final = precio * (impuesto / 100)
    return precio + impuesto_final

#Función que suma una lista de números
def sumar_lista(lista:list)->int: 
    lista_numeros = [float(num) for num in lista.split(",")] #Pasar str a float
    suma = 0
    for i in lista_numeros:
        suma =  suma + i
    return suma

#Función con valores predeterminados
def producto(nombre:str,cantidad=1,precio=10): 
    return f"{cantidad} {nombre} tienen un costo de {precio*cantidad} pesos"

#Función que separa los números pares e impares
def numeros_pares_e_impares(lista:list)->list: 
    lista = [float(num) for num in lista.split(",")] #Pasar str a float
    pares = []
    impares = []
    for i in  lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

#Función de la multiplicación con *args
def multiplicar_todos(*nums:int)->int:
    if len(nums) == 0:
        return 1 
    else:
        return nums[0] * multiplicar_todos(*nums[1:]) 

#Función de la información de una persona con **kwargs
def informacion_personal(**info:str)->dict: 
    for clave, valor in info.items():
        st.write(f"{clave} : {valor}") #Recorrer un diccionario

# Función de calculadora flexible
def calculadora_flexible(num1:int,num2:int,operacion:str)->int: 
    if operacion == "Suma":
        return num1 + num2
    elif  operacion ==  "Resta":
        return num1-num2
    elif operacion == "Multiplicacion" :
        return num1*num2
    else:
        try:
            return num1/num2
        except ZeroDivisionError:
            st.error("Error de división entre 0")

#Función para poner títulos
def titulo_bonito(titulo:str,color:str)->str:
    html_code = f""" <h1 style="color: {color}; text-align: center;">{titulo}</h1>"""
    st.markdown(html_code, unsafe_allow_html=True)

#Función para poner subtítulos nivel 2
def subtitulo_bonito2(subtitulo:str,color:str)->str:
    html_code = f"""
    <h2 style="color: {color}; text-align: center;">{subtitulo}</h2>
    """
    st.markdown(html_code, unsafe_allow_html=True)

#Función para subtitulos nivel 3
def subtitulo_bonito3(subtitulo:str,color:str)->str:
    html_code = f"""
    <h3 style="color: {color}; text-align: center;">{subtitulo}</h2>
    """
    st.markdown(html_code, unsafe_allow_html=True)