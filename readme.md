# `BlacklistFetcher` Library Documentation

The `BlacklistFetcher` library provides a simple and efficient way to fetch and parse IP addresses from a blacklist API. It supports both synchronous and asynchronous environments, making it versatile for different applications. This library abstracts the complexity of handling asynchronous operations, allowing you to work with blacklist data in a straightforward manner.

## Installation

To use the `BlacklistFetcher` library, you need to install the `aiohttp` package for asynchronous HTTP requests.

```bash
pip install aiohttp
```

---

## Class: `BlacklistFetcher`

The `BlacklistFetcher` class is designed to fetch and parse blacklist data from a specified URL. It automatically adapts to both asynchronous and synchronous contexts, allowing you to use it in different environments without additional setup.

### Methods

#### `__init__(self, url='https://core.security.luova.club/api/blacklist?text=1')`
Initializes the `BlacklistFetcher` instance with a given URL for fetching the blacklist data.

- **Parameters**:
  - `url` (`str`): The URL from which the blacklist will be fetched. Defaults to `https://core.security.luova.club/api/blacklist?text=1`.

#### `_fetch_blacklist(self, session)`
Asynchronously fetches the raw blacklist data from the specified URL.

- **Parameters**:
  - `session` (`aiohttp.ClientSession`): The session used for making the HTTP request.
  
- **Returns**:
  - `str`: The raw blacklist data as a string.

#### `_parse_blacklist(data)`
Parses the raw blacklist data (newline-separated IP addresses) into a list of IP addresses.

- **Parameters**:
  - `data` (`str`): The raw data fetched from the blacklist API.
  
- **Returns**:
  - `list`: A list of IP addresses parsed from the raw data.

#### `_get_blacklist_ips_async(self)`
Asynchronously fetches and parses the blacklist data, returning a list of IP addresses.

- **Returns**:
  - `list`: A list of IP addresses from the blacklist.

#### `get_blacklist_ips(self)`
This method adapts to both synchronous and asynchronous contexts. If an active event loop is detected, it runs asynchronously; otherwise, it executes the asynchronous function synchronously using `asyncio.run()`.

- **Returns**:
  - `list`: A list of IP addresses from the blacklist.

- **Notes**:
  - If no event loop is detected, the method will run the asynchronous function synchronously using `asyncio.run()`.
  - If an event loop is already running, it will use the existing loop to fetch the data asynchronously.

---

## Example Usage

#### 1. Using the Library in a Synchronous Context

```python
from bl import BlacklistFetcher

def fetch_ips_sync():
    fetcher = BlacklistFetcher()
    ips = fetcher.get_blacklist_ips()  # This fetches synchronously
    return ips

if __name__ == "__main__":
    ips = fetch_ips_sync()
    for ip in ips:
        print(ip)
```

#### 2. Using the Library in an Asynchronous Context

```python
import asyncio
from bl import BlacklistFetcher

async def async_example():
    fetcher = BlacklistFetcher()
    ips = await fetcher.get_blacklist_ips()  # This fetches asynchronously
    for ip in ips:
        print(ip)

asyncio.run(async_example())
```

#### Notes for Synchronous Use:
- `asyncio.run()` is used to start the event loop, making it suitable for calling asynchronous code from a synchronous function.
- Avoid using `asyncio.run()` multiple times in the same process. It should only be called once per program to prevent creating multiple event loops.

---

### Additional Notes:

- Ensure that `aiohttp` is installed before using the library. Install it via:
  ```bash
  pip install aiohttp
  ```
- The default URL for fetching the blacklist is `https://core.security.luova.club/api/blacklist?text=1`, but it can be customized by specifying a different URL when initializing the `BlacklistFetcher`.

---

The `BlacklistFetcher` library provides a flexible and easy-to-use interface for working with blacklist data. Whether you need it in a synchronous or asynchronous context, this library abstracts the complexity, allowing you to focus on using the data instead of managing asynchronous tasks.