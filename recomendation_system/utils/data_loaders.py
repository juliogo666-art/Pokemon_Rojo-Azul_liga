import pandas as pd
import os


def load_pokemon_data():
    # 1.- Cargar CSV
    df = pd.read_csv("recomendation_system/data/all_pokemon.csv")

    # 2.- Mostrar los primeros 5 registros
    # df.head()

    # 3.- Mostrar los nombres de las columnas
    # df.columns

    return df


#######################################################################################


def add_pokemon_team():
    decision_equipo_nuevo = input("Quieres añadir un nuevo equipo? (S/N): ")

    if decision_equipo_nuevo == "S":
        equipo = []

        def pokemon_team():
            pokemon = input("Introduce tu pokemon: ")
            return pokemon

        numero_pokemon = int(
            input("¿Cuántos pokemons tiene el equipo? (Introduce un número): ")
        )

        for poke in range(numero_pokemon):
            equipo.append(pokemon_team())

        print(equipo)

        # Convertimos la lista a un DataFrame de pandas
        df_equipo = pd.DataFrame(equipo, columns=["Nombre"])
        # Guardamos el DataFrame en un archivo CSV
        df_equipo.to_csv("recomendation_system/data/Nuestro_equipo.csv", index=False)

    else:
        print("No se ha añadido equipo nuevo")
        print(
            "Nuestro equipo es: ",
            pd.read_csv("recomendation_system/data/Nuestro_equipo.csv"),
        )


#######################################################################################


def load_rival_team():
    print("Podemos agregar un rival nuevo o enfrentarnos a uno ya existente")
    nuevo_rival = input("Quieres agregar un nuevo rival? (S/N): ")

    if nuevo_rival == "S":
        Nombre_rival = input("Introduce el nombre de tu rival: ")

        equipo_rival = []
        niveles = []

        def pokemon_rival():
            pokemon = input("Introduce tu pokemon: ")
            return pokemon

        numero_pokemon_rival = int(
            input("¿Cuántos pokemons tiene el rival? (Introduce un número): ")
        )

        for poke in range(numero_pokemon_rival):
            equipo_rival.append(pokemon_rival())
            niveles.append(int(input("Introduce el nivel de tu pokemon: ")))

        print(equipo_rival)
        print(niveles)

        # Convertimos la lista a un DataFrame de pandas
        df_equipo_rival = pd.DataFrame(
            {"Entrenador": Nombre_rival, "pokemon": equipo_rival, "nivel": niveles}
        )

        # Guardamos el DataFrame en un archivo CSV
        # Usamos mode='a' para añadir sin borrar lo anterior, y header=False si el archivo ya existe
        file_path = "recomendation_system/data/Equipo_rival_nuevos.csv"
        file_exists = os.path.isfile(file_path)

        df_equipo_rival.to_csv(
            file_path,
            index=False,
            mode="a",
            header=not file_exists,
        )

    else:
        print("No se ha añadido rival nuevo")
        rival_a_enfrentar = input(
            "Quieres enfrentar rival de la liga o nuevo? (Liga/Nuevo): "
        )

        if rival_a_enfrentar == "Liga":
            print(
                "Rivales disponibles: ",
                pd.read_csv("recomendation_system/data/Equipo_rival_liga.csv")[
                    "Entrenador"
                ].unique(),
            )
            rival = input("Que rival enfrentamos? ")

            if (
                rival
                in pd.read_csv("recomendation_system/data/Equipo_rival_liga.csv")[
                    "Entrenador"
                ].unique()
            ):
                print("Rival encontrado")
                print(
                    pd.read_csv("recomendation_system/data/Equipo_rival_liga.csv").loc[
                        pd.read_csv("recomendation_system/data/Equipo_rival_liga.csv")[
                            "Entrenador"
                        ]
                        == rival
                    ]
                )
            else:
                print("Rival no encontrado")

        elif rival_a_enfrentar == "Nuevo":
            file_path = "recomendation_system/data/Equipo_rival_nuevos.csv"

            if os.path.exists(file_path):
                print(pd.read_csv(file_path))
                rival_nuevo = input("Que rival enfrentamos? ")

                if rival_nuevo in pd.read_csv(file_path)["Entrenador"].unique():
                    print("Rival encontrado")
                    print(
                        pd.read_csv(file_path).loc[
                            pd.read_csv(file_path)["Entrenador"] == rival_nuevo
                        ]
                    )
                else:
                    print("Rival no encontrado")
            else:
                print("No hay rivales nuevos registrados todavía.")

        else:
            print("Opcion no valida")
