import os
import pandas as pd


def load_sales_csv(csv_path=None):
    """Carga un CSV de ventas y devuelve un DataFrame de pandas.

    Args:
        csv_path (str): Ruta al archivo CSV. Si es None, intenta cargar
                        '../ventas/ControlBotBar - EntradaDiaria.csv'.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.

    Raises:
        FileNotFoundError: Si no existe el archivo.
        Exception: Para otros errores de lectura.
    """
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'ventas', 'ControlBotBar - EntradaDiaria.csv')
        csv_path = os.path.abspath(csv_path)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'No se encontró el archivo: {csv_path}')

    try:
        df = pd.read_csv(csv_path, parse_dates=True, dayfirst=True, low_memory=False)
        return df
    except Exception:
        # Re-raise con contexto
        raise


if __name__ == '__main__':
    # Pequeña prueba rápida al ejecutar el script
    try:
        df = load_sales_csv()
        print('Archivo cargado correctamente. Shape:', df.shape)
        print('\nColumnas:', df.columns.tolist())
    except Exception as e:
        print('Error cargando CSV:', e)
