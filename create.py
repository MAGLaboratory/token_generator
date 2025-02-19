#!/usr/bin/env python3

import secrets
import base64
import zlib

def mt_encode():
    token = "magls_"
    
    central_token = secrets.token_bytes(28)
    
    end_checksum = base64.b64encode(zlib.crc32(
                    central_token
                ).to_bytes(4, "little"))
    
    central_token = base64.b64encode(central_token).decode("utf-8").rstrip('=')
    
    token += central_token 
    
    end_checksum = end_checksum.decode("utf-8").rstrip('=')
    
    token += end_checksum

    return token

print(mt_encode())
