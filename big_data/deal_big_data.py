def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'r') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


temp = read_file("D:/Data/test/ODS_MDS.css_enduser20190408_1.dat")
for i in temp:
    print(i)
