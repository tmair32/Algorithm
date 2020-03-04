import sys
import base64
sys.stdin = open("1928.Base64 Decoder.txt")

T = int(input())
for tc in range(1, T+1):
    encoding = input()
    decode = base64.b64decode(encoding)
    result = decode.decode("UTF-8")
    print("#{} {}".format(tc, result))