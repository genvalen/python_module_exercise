import sys

def main(opener):
    f = opener(sys.argv[1], mode='wt')
    print("object type:", type( f))
    f.write(' '.join(sys.argv[2:])) # data to compress
    f.close()

