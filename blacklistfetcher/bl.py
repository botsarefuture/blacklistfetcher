import aiohttp
import asyncio
import ipaddress


class BlacklistFetcher:
    """
    A class for fetching and parsing a blacklist of IP addresses and CIDR networks.
    Automatically adapts to asynchronous or synchronous contexts.
    """

    def __init__(self, url="https://core.security.luova.club/api/blacklist?text=1"):
        self.url = url

    async def _fetch_blacklist(self, session):
        async with session.get(self.url) as response:
            return await response.text()

    @staticmethod
    def _parse_blacklist(data):
        """
        Parse raw blacklist into:
         - individual IPs (as strings)
         - CIDR networks (as ipaddress.ip_network objects)
        """
        ips = set()
        cidrs = set()

        for line in data.splitlines():
            entry = line.strip()
            if not entry:
                continue

            # CIDR network
            if "/" in entry:
                try:
                    cidr = ipaddress.ip_network(entry, strict=False)
                    cidrs.add(cidr)
                except ValueError:
                    # invalid line → ignore silently
                    continue
            
            # Single IP
            else:
                try:
                    ipaddress.ip_address(entry)
                    ips.add(entry)
                except ValueError:
                    continue

        return {
            "ips": sorted(ips),
            "cidrs": list(cidrs)
        }

    async def _get_blacklist_ips_async(self):
        async with aiohttp.ClientSession() as session:
            raw_data = await self._fetch_blacklist(session)
            return self._parse_blacklist(raw_data)

    def get_blacklist_ips(self):
        """
        Returns:
        {
           "ips": ["1.2.3.4", "7.7.7.7"],
           "cidrs": [IPv4Network('10.0.0.0/8'), IPv6Network('2001:db8::/32')]
        }
        """
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            return self._get_blacklist_ips_async()
        else:
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
