import sys

def countWords(filename):
    with open(filename, 'r') as myFile:
        fileText = myFile.read().replace('\n',' ')

    fileText.split();
    myFile.close

def main():
    Cat(sys.argv[1])

#standard boilerplate that calls the main function
if __name__ == '__main__':
    main()
