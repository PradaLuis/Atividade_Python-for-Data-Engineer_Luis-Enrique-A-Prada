import pandas as pd

def tempo_voo_horas(df, coluna_tempo_horas):
    df['tempo_voo_minutos'] = df[coluna_tempo_horas] * 60
    return df


def turno_partida(df, coluna_hora_partida):
    def classificar_turno(horario):
        if pd.isnull(horario):
            return None
        hora = horario.hour
        if 5 <= hora < 12:
            return 'manhã'
        elif 12 <= hora < 18:
            return 'tarde'
        elif 18 <= hora < 24:
            return 'noite'
        else:
            return 'madrugada'

    df['turno_partida'] = pd.to_datetime(df[coluna_hora_partida]).apply(classificar_turno)
    return df
