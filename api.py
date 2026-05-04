from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Calculadora API", version="1.0.0")


class CalculationRequest(BaseModel):
    first_number: float
    second_number: float
    operation: str


class CalculationResponse(BaseModel):
    result: float
    operation: str
    first_number: float
    second_number: float


@app.get("/")
def root():
    return {"message": "Calculadora API - Simple Calculator API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):
    operation = request.operation
    first = request.first_number
    second = request.second_number

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = first / second
    else:
        raise HTTPException(status_code=400, detail=f"Invalid operation: {operation}")

    if result == int(result):
        result = int(result)

    return CalculationResponse(
        result=result,
        operation=operation,
        first_number=first,
        second_number=second
    )


@app.get("/history")
def get_history():
    return {"history": [], "message": "History feature - calculate to build history"}