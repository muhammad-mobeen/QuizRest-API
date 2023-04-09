from typing import Union
from fastapi import FastAPI
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
            <p>Enter the number of MCQS in the URL you want to fetch</p>
            <p>Example: <a href="http://127.0.0.1:8000/5">http://127.0.0.1:8000/5</a> </p>
        </body>
    </html>
    """

@app.get("/{number}")
def read_root(number: int):
    parser = MCQsParser("mcqs_bank.txt", number)
    response = parser.get_response()
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
