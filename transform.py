import pandas as pd

def tempo_voo_horas_para_minutos(df):

    if "tempo_voo" in df.columns:
        df["tempo_voo_minutos"] = df["tempo_voo"] * 60
    else:
        raise ValueError("Coluna 'tempo_voo' não encontrada no DataFrame.")
    return df


def classifica_turno_partida(df):

    def extrai_hora(dep_time):
        try:
            if pd.isna(dep_time):
                return None
            dep_time = int(dep_time)
            hora = dep_time // 100
            minuto = dep_time % 100
            return pd.to_datetime(f"{hora:02d}:{minuto:02d}", format="%H:%M").time()
        except:
            return None

    def get_turno(hora):
        if hora is None:
            return "indefinido"
        elif 6 <= hora.hour < 12:
            return "manhã"
        elif 12 <= hora.hour < 18:
            return "tarde"
        elif 18 <= hora.hour < 24:
            return "noite"
        else:
            return "madrugada"

    df["hora_partida"] = df["data_hora"].apply(extrai_hora)
    df["turno_partida"] = df["hora_partida"].apply(get_turno)
    return df
