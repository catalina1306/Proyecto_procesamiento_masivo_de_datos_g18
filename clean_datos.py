import pandas as pd
import ast
from tqdm import tqdm

def expandir_columna_diccionario(csv_entrada, csv_salida):
    df = pd.read_csv(csv_entrada)

    tqdm.pandas(desc="Procesando columna velocity_last_hour")

    df_dicts = df['velocity_last_hour'].progress_apply(lambda x: ast.literal_eval(x))

    df_expandidas = pd.json_normalize(df_dicts)
    df_expandidas.columns = [f'velocity_last_hour_{col}' for col in df_expandidas.columns]

    df.drop(columns=['velocity_last_hour'], inplace=True)

    df_final = pd.concat([df, df_expandidas], axis=1)

    df_final.to_csv(csv_salida, index=False)

expandir_columna_diccionario('fraud_data.csv', 'fraud_data_clean.csv')
