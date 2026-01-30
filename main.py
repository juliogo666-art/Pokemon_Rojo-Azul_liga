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

#######################################################################################
# 1.- Importar librerias
#######################################################################################

import pandas as pd

# 1.- Cargar CSV
df = pd.read_csv("all_pokemon.csv")

# 2.- Mostrar los primeros 5 registros
# df.head()

# 3.- Mostrar los nombres de las columnas
# df.columns

#######################################################################################
# 2.- Limpieza y preparacion de datos
#######################################################################################

# Miramos la DB
# print(df.isnull().sum())

# 1.- Gestionar null o vacios

df_limpio = df.fillna("Nada")
# print(df_limpio.isnull().sum())

#######################################################################################
# 3.- Añadimos nuestros pokemons
#######################################################################################

decision_equipo_nuevo = input("Quieres añadir un nuevo equipo? (S/N): ")

if decision_equipo_nuevo == "S":
    equipo = []

    def pokemon_team():
        pokemon = input("Introduce tu pokemon: ")
        return pokemon

    numero_pokemon = int(input("Introduce el numero de pokemon: "))

    for poke in range(numero_pokemon):
        equipo.append(pokemon_team())

    print(equipo)

    # Convertimos la lista a un DataFrame de pandas
    df_equipo = pd.DataFrame(equipo, columns=["Nombre"])
    # Guardamos el DataFrame en un archivo CSV
    df_equipo.to_csv("Nuestro_equipo.csv", index=False)

else:
    print("No se ha añadido equipo nuevo")
    print("Nuestro equipo es: ", pd.read_csv("Nuestro_equipo.csv"))


#######################################################################################
# 4.- Equipo de nuestro rival
#######################################################################################

print("Rivales disponibles: ", pd.read_csv("Equipo_rival.csv")["Entrenador"].unique())
rival = input("Que rival enfrentamos? ")

if rival in pd.read_csv("Equipo_rival.csv")["Entrenador"].unique():
    print("Rival encontrado")
    print(
        pd.read_csv("Equipo_rival.csv").loc[
            pd.read_csv("Equipo_rival.csv")["Entrenador"] == rival
        ]
    )
else:
    print("Rival no encontrado")


#############################
# Nuevo rival
#############################

nuevo_rival = input("Quieres agregar un nuevo rival? (S/N): ")

if nuevo_rival == "S":
    Nombre_rival = input("Introduce el nombre de tu rival: ")

    equipo_rival = []
    niveles = []

    def pokemon_rival():
        pokemon = input("Introduce tu pokemon: ")
        return pokemon

    numero_pokemon_rival = int(input("Introduce el numero de pokemon: "))

    for poke in range(numero_pokemon_rival):
        equipo_rival.append(pokemon_rival())
        niveles.append(int(input("Introduce el nivel de tu pokemon: ")))

    print(equipo_rival)
    print(niveles)

    # Convertimos la lista a un DataFrame de pandas
    df_equipo_rival = pd.DataFrame({"pokemon": equipo_rival, "nivel": niveles})

    # Guardamos el DataFrame en un archivo CSV
    df_equipo_rival.to_csv("Equipo_rival_" + Nombre_rival + ".csv", index=False)

else:
    print("No se ha añadido rival nuevo")

#######################################################################################
# 5.- Cargamos datos de equipos
#######################################################################################

df_equipo = pd.read_csv("Nuestro_equipo.csv")
df_all_pokemon = pd.read_csv("all_pokemon.csv")
