# **Gestión del Proyecto: Estacionamiento ACO**

## **Descripción del Proyecto**
El proyecto tiene como objetivo principal optimizar la asignación de espacios de estacionamiento utilizando algoritmos avanzados de optimización como la Optimización por Colonias de Hormigas (ACO). Se enfoca en resolver problemas relacionados con la movilidad urbana y el uso eficiente de los recursos, haciendo uso de herramientas tecnológicas como **Google Maps API** y **FastAPI**.

El sistema busca minimizar el tiempo y el consumo de recursos para los usuarios, apoyándose en cálculos de rutas, distancias y diseño óptimo de estacionamientos. Este enfoque tiene un impacto positivo en la sociedad al reducir la congestión vehicular y la huella ambiental.

---

## **Componentes del Proyecto**
1. **Backend**:
   - Implementado en **Python** con **FastAPI**.
   - Incluye algoritmos de optimización (ACO) y comunicación con la API de Google Maps.
2. **Frontend**:
   - Prototipado con **FlutterFlow**, proporcionando una experiencia interactiva y amigable para el usuario.
3. **Integración**:
   - Uso de Google Maps API para la geolocalización y cálculo de rutas.
   - Base de datos diseñada para almacenar ubicaciones y optimizaciones en tiempo real.

---

## **Aspectos Técnicos y Buenas Prácticas**
El proyecto cumple con varios aspectos fundamentales de buenas prácticas de programación, detallados a continuación:

### **1. Herencia y Polimorfismo**
- Implementación modular basada en clases, permitiendo la reutilización y extensibilidad del código.

### **2. Patrones de Diseño**
- Uso de patrones como **Factory** y **Singleton** para la creación y manejo de instancias dentro del sistema.

### **3. Manejo de Errores**
- Gestión de excepciones en **FastAPI** para garantizar robustez y evitar fallos en tiempo de ejecución.

### **4. Punteros y Manejo de Memoria (Simulación en Python)**
- Aunque Python no maneja punteros directamente, se asegura la optimización del uso de recursos a través de gestión de memoria eficiente con herramientas de monitoreo.

### **5. Multiprocesamiento**
- Uso de librerías como `asyncio` para garantizar concurrencia en operaciones como la consulta de rutas y cálculos intensivos.

---

## **Documentación y Referencias**
### **Revisión de Material Bibliográfico**
El proyecto se basa en conceptos de:
- **Algoritmos de Optimización por Colonias de Hormigas (ACO)**:
  - "Ant Colony Optimization" por Marco Dorigo.
  - Artículos de investigación recientes relacionados con optimización en sistemas de tráfico.
- **Google Maps API**:
  - Documentación oficial de Google Maps API.
  - Ejemplos prácticos para integración en sistemas de estacionamientos.
- **FastAPI**:
  - Documentación oficial de FastAPI.
  - Recursos externos sobre desarrollo de APIs RESTful en Python.

### **Código de Terceros y Librerías**
- **FastAPI** (MIT License): Framework para creación de APIs.
- **Google Maps API**: Servicios para geolocalización y mapas.
- **NumPy**: Cálculos matemáticos necesarios para optimización.

El proyecto respeta los derechos de autor de todas las herramientas y librerías utilizadas, incluyendo las licencias correspondientes en el código fuente.

---

## **Guía Técnica**
### **Requisitos del Sistema**
- **Python** 3.10 o superior.
- Dependencias especificadas en `requirements.txt`:
  - FastAPI
  - Google Maps API
  - NumPy
  - Uvicorn

### **Pasos para Compilar y Ejecutar**
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/imlosing07/proyecto-estacionamientos-ACO.git
   cd proyecto-estacionamientos-ACO
2. **Crear un Entorno Virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
3. **Instalar Dependencias:**:
   ```bash
    pip install -r requirements.txt
4. **Iniciar el Servidor Backend:**:
   ```bash
    uvicorn main:app --reload
5. **Acceder al Frontend:**:
Configurar FlutterFlow según el manual de usuario disponible en la documentación técnica.

## **Diagrama UML**

### **Diseño General**

Incluye diagramas que reflejan los siguientes aspectos:

1. **Arquitectura del Sistema**:
   - Relación entre módulos (backend, API, y frontend).
2. **Modelo de Datos**:
   - Estructura de la base de datos.
3. **Flujo de Información**:
   - Secuencia de interacciones entre los usuarios y el sistema.

*(El diagrama UML completo se encuentra en la carpeta `docs/uml`.)*

---

## **Responsabilidad Social**

El proyecto aborda problemas reales relacionados con:

- **Movilidad Urbana**:
  - Reducción del tiempo y estrés para los conductores al encontrar espacios de estacionamiento.
- **Sostenibilidad**:
  - Disminución de la huella de carbono mediante el uso eficiente de rutas y recursos.


## **Licencia**
Este proyecto se distribuye bajo la licencia MIT.