import sys

sys.path.append("..//")
import hello

uuid = "010c2c6dd46d94ab3f129697112f74b3a2367f75"
key = "0044"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "003", "hello", "true")