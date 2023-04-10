# QuizRest API
 A quiz API developed in Fast API Framework in Python. Assignment 2 of Computer Networks.
 Quiz Topic: Socket Programming in UDP

## How to run?
First activate environment
```
env/Scripts/activate
```

Now activate Uvicorn Server
```
uvicorn main:app --reload
```

Now you can go to hosted app url!

## How to use?
You can get responses in following ways:-
Both urls will return 5 MCQS

```
http://127.0.0.1:8000/mcqs_bank/5
```
OR
```
http://127.0.0.1:8000/5
```
