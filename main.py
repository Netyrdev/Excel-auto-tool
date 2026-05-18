import argparse
import json
from processor import (
    load_data,
    clean_data,
    apply_discount,
    get_top_products,
    export_with_chart
)


def parse_args():
    parser = argparse.ArgumentParser(description="Excel Data Processor")

    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Ruta al archivo de configuración JSON"
    )

    return parser.parse_args()

def validate_columns(df, columns: dict):
    for key, col_name in columns.items():
        if col_name not in df.columns:
            raise ValueError(f"Columna no encontrada en Excel: {col_name}")


def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def validate_config(config: dict):
    required_keys = ["input_file", "output_file", "header_row", "columns"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Falta la clave obligatoria: {key}")

    required_columns = ["price", "discount"]

    for col in required_columns:
        if col not in config["columns"]:
            raise ValueError(f"Falta columna en config: {col}")

def main():
    try:
        args = parse_args()
        config = load_config(args.config)
        validate_config(config)

        df = load_data(
            config["input_file"],
            config["header_row"]
        )

        validate_columns(df, config["columns"])

        df = clean_data(df)

        df = apply_discount(
            df,
            config["columns"]["price"],
            config["columns"]["discount"]
        )

        top_products = get_top_products(
            df,
            config["columns"]["price"],
            config["top_n"]
        )

        print("\nTop productos:")
        print(top_products)

        export_with_chart(df, config)
        print("Proceso completado correctamente.")
        
    except Exception as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    main()