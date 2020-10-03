import subprocess

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def accept():
    try:
        res = subprocess.check_output(["bun", "esa"])
        return {"status": "OK", "message": str(res)}
    except Exception as err:
        return {"status": "ERROR", "message": str(err)}
