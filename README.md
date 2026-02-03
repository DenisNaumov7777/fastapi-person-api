# 🚀 FastAPI Person API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

**Author:** Denis Naumov  
**Location:** Cologne, Germany 🇩🇪

## 📖 Overview

This project demonstrates a robust RESTful API built with **FastAPI**. It represents a complete migration and refactoring of a legacy Flask application.

The API manages a mock database of "Person" records and demonstrates advanced backend concepts including:
* **Strict Data Validation** using Pydantic models.
* **Global Error Handling** (JSON responses for 404/500 errors).
* **Dynamic Routing** with UUID validation.
* **CRUD Operations** (Create, Read, Delete).

## 🛠 Tech Stack

* **FastAPI**: Modern, high-performance web framework for building APIs.
* **Pydantic**: Data validation and settings management using Python type hints.
* **Uvicorn**: Lightning-fast ASGI server implementation.
* **Python 3.10+**: Core programming language.

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone [https://github.com/DenisNaumov7777/fastapi-person-api.git](https://github.com/DenisNaumov7777/fastapi-person-api.git)
cd fastapi-person-api

```

### 2. Install dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt

```

### 3. Run the development server

Since the application code is inside the `app` package:

```bash
fastapi dev app/main.py

```

The server will start at `http://127.0.0.1:8000`.

## 📚 API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

## 🧪 Testing Endpoints (cURL Examples)

You can also test the API directly from your terminal.

### 1. Get Application Status

```bash
curl -i [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```

### 2. Search Person by Name (Query Parameter)

Validates that the input is a string (not a number).

```bash
curl -i "[http://127.0.0.1:8000/name_search?q=Abdel](http://127.0.0.1:8000/name_search?q=Abdel)"

```

### 3. Create a New Person (POST)

Validates JSON body against the `Person` Pydantic model.

```bash
curl -X POST -i \
  --url [http://127.0.0.1:8000/person](http://127.0.0.1:8000/person) \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "[http://dummyimage.com/139x100.png/cc0000/ffffff](http://dummyimage.com/139x100.png/cc0000/ffffff)"
}'

```

### 4. Delete Person by UUID (Path Parameter)

Checks if the ID exists and performs deletion.

```bash
curl -X DELETE -i [http://127.0.0.1:8000/person/4e1e61b4-8a27-11ed-a1eb-0242ac120002](http://127.0.0.1:8000/person/4e1e61b4-8a27-11ed-a1eb-0242ac120002)

```

### 5. Error Handling Tests

The API returns JSON errors instead of HTML.

* **Test 404 (Not Found):**
```bash
curl -i [http://127.0.0.1:8000/unknown_route](http://127.0.0.1:8000/unknown_route)

```


* **Test 500 (Internal Server Error):**
```bash
curl -i [http://127.0.0.1:8000/test500](http://127.0.0.1:8000/test500)

```



## 📂 Project Structure

```text
fastapi-person-api/
├── app/
│   ├── __init__.py    # Makes 'app' a Python package
│   └── main.py        # Main application logic
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignored files (venv, __pycache__, etc.)
└── README.md          # Project documentation

```

---

*Developed with ❤️ in Cologne.*

```

