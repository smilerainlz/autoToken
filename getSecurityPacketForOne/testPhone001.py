import sys

sys.path.append("..//")
import hello

uuid = "08771801cd4ba47bd323204310a296c6e05e2b1a"
key = "0034"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "001", "hello")
