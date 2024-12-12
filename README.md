# DataQuant: Modular and Scalable Measurement System

**DataQuant** is an object-oriented framework designed for modular and scalable data acquisition, processing, and storage. It supports various measurement devices, sensors, and storage backends while maintaining a clean and extendable architecture.

---

## Features
- Modular integration of measurement devices and sensors.
- Support for various physical quantities (current, voltage, temperature, etc.).
- Storage support for InfluxDB (expandable to other formats like CSV).
- Real-time visualization of data (e.g., heatmaps, graphs).
- Designed with **SOLID principles** for maintainability and scalability.

---

## Directory Structure

```plaintext
DataQuant/
├── devices/                   # Device-specific implementations
│   ├── rigol_dm3068.py        # Rigol DM3068 device implementation
├── measurements/              # Measurement-specific logic
│   ├── current.py             # Current measurement logic
│   ├── voltage.py             # Voltage measurement logic
├── storage/                   # Storage backends
│   ├── influxdb_storage.py    # InfluxDB storage implementation
├── main.py                    # Main script for running measurements
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation