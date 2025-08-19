from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    """
    Extracts YouTube video ID from any valid YouTube URL
    """
    parsed_url = urlparse(url)

    if "youtu.be" in parsed_url.netloc:
        # Short link format: youtu.be/<id>
        return parsed_url.path[1:]
    elif "youtube.com" in parsed_url.netloc:
        # Long link format: youtube.com/watch?v=<id>
        return parse_qs(parsed_url.query).get("v", [None])[0]
    return None