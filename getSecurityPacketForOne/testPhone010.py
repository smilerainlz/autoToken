import sys

sys.path.append("..//")
import hello

uuid = "1ad586521d7b19709f5e122396c02373b7cab150"
key = "0036"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "010", "false")
