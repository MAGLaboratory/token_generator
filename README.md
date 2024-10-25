# token_generator

This is the MAG Laboratory token generator

## Branch Description
This branch contains the inital revision of the generator before it has reached
a level of maturity necessary for a `main` branch.

## Format
### AS S-First (Application Specific String)
The tokens start with an application specific text string before an underscore.
Most applications should parse for their target string.

### Token
The next part of the token string is a base64 encoded token.  This token is
encoded in the default big-endian order.

### CRC32
The last part of the token string is a crc32 of the decoded token.  The data
is entered into the crc32 calculation in the same big-endian order as it is
presented through base64.  The crc32 is encoded in little-endian format.

Note that the CRC32 format and polynomial are consistent with the default CRC32
which is also called "ISO-HDLC", "ISO 3309", "ITU-T V.42", "CRC-32-IEEE",
_et cetera._
