import sys, os
import database as db

if len(sys.argv) == 1:
    print("Syntax: python3 dump.py DATABASE [PREFIX]")
    exit(0)

test = db.Tess2Database(sys.argv[1])
test.dump(sys.argv[2]+"_" if len(sys.argv) > 2 else os.path.splitext(os.path.basename(sys.argv[1]))[0]+"_")
