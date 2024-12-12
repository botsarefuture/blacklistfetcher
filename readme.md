# BlacklistFetcher

`BlacklistFetcher` is a Python module that fetches and parses a blacklist of IP addresses from a specified URL. It provides an easy-to-use API that works both synchronously and asynchronously. The module is built on top of `aiohttp` for asynchronous HTTP requests and can be integrated seamlessly into both synchronous and asynchronous Python environments.

## Features
- Fetch blacklist data from a specified URL.
- Parse the raw blacklist data into a list of IP addresses.
- Adapt automatically to both asynchronous and synchronous contexts.

## Installation

To install the `BlacklistFetcher` module, you can use `pip`:

```bash
pip install blacklistfetcher
```

## Usage

### Example Usage

#### 1. Using in a Synchronous Function

```python
from blacklistfetcher import BlacklistFetcher

def fetch_ips_sync():
    fetcher = BlacklistFetcher()
    ips = fetcher.get_blacklist_ips()  # This will fetch synchronously
    return ips

if __name__ == "__main__":
    ips = fetch_ips_sync()
    for ip in ips:
        print(ip)
```

#### 2. Using in an Asynchronous Function

```python
import asyncio
from blacklistfetcher import BlacklistFetcher

async def async_example():
    fetcher = BlacklistFetcher()
    ips = await fetcher.get_blacklist_ips()  # This will fetch asynchronously
    for ip in ips:
        print(ip)

asyncio.run(async_example())
```

## Requirements

- Python 3.6+
- `aiohttp` for asynchronous HTTP requests. You can install it with:
  ```bash
  pip install aiohttp
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.