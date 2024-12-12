import aiohttp
import asyncio

class BlacklistFetcher:
    """
    A class for fetching and parsing a blacklist of IP addresses.
    Automatically adapts to asynchronous or synchronous contexts.
    """

    def __init__(self, url='https://core.security.luova.club/api/blacklist?text=1'):
        """
        Initialize the BlacklistFetcher with a URL.

        Parameters
        ----------
        url : str
            The URL to fetch the blacklist from.
        """
        self.url = url

    async def _fetch_blacklist(self, session):
        """
        Asynchronously fetch the blacklist from the given URL.

        Parameters
        ----------
        session : aiohttp.ClientSession
            The aiohttp session to use for the request.

        Returns
        -------
        str
            The raw blacklist data as a string.
        """
        async with session.get(self.url) as response:
            return await response.text()

    @staticmethod
    def _parse_blacklist(data):
        """
        Parse the blacklist data into a list of IP addresses.

        Parameters
        ----------
        data : str
            The raw blacklist data.

        Returns
        -------
        list
            A list of IP addresses.
        """
        return data.splitlines()

    async def _get_blacklist_ips_async(self):
        """
        Asynchronously get the list of IP addresses from the blacklist API.

        Returns
        -------
        list
            A list of IP addresses from the blacklist.
        """
        async with aiohttp.ClientSession() as session:
            raw_data = await self._fetch_blacklist(session)
            return self._parse_blacklist(raw_data)

    def get_blacklist_ips(self):
        """
        Get the list of IP addresses from the blacklist API, automatically
        adapting to synchronous or asynchronous contexts.

        Returns
        -------
        list
            A list of IP addresses from the blacklist.
        """
        try:
            # Check if there is an active event loop (asynchronous context)
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # No active event loop, use synchronous mode
            loop = None

        if loop and loop.is_running():
            # Running in an asynchronous context
            return self._get_blacklist_ips_async()
        else:
            # Running in a synchronous context
            return asyncio.run(self._get_blacklist_ips_async())

# Example usage
if __name__ == "__main__":
    fetcher = BlacklistFetcher()

    # Synchronous usage
    ips = fetcher.get_blacklist_ips()
    if asyncio.iscoroutine(ips):
        print("This function should be awaited in an asynchronous context.")
    else:
        print("Fetched IPs in synchronous context:")
        for ip in ips:
            print(ip)

    # Asynchronous usage
    async def async_example():
        async_ips = await fetcher.get_blacklist_ips()
        print("Fetched IPs in asynchronous context:")
        for ip in async_ips:
            print(ip)

    # Uncomment the following line to test in an asynchronous context
    # asyncio.run(async_example())
