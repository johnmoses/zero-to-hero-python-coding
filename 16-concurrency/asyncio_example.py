"""
Asyncio

Best for high-concurrency I/O (APIs, websockets, databases).
Single thread, event loop — no GIL issues, very low overhead.
"""
import asyncio
import time


async def fetch(url, delay=1):
    print(f"Fetching: {url}")
    await asyncio.sleep(delay)  # non-blocking wait
    print(f"Done: {url}")
    return f"data from {url}"


async def main():
    urls = [
        "https://example.com/api/1",
        "https://example.com/api/2",
        "https://example.com/api/3",
    ]

    # Run all concurrently — takes ~1 second total
    start = time.time()
    results = await asyncio.gather(*[fetch(url) for url in urls])
    print(f"\nAll done in {time.time() - start:.1f}s")
    print("Results:", results)


asyncio.run(main())
