import bz2

from demo_reader.util import writer

opener = bz2.open # decompress file during read

if __name__ == '__main__':
	writer.main(opener)