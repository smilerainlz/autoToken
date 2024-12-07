import sys

sys.path.append("..//")
import hello

uuid = "958249e4a70aff1b6514cd0cf64df32aeb9ecbb2"
key = "0034"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "004", "false")