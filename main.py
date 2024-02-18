from fastapi import FastAPI
import uvicorn
from libs.logic import search_wiki
from libs.logic import wiki as wiki_logic
from libs.logic import phrase as wiki_phrase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki or /phrase"}

@app.get("/search/{query}")
async def add(query: str):
    """Page to search in Wikipedia"""

    result = search_wiki(query)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve Wikipedia page"""

    result = wiki_logic(name)
    return {"result": result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    """Return Phrase from Wikipedia"""

    result = wiki_phrase(name)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
