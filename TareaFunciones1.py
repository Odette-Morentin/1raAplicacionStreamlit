import streamlit as st
import BibliotecaFuncionesStreamlit as bf

# Configuración del menú principal
menu_principal = ["Inicio","Función de saludo simple", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento", "Suma de una lista de números", "Función con valores predeterminados", "Números pares e impares", "Multiplicación con *args", " Información de una persona con **kwargs", "Calculadora flexible"]
opcion_seleccionada = st.sidebar.selectbox("Opciones", menu_principal)
match opcion_seleccionada:


    # Código de la página principal
    case "Inicio":
        bf.titulo_bonito("Bienvenido a mi aplicación de streamlit","#8e44ad")
        bf.subtitulo_bonito2("Ingenieria en computación inteligente","#f943e5")
        bf.subtitulo_bonito3("3b","#8e44ad")
        st.image("LOGO.png",use_column_width=True)
        

    #Código y formato de la opción de saludo simple
    case "Función de saludo simple":
        bf.titulo_bonito("Función de saludo simple", "#fb1310")
        nombre_saludo = st.text_input("Ingresa un nombre")
        if nombre_saludo:
            st.write(bf.saludo(nombre_saludo))


    #Código y formato de la opción de suma
    case "Suma de dos números":
        bf.titulo_bonito("Suma de dos números","#53b932")
        num1_suma = st.number_input("Ingresa  un número")
        num2_suma = st.number_input("Ingresa otro número")
        if num1_suma and num2_suma:
            st.write(f"La suma es: {bf.sumar(num1_suma,num2_suma)}")


    #Código y formato de la opcioón de área del triángulo
    case "Área de un triángulo":
        bf.titulo_bonito(" Área de un triángulo","#3238b9")
        base = st.number_input("Ingresa la base del triángulo", min_value=0.0)
        altura = st.number_input("Ingresa la altura del triángulo",min_value=0.0)
        if base and altura:
            st.write(f"El área del tríangulo es: {bf.calcular_area_triangulo(base,altura)}")


    #Código y formato de la opción de calculadora con descuento
    case "Calculadora de descuento":
        bf.titulo_bonito("Calculadora de descuento","#b9328a")
        precio = st.number_input("Ingresa el precio del producto",min_value=0.0)
        # Configuración de valores por defecto
        descuento = st.number_input("Ingresa el descuento del producto(opcional)",min_value=0.0,value=10.0)
        impuesto =  st.number_input("Ingresa el impuesto del producto(opcional)",min_value=0.0,value=16.0)
        if precio :
            precio_final = bf.calcular_precio_final(precio, descuento, impuesto)
            st.write(f"El precio final con el descuento más impuesto es: {precio_final}")


    #Código y formato de la opción de conversión de unidades
    case "Suma de una lista de números":
        bf.titulo_bonito(" Suma de una lista de números","#48a79e")
        try:
            numeros_sumar = st.text_input("Ingresa una lista de números separados por comas:")
            if  numeros_sumar:
                st.write(f"La suma de la lista es: {bf.sumar_lista(numeros_sumar)}")
        except ValueError:
            st.error("Error: Sólo puedes ingresar números")


    #Código y formato de la opción de valores predeterminados
    case "Función con valores predeterminados":
        bf.titulo_bonito("Función con valores predeterminados","#9ebb3b")
        nombre = st.text_input("Ingresa el nombre del producto: ")
        # Configuración de valores por defecto
        cantidad =  st.number_input("Ingresa la cantidad del producto", min_value=0,value=1,step=1)
        precio = st.number_input("Ingresa el precio del producto",min_value=0.0,value=10.0,step=.5)
        if nombre and cantidad and precio:
            st.write(bf.producto(nombre,cantidad,precio))


    #Código y formato de la opción de números pares e impares
    case "Números pares e impares":
        bf.titulo_bonito("Números pares e impares","#3bbb71")
        try: 
            numeros_pares_impares = st.text_input("Ingresa una lista de números separados por comas")
            if numeros_pares_impares:
                # Descompactar el resultado de la función
                lista_pares,lista_impares = bf.numeros_pares_e_impares(numeros_pares_impares)
                st.write(f"Los números pares son: {lista_pares}")
                st.write(f"Los números impares son: {lista_impares}")
        except ValueError:
            st.error("Ingresa números válidos")
    
    #Código y formato de la opción multiplicación
    case "Multiplicación con *args":
        bf.titulo_bonito("Multiplicación con *args","#d07d2a")
        try:
            numeros_multiplicar = st.text_input("Ingresa los números que quieras multiplicar: ")
            if not numeros_multiplicar:
                st.write(f"El producto es: {bf.multiplicar_todos()}")
            if numeros_multiplicar:
                # Pasar str a float
                lista_multiplicar = [float(num) for num in numeros_multiplicar.split(",")]
                st.write(f"El producto de los número es: {bf.multiplicar_todos(*lista_multiplicar)}")
        except ValueError:
            st.error("Ingresa números válido")

    
    # Código y formato de la opción de la información de una persona
    case " Información de una persona con **kwargs":
        bf.titulo_bonito(" Información de una persona con **kwargs","#15be79")
        informacion = st.text_input("Escribe la información personal, ejemplo: Nombre=Odette,Edad=18")
        if informacion:
            # Pasar str a diccionario
            diccionario_info = {}
            for item in informacion.split(","):
                if "=" in item:
                    clave,valor = item.split("=")
                    diccionario_info[clave] = valor
            bf.informacion_personal(**diccionario_info)


    # Código y formato de la calculadora
    case "Calculadora flexible":
        bf.titulo_bonito("Calculadora flexible","#ca4c8d")
        num1_calculadora = st.number_input("Ingresa un número",min_value=0.0)
        num2_calculadora = st.number_input("Ingresa otro número",min_value=0.0)
        # Menú de opciones
        opciones = ["Suma","Resta","Multiplicación","División"]
        opcion = st.sidebar.selectbox("Opciones: ", opciones)
        if num1_calculadora:
            st.write(f"El resultado de la {opcion} es: {bf.calculadora_flexible(num1_calculadora,num2_calculadora,opcion)}")