# Backend

This directory contains the Flask backend code for the Study Planner App.

## Setup

### 1. Create a virtual environment:
```bash
python -m venv venv
```

### 2. Activate the virtual environment:

- On windows:
```bash
venv\Scripts\activate
```

- On MacOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To start the Flask application, run:
```bash
flask run
```
The app will be available at `http://localhost:5000`.

## Running Tests

To run tests, use:
```bash
pytest
```
