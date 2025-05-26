# test_app/main.py
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/run-tests")
def run_tests():
    # Call NL2SQL app (assume it's deployed at http://nl2sql-app:8000)
    response = requests.post("http://nl2sql-app:8000/nl2sql", json={"query": "get all users"})

    # Simulated test check
    if response.status_code == 200 and "sql" in response.json():
        return {"test_result": "Passed", "output": response.json()}
    else:
        return {"test_result": "Failed", "output": response.text}