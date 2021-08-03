import gzip

from demo_reader.util import writer

opener = gzip.open # decompress file during read

if __name__ == '__main__':
	writer.main(opener)