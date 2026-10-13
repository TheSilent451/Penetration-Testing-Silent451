import base64
import json

def base64url_decode(input):
    rem = len(input) % 4
    if rem > 0:
        input += '=' * (4 - rem)
    return base64.urlsafe_b64decode(input)

header_encoded = "your_header_part"
payload_encoded = "your_payload_part"

header_json = json.loads(base64url_decode(header_encoded).decode('utf-8'))
payload_json = json.loads(base64url_decode(payload_encoded).decode('utf-8'))

print("Header:", header_json)
print("Payload:", payload_json)
