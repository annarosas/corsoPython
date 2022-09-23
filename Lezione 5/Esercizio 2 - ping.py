# ping su sistema windows
import os
def ping(indirizzo):
    return not os.system('ping %s -n 1' % (indirizzo,))

ping('www.google.com')