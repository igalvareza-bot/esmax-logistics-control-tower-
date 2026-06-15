import pandas as pd

def clasificacion_abc(df):
    resumen = df.groupby("sku")["demanda"].sum().reset_index()

    resumen = resumen.sort_values(by="demanda", ascending=False)

    resumen["acumulado"] = resumen["demanda"].cumsum() / resumen["demanda"].sum()

    def categoria(x):
        if x <= 0.8:
            return "A"
        elif x <= 0.95:
            return "B"
        else:
            return "C"

    resumen["ABC"] = resumen["acumulado"].apply(categoria)

    return resumen