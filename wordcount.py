#!/usr/bin/env python

import sys

def print_words(fname, toprint):
    charList = ['!',',','.','--','\'','\"','?',':','`',';', '(',')']
    with open(fname, 'r') as myFile:
        fileText = myFile.read().replace('\n',' ')
        myFile.close
    for ch in charList:
        if ch in fileText:
            fileText = fileText.replace(ch,' ')
    fileText = fileText.lower()
    wordList = fileText.split()
    # print(wordList)
    wordCount = {}
    for word in wordList:
         if wordCount.has_key(word) :
            #  print('New word:'+word)
             wordCount[word] += 1
         else:
            #  print('Old word:'+word)
             wordCount[word]=1

    if toprint:
        for w,c in sorted(wordCount.iteritems(), key=lambda (k,v): (v,k), reverse=True ):
            print '%s:%d' % (w,c)
    else:
        return wordCount

    return

def getFreq(item):
    return item[-1]

def sort_freq(wordList):
    print sorted(wordList.iteritems(), key=lambda (k,v): (v,k), reverse=True )[:10]
    return

def print_top(fname):
    wordList = print_words(fname, 0)

    sort_freq(wordList)

    return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename, 1)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
    main()
