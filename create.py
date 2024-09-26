#!/usr/bin/env python3

import secrets
import base64
import zlib

token = "magls_"

central_token = secrets.token_bytes(26)

end_checksum = base64.b64encode(zlib.crc32(
                central_token
            ).to_bytes(4, 'little'))

print(token+base64.b64encode(central_token).decode("utf-8")[:-2]+end_checksum.decode("utf-8")[:-2])
