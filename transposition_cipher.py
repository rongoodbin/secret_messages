import string
from ciphers import Cipher
import math
import helper_functions as help


class Transposition(Cipher):

    def __init__(self):
       self.ALPHABET  = string.ascii_uppercase
       self.ALPHABETLIST = [char for char in string.ascii_uppercase]

    def getNumericalKeyword(self, keyword):
        numlist = []
        orderedkeyword = sorted(keyword)
        l  = [str(s) for s in range(1,len(orderedkeyword)+1)]
        ordermap = dict(zip(orderedkeyword,l))
        for char in keyword:
            numlist.append(ordermap[char])
        print(numlist)
        nummap = {}
        for i,num in enumerate(numlist):
            #print(num,numlist.index(num))
            #nummap[numlist.index(int(num))] = num
            nummap[num] = numlist.index(num)
        return nummap

    def get_list_by_column(self, column):
        str_list = []
        for row in self.matrix:
            print(row)
            val = row[column]
            if val is not None:
               str_list.append(row[column])
        return "".join(str_list)


    def encrypt(self, text, keyword):

       self.numeric_map = self.getNumericalKeyword(keyword)
       columnlen = len(keyword)
       textlen  = len(text)
       rowlen = math.ceil(textlen/columnlen)
       self.matrix = [[None for x in range(columnlen)] for y in range(rowlen)]
       textlist = [s for s in help.remove_nonletters(text).upper()]

       for row in self.matrix:
           for i,cell in enumerate(row):
               try:
                  char = textlist.pop(0)
               except:
                   continue
               if char not in string.ascii_uppercase:
                   continue
               row[i] = char

      # for i in self.matrix:
      #    print(i)

       for z in sorted(self.numeric_map):
           print(self.get_list_by_column(self.numeric_map[z]))


    def decrypt(self, text):
       pass

if __name__ == "__main__":


  keyword = "ZEBRAS"
  text  = "WE ARE DISCOVERED FLEE AT ONCE"

  t = Transposition()
  t.encrypt(text,keyword)
  """
  print(len(text))
  w, h = 8, 5;
  matrix = [[0 for x in range(w)] for y in range(h)]
  for i in matrix:
      print(i)
  """