import os
import Queue
from random import choice
from flask import session
from string import ascii_uppercase
from dropbox.client import DropboxClient

# Run a Breadth First Search
# Collect all file and folder meta data starting from the root
def BFS(client, contents, names, types, sizes, paths):
    Q = Queue()

    # Push all the items in root into queue
    for content in contents:
        Q.put(content)

    while not Q.empty():
        content = Q.get()
        names.append(os.path.basename(content["path"]))
        sizes.append(toKB(content["bytes"]))
        paths.append(content["path"])

        if(content["is_dir"]):
            types.append("Folder")
            folderMetadata = client.metadata(content["path"])
            contents = folderMetadata["contents"]
            for content in contents:
                Q.put(content)
        else:
            types.append("File")
    return

# Convert bytes to Kilo bytes
def toKB(bytes):
    return int(bytes / 1024);

# Convert bytes to Mega bytes
def toMB(bytes):
    return toKB(toKB(bytes));

# Find the space usage
def spaceUsage():
    client = DropboxClient(session['accessToken'])
    accountInfo = client.account_info()
    quotaInfo = accountInfo["quota_info"]
    total = quotaInfo["quota"]
    normal = quotaInfo["normal"]
    shared = quotaInfo["shared"]
    used = normal + shared
    return toMB(used), toMB(total - used)

# Get the file types and their total sizes
def getFileTypeSizes(names, sizes):
    hash = {}
    index = 0
    for name in names:
        if '.' not in name: continue
        type = os.path.splitext(name)[1][1:]
        type = type.upper()

        if type in hash:
            hash[type] = hash[type] + sizes[index]
        else:
            hash[type] = sizes[index]
        index = index + 1

    types = []
    totalSizes = []
    for key, value in hash.items():
        types.append(key)
        totalSizes.append(value)
    return types, totalSizes

# Generate color codes for the charts
def getColors(n):
    colors = []
    for i in range(1, n + 1):
        colors.append(getColorCode())
    return colors

# Get a random hexadecimal color code
def getColorCode():
    a = hex(random.randrange(0, 256))
    b = hex(random.randrange(0, 256))
    c = hex(random.randrange(0, 256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a) < 2: a = "0" + a
    if len(b) < 2: b = "0" + b
    if len(c) < 2: c = "0" + c
    z = a + b + c
    return "#" + z.upper()

# Generate a 32 digits secret key
def getSecretKey():
    return ''.join(choice(ascii_uppercase) for i in range(32))
