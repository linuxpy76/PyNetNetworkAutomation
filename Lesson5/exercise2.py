import re

with open("show_ip_bgp_neighbors.txt", mode="r") as f:
    data = f.read()

bgp_neighbor_ip = r"(?P<bgp_neighbor_ip>\d+\.\d+\.\d+\.\d+)"
remote_as = r"(?P<remote>\d\d)"
bgp_version = r"(?P<bgp_ver>\d)"
remote_router_id = r"(?P<remote_router_id>\d+\.\d+\.\d+\.\d+)"
bgp_state = r"(?P<bgp_state>\w+?)"

bgp = re.search(rf"^BGP.+?{bgp_neighbor_ip},", data, flags=re.MULTILINE)
remote = re.search(rf"^BGP.+?remote\sAS\s{remote_as}", data, flags=re.MULTILINE)
bgp_ver = re.search(rf"^\s\sBGP\sversion\s{bgp_version},", data, flags=re.MULTILINE)
remote_router = re.search(rf"^\s\sBGP.+?{remote_router_id}$", data, flags=re.MULTILINE)
bgp_state = re.search(rf"^\s\sBGP\sstate\s=\s{bgp_state},", data, flags=re.MULTILINE)



print("BGP neighbor: " + bgp.group("bgp_neighbor_ip"))
print("Remote AS version: " + remote.group("remote"))
print("BGP version: " + bgp_ver.group("bgp_ver"))
print("BGP neighbor: " + remote_router.group("remote_router_id"))
print("BGP neighbor: " + bgp_state.group("bgp_state"))