import random
import pyperclip
from string import digits
from string import punctuation
from string import ascii_letters

def copy_toclipboard(vartocopy):
    pyperclip.copy(vartocopy)

def pass_gen(num):
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols) for i in range(num))
    copy_toclipboard(password)
    return password

def main(pass_request):
    return pass_gen(pass_request)

