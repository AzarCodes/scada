import random
import time
import logging
from prometheus_client import start_http_server, Gauge

logging.basicConfig(level=logging.INFO)

metrics = {
    'temp':      Gauge('temperature_celsius', 'Temperature in Celsius'),
    'pressure':  Gauge('pressure_psi',        'Pressure in PSI'),
    'flow':      Gauge('flow_lpm',            'Flow in liters per minute'),
    'voltage':   Gauge('voltage_v',           'Voltage in volts'),
    'current':   Gauge('current_a',           'Current in amperes'),
    'humidity':  Gauge('humidity_percent',    'Humidity in percent'),
    'vibration': Gauge('vibration_mm_s',      'Vibration in mm/s')
}

def generate_data():
    while True:
        temp      = round(random.uniform(20, 30), 1)
        pressure  = round(random.uniform(0, 100), 1)
        flow      = round(random.uniform(50, 150), 1)
        voltage   = round(random.uniform(220, 240), 1)
        current   = round(random.uniform(0, 10), 2)
        humidity  = round(random.uniform(0, 100), 1)
        vibration = round(random.uniform(0, 10), 2)

        for k, v in zip(metrics.keys(), [temp, pressure, flow, voltage, current, humidity, vibration]):
            metrics[k].set(v)

        logging.info("Temp=%s°C Press=%sPSI Flow=%slpm Volt=%sV Curr=%sA Humid=%s%% Vibrate=%smm/s",
                     temp, pressure, flow, voltage, current, humidity, vibration)
        time.sleep(2)

if __name__ == "__main__":
    start_http_server(8000)   # ← always 8000 inside container
    generate_data()