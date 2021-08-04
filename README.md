# How To Use
Create a compressed file:

```
$ python -m demo_reader.compressed.<ziptype> <filename> <message>
``` 

Examples
```
$ python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
$ python -m demo_reader.compressed.gzipped test.gz data compressed with gzip
```

Read a compressed file:
```
$ python -m multi-reader-program <filename>
```

Examples:
```
$ python -m multi-reader-program test.bz2
data compressed with bz2

$ python -m multi-reader-program test.gz
data compressed with gzip
```