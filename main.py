from fastapi import FastAPI

app = FastAPI()


# Home Route
@app.get("/")
def home ():
    return {"message": "Welcome to the FastAPI application!"}  


# About Route
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

# Contact Route
@app.get("/contact")
def contact():
    return {"message": "You can reach us at contact@example.com."}