import random
import string

ALIAS_LENGTH = 8


def get_random_alias():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(ALIAS_LENGTH))
