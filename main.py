from fastapi import FastAPI, HTTPException
from pytube import YouTube
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from any origin (replace "*" with your Laravel domain if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/video-info")
def video_info(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")
    try:
        yt = YouTube(url)
        return {
            "title": yt.title,
            "thumbnail": yt.thumbnail_url,
            "views": yt.views,
            "length": yt.length,
            "publish_date": str(yt.publish_date)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))