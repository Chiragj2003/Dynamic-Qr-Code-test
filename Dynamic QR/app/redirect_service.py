from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for the redirect URLs (for simplicity, using a dictionary)
redirect_urls = {
    "default": "https://default-url.com",
    "my-unique-code": "https://initial-url.com"
}

class URLUpdateRequest(BaseModel):
    new_url: str

@app.get("/{code}")
def redirect(code: str):
    if code in redirect_urls:
        return RedirectResponse(url=redirect_urls[code])
    raise HTTPException(status_code=404, detail="Code not found")

@app.post("/update/{code}")
def update_redirect(code: str, url_update: URLUpdateRequest):
    redirect_urls[code] = url_update.new_url
    return {"message": "URL updated successfully"}
