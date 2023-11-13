# Climate Forecast Project


[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release)
[![Build Status](https://travis-ci.org/pithit/Climate_Forecast.svg?branch=master)](https://travis-ci.org/pithit/Climate_Forecast)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://github.com/pithit/Climate_Forecast)

## Overview

This project aims to create a climate forecast dashboard for Buenos Aires, generating and visualizing fictional climate data using PySpark and creating a simple web-based dashboard. This project is being updating on regular basis.

## Features

- **Data Generation:** Fictional climate data is generated for the last two years, including temperature, humidity, wind speed, and weather descriptions.
- **PySpark:** The data is processed and stored using PySpark, allowing for efficient data manipulation.
- **Dashboard:** A simple dashboard is created to display the climate forecast for Buenos Aires.

## File Structure

- **`data_generation.py`:** Python script to generate fictional climate data using PySpark.
- **`dashboard.py`:** Python script to create a web-based dashboard for climate data visualization.
- **`clima_data_2_years.parquet`:** Parquet file containing the generated climate data.

## Usage

1. Run `data_generation.py` to generate fictional climate data and store it in `clima_data_2_years.parquet`.
2. Run `dashboard.py` to start the web-based dashboard.

## Getting Started

### Prerequisites

- Python 3
- PySpark
- Required Python packages (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/climate-forecast-project.git

