import pandas as pd

#######################################################################################

from recomendation_system.utils.data_loaders import (
    load_pokemon_data,
    add_pokemon_team,
    load_rival_team,
)
from recomendation_system.utils.data_cleaning import gestion_null_o_vacios

#######################################################################################

# 1.- Cargar CSV
df = load_pokemon_data()

# 2.- Limpieza y preparacion de datos
df_limpio = gestion_null_o_vacios(df)

# 3.- Añadimos nuestros pokemons
add_pokemon_team()

# 4.- Equipo de nuestro rival
load_rival_team()

#######################################################################################
# 5.- Cargamos datos de equipos
#######################################################################################

# df_equipo = pd.read_csv("Nuestro_equipo.csv")
# df_all_pokemon = pd.read_csv("all_pokemon.csv")
