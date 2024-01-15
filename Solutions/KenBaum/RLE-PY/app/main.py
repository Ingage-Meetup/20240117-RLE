import utils



def main():
    print("Hello, World!")
    x = utils.add(1,3)
    print(x)
    import os
    print("Current Working Directory: ", os.getcwd())

    encoding = utils.rle(utils.readFile('app/files/iliad.txt'))
    utils.writeFile("app/files/iliad.encoding", encoding)

    # bmp = utils.load_bitmap('app/files/sample.bmp')
    # encoded_list = utils.run_length_encode(bmp)
    # encoding = ' '.join(str(item) for item in encoded_list)
    # utils.writeFile("app/files/samplebmp.encoding", encoding)


if __name__ == "__main__":
    main()