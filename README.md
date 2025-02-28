# Cellular Module Automation

This project provides a framework for automating the testing of a cellular module using AT commands. The tests are written in Python and use the pytest and `unittest` framework to ensure the functionality of various AT commands.

## Table of Contents
- Installation
- Usage

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rrakshithaa/cellular-module-automation.git
    cd cellular-module-automation
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Connect your cellular module** to the appropriate COM port (e.g., `COM12`).

2. **Run the tests**:
    ```sh
    python test_at_commands.py
    ```

## Test Cases

The following AT commands are tested in this project:
**AT command which is vulnerable to Telit modules**
- **Network Registration Status**: `AT command?`
- **Signal Quality**: `AT command`
- **Manufacturer Identification**: `AT command`
- **Model Identification**: `AT command`
- **Revision Identification**: `AT command`
