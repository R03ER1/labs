#!/usr/bin/env python3

import sys
url = sys.argv[1]

scheme = url.split("://")[0]
print("scheme: " + scheme)
host = url.split("/")[2].split(":")[0]
print("host: " + host)
if len(url.split(":")) > 2:
    port = url.split("/")[2].split(":")[1]
    print("port: " + port)
path = "/" + url.split("/")[3].split("?")[0]
if len(url.split("/")) > 4:
    path += "/" + url.split("/")[4].split("#")[0].split("?")[0]
print("path: " + path)

if "?" in url:
    query = url.split("?")[1].split("#")[0]
    print("query-string: " + query)
if "#" in url:
    fragment = url.split("#")[1]
    print("fragment-id: " + fragment)
