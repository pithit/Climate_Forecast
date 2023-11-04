import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import clima_datos

# Carga los datos del archivo JSON
data_clima = clima_datos.cargar_datos_clima('clima_data.json')
datos_historicos = clima_datos.obtener_datos_historicos(data_clima)
pronostico = clima_datos.obtener_pronostico(data_clima)

# Calcula la fecha de mañana
fecha_actual = datetime.datetime.strptime(pronostico["fecha"], "%Y-%m-%d")
fecha_mañana = fecha_actual + datetime.timedelta(days=1)
fecha_mañana_str = fecha_mañana.strftime("%Y-%m-%d")

# Proyecta el clima de mañana (en este caso, simplemente copia el pronóstico)
pronostico_mañana = pronostico.copy()
pronostico_mañana["fecha"] = fecha_mañana_str

# Inicializa la aplicación Dash
app = dash.Dash(__name__)

# Define el diseño del dashboard
app.layout = html.Div([
    html.H1("Informe del Clima en Buenos Aires"),
    html.Div([
        html.Label("Fecha:"),
        dcc.Input(id="fecha-input", type="text", value=pronostico_mañana["fecha"], disabled=True),
        html.Label("Temperatura (°C):"),
        dcc.Input(id="temperatura-input", type="text", value=pronostico_mañana["temperatura"], disabled=True),
        html.Label("Humedad (%):"),
        dcc.Input(id="humedad-input", type="text", value=pronostico_mañana["humedad"], disabled=True),
        html.Label("Viento (km/h):"),
        dcc.Input(id="viento-input", type="text", value=pronostico_mañana["viento"], disabled=True),
        html.Label("Descripción:"),
        dcc.Input(id="descripcion-input", type="text", value=pronostico_mañana["descripcion"], disabled=True),
    ]),
])

# Ejecuta la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)
