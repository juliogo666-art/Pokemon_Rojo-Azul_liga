#######################################################################################

# Descripción del Ejercicio

#######################################################################################

# Queremos ayudar a un usuario a ganar la liga pokemon.

# El usuario tiene 6 pokemons y sus rivales tambien.

# De entre 6 pokemon --> elegir cual es el mejor contra 1 pokemon especifico

## Que tenemos

# Datos pokemon

# Especificaciones de pokemon

# Ataques

# Estadisticas

# tipos

# Matriz de tipos

# Información en internet de otra gente que ya ha ganado

# Que podemos pedir al usuario

# Sus 6 pokemon

# Sus rivales

## Cual es el flujo

# 1.- Inputs

# Tus 6 pokemons a elegir

# pokemon a batir

# 2.- Esto va a un DB

# Consulta los datos de los pokemon

# Saca los datos necesarios

# 3.- Vectorizados la información

# 4.- Inferencia del modelo

# 5.- Mostramos Reusltados

## Que resticciones sabemos que tenemos con nuestra información actual.

# 1.- No sabes los movimientos de los pokemons.

# 2.- ¿ Que combate habrá despues ?

# 3.- El orden en que el rival va a sacar los pokemons.

# 4.- Objetos mágicas

# 5.- Importancia de que pokemon sacar

# 6.- Puede haber el caso de que ninguna opción es buena.

# Definición del world packaging

## Preparación DB

# 1.- Mirar la DB

# 2.- Gestionar null o vacios

# 3.- Decidir que se hace con las variables categoricas

# 4.- Normalizar valores todos a la misma cosa.

# 5.- Feature Engineering

# 6.- DB Final

## Vectorización

# ( Siguiente clase )

# 1.- Comparar los datos de entrada con DB

# 2.- Transformar estos datos a agrupaciones especificas

# 3.- Limpiar el vector a lo que le interesa el modelo

## Modelo

# 1.- Decidir modelo

# 1.- En clase hemos visto unos cuantos.

# 2.- Hemos decidido todos juntos que el collaborative filtering no serviría en esta ocasion

# 3.- Pero que Content based y Matrix factorization sirven.

# 4.- Vamos a provar los dos modelos.

## Empollon AKA --> Benchmarking de tendencias.
