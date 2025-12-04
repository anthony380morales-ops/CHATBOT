import httpx
import asyncio

async def fetch_url(url: str, timeout: int = 5) -> str:
    """
    Fetch content from a URL asynchronously.
    """
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text[:2000]  # truncate to first 2000 chars
    except Exception as e:
        return f"⚠️ Failed to fetch URL {url}: {str(e)}"
