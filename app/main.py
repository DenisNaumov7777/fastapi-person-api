"""
FastAPI Person API
------------------
A RESTful API for managing person data, migrated from Flask.
Features include dynamic routing, query validation, Pydantic models,
and global error handling.

Author: Denis Naumov
Location: Cologne, Germany
Date: 2026
"""

from fastapi import FastAPI, Response, status, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

# Initialize the application with metadata
app = FastAPI(
    title="Person API Service",
    description="REST API for managing person records with UUIDs.",
    version="1.0.0",
    contact={
        "name": "Denis Naumov",
        "email": "denis@example.com",
    },
)

# --- DATA MODELS ---

class Person(BaseModel):
    """
    Pydantic model representing a Person entity.
    Provides automatic validation and documentation.
    """
    id: UUID
    first_name: str
    last_name: str
    graduation_year: int
    address: str
    city: str
    zip: str
    country: str
    avatar: str

# --- MOCK DATABASE ---

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# --- GLOBAL ERROR HANDLERS ---

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Global handler for HTTP exceptions (e.g., 404).
    Returns a JSON response instead of default HTML.
    """
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "API not found"}
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global handler for unexpected server errors (500).
    """
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)}
    )

# --- ROUTES ---

@app.get('/')
def index():
    """Root endpoint to verify the service is running."""
    return {"message": "Welcome to the Person API Service by Denis Naumov"}

@app.get("/no_content", status_code=status.HTTP_204_NO_CONTENT)
def no_content():
    """Returns a 204 No Content status."""
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/exp")
def index_explicit():
    """Returns an explicit JSONResponse with 200 OK."""
    return JSONResponse(
        content={"message": "Hello world"},
        status_code=status.HTTP_200_OK
    )

@app.get("/data")
def get_data():
    """
    Returns the count of data items.
    Simulates 500 if data is empty or 404 if variable is undefined.
    """
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message": "Data is empty"}
            )
    except NameError:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Data not found"}
        )

@app.get("/name_search")
def name_search(q: Optional[str] = None):
    """
    Searches for a person by first name using a query parameter.
    Example: /name_search?q=John
    """
    if not q:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Invalid input parameter"}
        )

    if q.isdigit():
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": "Invalid input parameter"}
        )

    person = next((item for item in data if item["first_name"].lower() == q.lower()), None)

    if person:
        return person
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Person not found"}
        )

@app.get("/count")
def count():
    """Returns the total number of persons in the database."""
    return {"data count": len(data)}

@app.get("/person/{person_id}")
def find_by_uuid(person_id: UUID):
    """
    Finds a person by their UUID.
    FastAPI automatically validates the UUID format.
    """
    for person in data:
        if person["id"] == str(person_id):
            return person

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Person not found"}
    )

@app.delete("/person/{person_id}")
def delete_by_uuid(person_id: UUID):
    """
    Deletes a person by their UUID.
    """
    for i, person in enumerate(data):
        if person["id"] == str(person_id):
            del data[i]
            return {"message": f"Person with ID {person_id} deleted"}

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Person not found"}
    )

@app.post("/person")
def add_by_uuid(person: Person):
    """
    Creates a new person record.
    Validates input using the Pydantic model.
    """
    # Convert Pydantic model to dict
    person_dict = person.model_dump()
    
    # Cast UUID object to string for storage compatibility
    person_dict["id"] = str(person_dict["id"])
    
    data.append(person_dict)
    return {"message": person_dict["id"]}

@app.get("/test500")
def test500():
    """
    Endpoint to trigger a forced 500 error for testing the Global Exception Handler.
    """
    raise Exception("Forced exception for testing")