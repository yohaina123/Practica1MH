# Práctica 1 – Planificación de Exámenes mediante Búsqueda Local

## Descripción

Hemos implementado un sistema para la planificación de exámenes universitarios utilizando técnicas de búsqueda local.  

Se genera una solución inicial mediante una heurística constructiva y luego se mejora utilizando dos algoritmos:

- First Improvement
- Best Improvement
El objetivo es minimizar los conflictos entre exámenes de los estudiantes.

## Requisitos

El proyecto está desarrollado en python utilizando el entorno anaconda y las siguientes librerías:

- numpy
- pandas
- matplotlib

Si no están instaladas, se pueden instalar con:

bash :    pip install numpy pandas matplotlib

Ejecución

Para ejecutar el programa:

python main.py

El programa realizará los siguientes pasos:

Generar una instancia del problema
Construir una solución inicial
Aplicar los algoritmos de búsqueda local
Mostrar los resultados por consola
Generar gráficas de resultados

Resultados

El programa genera dos gráficos automáticamente en la carpeta:

imagenes/
costes.png : comparación del coste de los algoritmos
tiempos.png : comparación del tiempo de ejecución