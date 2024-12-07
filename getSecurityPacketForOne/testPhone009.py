import sys

sys.path.append("..//")
import hello

uuid = "784edd8dada37967246b1a3ddaf85118a3afecab"
key = "0036"

# hello.doAll(uuid, key)
hello.doFromFile(uuid, key, "009", "false")
