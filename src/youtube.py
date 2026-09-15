import re

from youtube_transcript_api import (
    YouTubeTranscriptApi
)


def get_video_id(url):
    """
    Extract the YouTube video ID from a URL.
    """

    patterns = [

        r"(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})",

        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",

        r"(?:youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",

        r"(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            url
        )

        if match:

            return match.group(1)

    return None


def get_transcript(video_id):
    """
    Fetch the English transcript of a YouTube video.
    """

    api = YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=["en"]
    )

    text = " ".join(
        snippet.text
        for snippet in transcript
    )

    return text