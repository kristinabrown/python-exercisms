
def is_isogram(string):
    # import code; code.interact(local=locals())
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        count = string.lower().count(char)
        if count > 1:
            return False

    return True
