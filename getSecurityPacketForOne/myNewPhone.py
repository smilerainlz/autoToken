import sys

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0049"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "my", "hello", "false")
# hello.doFromFileAll(uuid, key, "001")