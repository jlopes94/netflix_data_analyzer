import secrets
import string
# just for testing things here and there


print(string.digits)

var = str(secrets.randbelow(100000000))
print(var.rjust(8, "0"))

