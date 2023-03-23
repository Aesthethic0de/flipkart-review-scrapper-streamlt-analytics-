# Description: This is the main file for the project. It will be used to run the program.
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from utils.scrapper import review_scrapper

app = FastAPI()

class product(BaseModel):
    product_name: str
@app.post("/reviews/")
def create_review(request : product):
    review_scrapper(request.product_name)
    return {"data": "Review scrapped successfully"}




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)







