from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
import requests
from ics import Calendar
from ics.parse import ParseError
import base64

app = FastAPI()
REQUEST_TIMEOUT = 30


@app.get("/")
def index():
    return FileResponse('index.html')


@app.get("/calendar/{b64url}/{b64allowlist}/filtered.ics")
async def get_calendar(b64url: str, b64allowlist: str):
    try:
        url = base64.urlsafe_b64decode(b64url)
        allowlist = base64.urlsafe_b64decode(b64allowlist).decode("utf-8").split(",")
    except:
        raise HTTPException(status_code=400, detail="Invalid base64 data.")

    try:
        remote_cal = requests.get(url, timeout=REQUEST_TIMEOUT).text
    except requests.Timeout:
        raise HTTPException(status_code=400,
                            detail=f"Timed out while getting the URL, timeout is {REQUEST_TIMEOUT} seconds.")
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail="Error getting the URL.")
    except:
        raise HTTPException(status_code=500, detail="Error while fetching calendar contents.")

    try:
        cal = Calendar(remote_cal)
    except ParseError:
        raise HTTPException(status_code=400, detail="Server response not a valid ics format.")
    except:
        raise HTTPException(status_code=500, detail="Error while parsing calendar contents.")

    valid_events = []
    for c in cal.events:
        for word in allowlist:
            if word in c.name:
                valid_events.append(c)

    cal.events = set(valid_events)
    return Response(content=str(cal), media_type="text/calendar")
