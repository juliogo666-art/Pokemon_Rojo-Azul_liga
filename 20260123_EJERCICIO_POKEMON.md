\# DEFINIR SCOPE  
Queremos ayudar a un usuario a ganar la liga pokemon. Él tiene 6 pokemons y sus rivales también. 

- De entre 6 pokemons → elegir cuál es el mejor contra 1 pokemon específico. 

\#\# Quén tenemos

1. Datos pokemon   
   1. Especificaciones de pokemons  
      1. Ataques  
      2. Estad´siticas  
      3. tipos  
      4. Matriz de tipos  
   2. Información en internet de otra gente que ya ha ganado.  
2. Qué le podemos pedir al usuario  
   1. Sus 6 pokemons  
   2. Sus rivales.

\#\# Cuál es el flujo

1. INPUTS  
   1. Tus 6 pokemons a elegir.  
   2. Pokemon a batir.  
2. Esto va a una DB  
   1. Consulta los datos de los pokemons  
   2. Saca los datos necesarios.  
3. Vectorizados la información  
4. Inferencia del modelo.  
5. MOSTRAMOS RESUTLADOS 🙂

\#\# Qué restricciones sabemos que tenemos con nuestra información actual.

1. No saber los movimientos de los pokemons.  
2. ¿Qué combate habrá después?  
3. El orden en que el rival va a sacar los pokemons.  
4. Objetos mágicos.  
5. Importància de qué pokemon sacar.  
6. Puede haber el caso en que ninguna opción es buena. 

\# DEFINICIÓN DE “WORK PACKAGES”.

\[INSERTAR FOTO\]

\#\# PREPARACIÓM DB

1. Mirar la DB  
2. Gestionar nulls o vacíos.  
3. Decidir qué se hace con las variables categóricas.  
4. Normalizar valores todos a la misma cosa.  
5. Feature Engineering.  
6. DB FINAL 🙂

\#\# VECTORIZACIÓN

→ (Esto es la siguiente clase :)) )

1. Comparar los datos de entrada con la DB  
2. Transformar estos datos a agrupaciones específicas.   
3. Limpiar el vector a lo que le interesa el modelo. 

\#\# MODELO  
→ Es un sistema de recomendación… PERO CUÁL???

1. Decidir modelo  
   1. En clase hemos visto unos cuantos.   
   2. Hemos decidido todos juntos que el collaborative filtering no serviría en esta ocasion  
   3. Pero que Content based y Matrix factorization sirven.  
   4. Vamos a provar los dos modelos.

\#\# El “empollon” AKA → Benchmarking de tendencias.  
