#!/usr/bin/env python3

# this file should have token validation and then decoding.

import base64
import zlib

def mt_decode(token):
    token = token.rstrip()
    start = "magls_"
    # length verification
    assert len(token) >= len(start) + 8
    # header verification
    assert token[0:len(start)] == start
    # retrieve token in bytes
    # big thanks to this gist https://gist.github.com/perrygeo/ee7c65bb1541ff6ac770?permalink_comment_id=3478388#gistcomment-3478388
    central_token = token[len(start):-6]
    central_token += '=' * ((4 - len(central_token) % 4) % 4)
    central_token = base64.b64decode(str.encode(central_token))

    end_checksum = token[-6:]

    calc_checksum = base64.b64encode(
            zlib.crc32(central_token).to_bytes(4, "little"))
    calc_checksum = calc_checksum.decode("utf-8").rstrip('=')
    # checksum verification
    assert calc_checksum == end_checksum

    return central_token

with open("tokens", "r") as file:
    for line in file:
        if (line[0] != '#'):
            print(base64.b64encode(mt_decode(line)).decode("utf-8").rstrip('='))

# if we make it here without any uncaught exceptions, all the tokens are correct
print("success")


