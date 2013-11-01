import nmap
from scanflask import store
from ipaddress import ip_address, ip_network

class NmapScan():
  def __init__(self, network, ports):
    self.ip = ip_network(network)
    self.ports = ports
    self.results = {}
    self.nm = nmap.PortScanner()

  def run(self):
    for ip in self.ip:
      self.results[str(ip)] = self.parseScan(self._scan(ip))
    return self.results

  def _scan(self, ip):
    self.nm.scan('ip', self.ports)
    return {'ip': str(ip)}

  def parseScan(self, results):
    scan = {}
    scan['up'] = ''
    scan['hostname'] = ''
    scan['os'] = ''
    scan['ports'] = {}
    scan['time'] = ''
    return scan