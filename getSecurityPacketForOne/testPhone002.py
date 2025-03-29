import sys

sys.path.append("..//")
import hello

uuid = "c933eea94b3ba611f48322b9d9ebc02e9c1efef1"
key = "0055"

hello.doAll(uuid, key)
# hello.doFromFile(uuid, key, "002", "hello", "false")
#hello.doFromFileAll(uuid, key, "002")