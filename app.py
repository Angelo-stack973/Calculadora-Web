import math
import streamlit as st

# 1. Configuración del menú en la barra lateral
st.sidebar.title("📌 MENÚ DE OPERACIONES")
opcion = st.sidebar.radio(
    "Selecciona la herramienta:",
    ["Calculadora Básica", "Cálculos Avanzados", "Cálculo de Porcentajes", "Cálculo de áreas"]
)

# ---------------------------------------------------------
# OPCIÓN 1: CALCULADORA BÁSICA
# ---------------------------------------------------------
if opcion == "Calculadora Básica":
    st.title("🧮 Calculadora Básica")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Número 1:", value=None, placeholder="Ingresa un número...")
    with col2:
        num2 = st.number_input("Número 2:", value=None, placeholder="Ingresa un número...")
    
    # Menú de operaciones simples
    operacion = st.selectbox("Operación:", ["SUMA", "RESTA", "MULTIPLICACIÓN", "DIVISIÓN"])
    
    if st.button("CALCULAR"):
        if num1 is None or num2 is None:
            st.warning("⚠️ Ingresa ambos números para continuar.")
        else:
            if operacion == "SUMA":
                res = num1 + num2
            elif operacion == "RESTA":
                res = num1 - num2
            elif operacion == "MULTIPLICACIÓN":
                res = num1 * num2
            elif operacion == "DIVISIÓN":
                res = "Error (división entre cero)" if num2 == 0 else num1 / num2
            
            st.success(f"RESULTADO: {res}")

# ---------------------------------------------------------
# OPCIÓN 2: CÁLCULOS AVANZADOS
# ---------------------------------------------------------
elif opcion == "Cálculos Avanzados":
    st.title("🔬 Operaciones Avanzadas")
    
    # Selección del tipo de cálculo avanzado
    tipo_calculo = st.selectbox(
        "Tipo de operación avanzada:",
        ["POTENCIA Y RAÍZ", "FUNCIONES TRIGONOMÉTRICAS", "LOGARITMOS", "FACTORIAL"]
    )
    
    # Formulario dinámico según la opción seleccionada
    if tipo_calculo == "POTENCIA Y RAÍZ":
        base = st.number_input("Base ($x$):", value=None, placeholder="Ingresa la base...")
        exponente = st.number_input("Exponente ($n$):", value=None, placeholder="Ingresa el exponente...")
        
        if st.button("Calcular"):
            if base is None or exponente is None:
                st.warning("⚠️ Completa los campos.")
            else:
                st.success(f"Resultado {base}^{exponente}: {math.pow(base, exponente)}")

    elif tipo_calculo == "FUNCIONES TRIGONOMÉTRICAS":
        angulo = st.number_input("Ángulo en grados (°):", value=None, placeholder="Escribe el ángulo 'α'...")
        
        if st.button("Calcular"):
            if angulo is None:
                st.warning("⚠️ Ingresa un ángulo.")
            else:
                rad = math.radians(angulo)
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Seno (sin α)", f"{math.sin(rad):.4f}")
                col_b.metric("Coseno (cos α)", f"{math.cos(rad):.4f}")
                col_c.metric("Tangente (tan α)", f"{math.tan(rad):.4f}")

    elif tipo_calculo == "LOGARITMOS":
        val = st.number_input("Coloca un valor:", value=None, placeholder="Ingresa un valor positivo...")
        a = st.number_input("Base del logaritmo (a):", value=None, placeholder="Ingresa una base positiva...", min_value=0.0)

        if st.button("Calcular"):
            if val is None or val <= 0:
                st.error("⚠️ El valor debe ser mayor que cero.")
            elif a is None or a <= 0:
                st.error("⚠️ La base del logaritmo debe ser mayor que cero.")
            else:
                col1, col2, col3 = st.columns(3)
                col1.metric("Logaritmo Natural (ln)", f"{math.log(val):.4f}")
                col2.metric("Logaritmo Base 10", f"{math.log10(val):.4f}")
                col3.metric("Logaritmo de Base (a)", f"{math.log(val, a):.4f}")
    elif tipo_calculo == "FACTORIAL":
        n = st.number_input("Ingresa un valor para calcular:",step=1 , value=None, placeholder="Escribe el valor")

        if st.button("Calcular"):
            if n is None or n < 0:
                st.error("⚠️ Ingresa un número entero no negativo.")
            else:
                st.success(f"{int(n)}! = {math.factorial(int(n))}")
##OPCIÓN 3: CÁLCULO DE PORCENTAJES
if opcion == "Cálculo de Porcentajes":
    st.title("📊 Cálculo de Porcentajes")

    n1 = st.number_input("Ingrese el primer valor:", value=None, placeholder="Ingrese un valor...")
    n2 = st.number_input("Ingrese el segundo valor:", value=None, placeholder="Ingrese un valor...")
   
    if st.button("Calcular"):
        if n1 is None or n2 is None:
            st.warning("⚠️ Ingresa ambos valores para continuar.")
        else:
            T = n1 + n2
            if T == 0:
                st.warning("⚠️ El total no puede ser cero para calcular porcentajes.")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    px1 = (n1 / T) * 100
                    st.metric("El porcentaje del primer valor es: ", f"{px1}%")
                with col2:
                    px2 = (n2 / T) * 100
                    st.metric("El porcentaje del segundo valor es: ", f"{px2}%")
if opcion == "Cálculo de áreas":
    st.title("📐 Cálculo de Áreas")
    
    figura = st.selectbox(
        "Selecciona la figura geométrica:",
        ["Rectángulo", "Círculo", "Triángulo"]
    )
    
    if figura == "Rectángulo":
        base = st.number_input("Base del rectángulo:", value=None, placeholder="Ingresa la base...")
        altura = st.number_input("Altura del rectángulo:", value=None, placeholder="Ingresa la altura...")
        
        if st.button("Calcular Área"):
            if base is None or altura is None:
                st.warning("⚠️ Completa los campos.")
            else:
                area = base * altura
                st.success(f"Área del Rectángulo: {area}")

    elif figura == "Círculo":
        radio = st.number_input("Radio del círculo:", value=None, placeholder="Ingresa el radio...")
        
        if st.button("Calcular Área"):
            if radio is None:
                st.warning("⚠️ Ingresa el radio.")
            else:
                area = math.pi * (radio ** 2)
                st.success(f"Área del Círculo: {area:.4f}")

    elif figura == "Triángulo":
        base = st.number_input("Base del triángulo:", value=None, placeholder="Ingresa la base...")
        altura = st.number_input("Altura del triángulo:", value=None, placeholder="Ingresa la altura...")
        
        if st.button("Calcular Área"):
            if base is None or altura is None:
                st.warning("⚠️ Completa los campos.")
            else:
                area = (base * altura) / 2
                st.success(f"Área del Triángulo: {area}")

