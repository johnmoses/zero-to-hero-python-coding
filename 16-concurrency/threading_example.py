"""
Threading

Best for I/O-bound tasks (file reads, network calls).
Threads share the same memory space.
"""
import threading
import time


def download(url, delay=1):
    print(f"Starting download: {url}")
    time.sleep(delay)  # simulate network I/O
    print(f"Finished download: {url}")


urls = [
    "https://example.com/file1",
    "https://example.com/file2",
    "https://example.com/file3",
]

# Sequential — takes ~3 seconds
print("--- Sequential ---")
start = time.time()
for url in urls:
    download(url)
print(f"Sequential time: {time.time() - start:.1f}s\n")

# Threaded — takes ~1 second
print("--- Threaded ---")
start = time.time()
threads = [threading.Thread(target=download, args=(url,)) for url in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Threaded time: {time.time() - start:.1f}s")
