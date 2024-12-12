### Documentation for `bl.py`

This updated module now introduces a `BlacklistFetcher` class to handle blacklist IP address fetching and parsing, and automatically adapts to both asynchronous and synchronous contexts.

---

## Class: `BlacklistFetcher`

The `BlacklistFetcher` class encapsulates the logic for fetching and parsing blacklist data from an IP blacklist API. It provides methods that can be used both asynchronously and synchronously.

### Methods

#### `__init__(self, url='https://core.security.luova.club/api/blacklist?text=1')`
Initializes the `BlacklistFetcher` instance with a specified URL from which the blacklist will be fetched.

- **Parameters**:
  - `url` (`str`): The URL to fetch the blacklist from (defaults to `https://core.security.luova.club/api/blacklist?text=1`).

#### `_fetch_blacklist(self, session)`
Asynchronously fetches the blacklist data from the given URL.

- **Parameters**:
  - `session` (`aiohttp.ClientSession`): The `aiohttp` session used to make the HTTP request.
  
- **Returns**:
  - `str`: The raw blacklist data as a string.

#### `_parse_blacklist(data)`
Parses the raw blacklist data (newline-separated IP addresses) into a list of IP addresses.

- **Parameters**:
  - `data` (`str`): The raw data fetched from the blacklist source.
  
- **Returns**:
  - `list`: A list of IP addresses extracted from the raw data.

#### `_get_blacklist_ips_async(self)`
Asynchronously retrieves the list of IP addresses from the blacklist API by fetching and parsing the data.

- **Returns**:
  - `list`: A list of IP addresses from the blacklist.

#### `get_blacklist_ips(self)`
Gets the list of IP addresses from the blacklist API. It adapts automatically to synchronous or asynchronous contexts by checking if there is an active event loop.

- **Returns**:
  - `list`: A list of IP addresses from the blacklist.

- **Notes**:
  - If no active event loop is detected, this method will run the asynchronous function in a synchronous context using `asyncio.run()`.
  - If an event loop is running, it will return the result of the asynchronous method.

---

### Example Usage

#### 1. Using the Class in a Synchronous Function
```python
from bl import BlacklistFetcher

def fetch_ips_sync():
    fetcher = BlacklistFetcher()
    ips = fetcher.get_blacklist_ips()  # This will fetch synchronously
    return ips

if __name__ == "__main__":
    ips = fetch_ips_sync()
    for ip in ips:
        print(ip)
```

#### 2. Using the Class in an Asynchronous Function
```python
import asyncio
from bl import BlacklistFetcher

async def async_example():
    fetcher = BlacklistFetcher()
    ips = await fetcher.get_blacklist_ips()  # This will fetch asynchronously
    for ip in ips:
        print(ip)

asyncio.run(async_example())
```

#### Notes for Synchronous Use:
- `asyncio.run()` starts and stops the event loop, so it's suitable for calling asynchronous code from a synchronous context (i.e., from a normal Python function).
- Avoid using `asyncio.run()` repeatedly in the same process, as it will create a new event loop each time. Instead, limit its use to one execution in a program.

---

### Additional Notes:
- Ensure that `aiohttp` is installed in your environment before using this module. You can install it with the following:
  ```bash
  pip install aiohttp
  ```
- The default URL (`https://core.security.luova.club/api/blacklist?text=1`) can be modified by setting a custom URL during the instantiation of the `BlacklistFetcher` class.

---

This approach abstracts away the complexity of handling asynchronous and synchronous contexts, making it easier to use the module in different scenarios.