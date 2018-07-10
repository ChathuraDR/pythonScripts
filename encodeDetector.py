import pkgutil
import os
import encodings

def all_encodings():
    modnames = set(
        [modname for importer, modname, ispkg in pkgutil.walk_packages(
            path=[os.path.dirname(encodings.__file__)], prefix='')])
    aliases = set(encodings.aliases.aliases.values())
    return modnames.union(aliases)

filename = 'enron1/emails/2140.2004-09-13.GP.spam.txt'
encodings = all_encodings()

for enc in encodings:
    try:
        with open(filename, encoding=enc) as f:
            print(enc, f.read())
    except Exception:
        pass