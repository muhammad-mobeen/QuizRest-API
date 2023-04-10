from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from ParserEngine import MCQsParser

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>🚀QuizREST API</title>
        </head>
        <body>
            <h1>Welcome to QuizREST API!</h1>
            <h2>Quiz Topic: Socket Programming in UDP</h2>
            <p>Enter the number of MCQS in the URL you want to fetch</p>
            <p>Example: <a href="http://127.0.0.1:8000/5">http://127.0.0.1:8000/5</a> </p>
        </body>
    </html>
    """

@app.get("/{number}", status_code=200)
def get_mcqs(number: int):
    parser = MCQsParser("mcqs_bank.txt", number)
    response = parser.get_response()
    if response["total_questions"] < number:
        raise HTTPException(
            status_code=400, 
            detail="Maximum number of MCQS requestable is 20"
            )
    return response


@app.get("/{filename}/{number}")
def get_file_mcqs(filename: str, number: int = 20):
    parser = MCQsParser(filename+".txt", number)
    response = parser.get_response()

    # Check if file exists or not else throw Exception Response Code
    if type(response) is not dict:
        raise HTTPException(
            status_code=404,
            detail=response
            )
    
    # Check if number of MCQS available else throw Exception Response Code
    if response["total_questions"] < number:
        raise HTTPException(
            status_code=400, 
            detail="Maximum number of MCQS requestable is 20"
            )
    
    return response

@app.get("/error", status_code=200)
def error(response):
    return response

@app.get("/favicon.ico", status_code=400)
def favicon_response():
    return {"favicon": "Not Found"}