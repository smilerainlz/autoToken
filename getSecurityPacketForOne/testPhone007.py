import sys

sys.path.append("..//")
import hello

uuid = "984e38e08278e882dda3017fc916d873d457b13d"
key = "0035"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "007", "false")