import pandas as pd
import os

def load_data(file_path: str, header_row: int):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo no existe: {file_path}")
    try:
        return pd.read_excel(file_path, header=header_row)
    except Exception:
        raise ValueError("Error leyendo Excel: revisa 'header_row' en config")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["PRECIO ORI"] = pd.to_numeric(df["PRECIO ORI"], errors="coerce")
    return df


def apply_discount(df: pd.DataFrame, price_col: str, discount_col: str) -> pd.DataFrame:
    df = df.copy()
    df["DESCUENTOS APROXIMADOS"] = df[price_col] * (
        1 - df[discount_col] / 100
    )
    return df


def get_top_products(df: pd.DataFrame, price_col: str, n: int):
    return df.sort_values(by=price_col, ascending=False).head(n)


def generate_unique_filename(file_path: str) -> str:
    if not os.path.exists(file_path):
        return file_path

    base, extension = os.path.splitext(file_path)
    counter = 1

    while True:
        new_file = f"{base}({counter}){extension}"
        if not os.path.exists(new_file):
            return new_file
        counter += 1

def export_with_chart(df, config):
    output_path = generate_unique_filename(config["output_file"])

    writer = pd.ExcelWriter(output_path, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Data", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Data"]

    chart_config = config.get("chart", {})

    if chart_config.get("enabled"):
        chart = workbook.add_chart({"type": chart_config["type"]})

        x_col = chart_config["x_column"]
        y_col = chart_config["y_column"]
        top_n = chart_config["top_n"]

        top_df = df.sort_values(by=y_col, ascending=False).head(top_n)

        # Escribimos top_df en otra hoja
        top_df.to_excel(writer, sheet_name="Top", index=False)
        top_sheet = writer.sheets["Top"]

        chart.add_series({
            "name": y_col,
            "categories": ["Top", 1, top_df.columns.get_loc(x_col), top_n, top_df.columns.get_loc(x_col)],
            "values": ["Top", 1, top_df.columns.get_loc(y_col), top_n, top_df.columns.get_loc(y_col)],
        })

        top_sheet.insert_chart("H2", chart)

    writer.close()

    print(f"Archivo exportado con gráfico: {output_path}")