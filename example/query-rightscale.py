#!/usr/bin/env python

import sys
import json

from rightscale import RightScale

# Setup your API access
accountid = 12345
username = 'username'
password = 'password'
rsapi = RightScale(accountid, username, password)

# Try to find myself (this server) in RightScale.
# Returns None if you are not on RS system
myself = rsapi.whoami()

if myself is not None:
    # Find all servers (including myself) in my deployment.
    servers = [s for s in rsapi.servers if s.deployment_href == myself.deployment_href]
else:
    print "This system is not found in RightScale."
    # Or just find all servers across all deployments
    servers = [s for s in rsapi.servers]

tagged = dict()
for server in servers:
  #print server
  #print server.tags
  for tag in server.tags:
    #print tag
    tagged.setdefault(tag.name, list())
    tagged[tag.name].append(server)

data = dict()

# data["deployment"] = myself.deployment.nickname
# data["name"] = myself.nickname
data["servers"] = dict()
for server in servers:
  data["servers"][server.nickname] = {
    "ip_address": server.settings.ip_address,
    "private_ip_address": server.settings.private_ip_address,
    "tags": [t.name for t in server.tags],
  }

# Pretty-print the json so it's easily human-readable
print json.dumps(data, indent=2)
