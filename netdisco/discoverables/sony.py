from . import SSDPDiscoverable

try:
    # python 3
    from urllib.parse import urlparse
except ImportError:
    # python 2
    from urlparse import urlparse

from pprint import pprint as pp

class Discoverable(SSDPDiscoverable):
    def get_entries(self):
        devs = self.find_by_device_description({
            "manufacturer": "Sony Corporation",
            "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1"})

        print(len(devs))
        return devs

    def info_from_entry(self, entry):
        model = entry.description["device"]["modelName"]
        name = entry.description["device"]["friendlyName"]
        host = urlparse(entry.values['location']).hostname
        d = {"name": name, "model": model, "host": host}
        return d
