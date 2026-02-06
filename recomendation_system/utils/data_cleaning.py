import pandas as pd


def clean_wrong_numerical_types(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    parameters
    ------------

    input_data : pd.dataframe
    Cambiamos las "," por "." en las columnas numericas

    """


def check_duplicated(input_data: pd.DataFrame, id: str) -> pd.DataFrame:
    """
    parameters
    ------------

    input_data : pd.dataframe
    id : str
    Comprueba si hay duplicados en el dataframe
    """


def gestion_null_o_vacios(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    parameters
    ------------

    input_data : pd.dataframe
    Gestiona los null o vacios del dataframe
    """

    # Miramos la DB
    # print(df.isnull().sum())

    # 1.- Gestionar null o vacios

    df_limpio = input_df.fillna("Nada")
    # print(df_limpio.isnull().sum())

    return df_limpio
