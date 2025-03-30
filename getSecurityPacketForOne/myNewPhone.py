import sys

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0056"

# hello.doAll(uuid, key)
hello.doFromFileSendGift(uuid, key, "my", "hello", "588815", "package", "星星票")
# hello.doFromFileAll(uuid, key, "001")
