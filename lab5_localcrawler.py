
import ntpath
import os
import sys


#for path of txt files
from os.path import join

#storing number of files
count = 0

#saving names of text files
files = {}


#hashtable 
wordcount = 0
ddict = {}


#Searching text files
mydir = "E:\"#use your own computers path here

#Indexing the Files
for root, dirs, files in os.walk(mydir):
    for file in files:
        if file.endswith(".txt"):
            count = count + 1
            Files[str(count)] = join(root, file.title())




for a in range(1,count+1,1):
      with open(Files[str(a)],"r") as f:
        for line in f:
            for word in line.split():
                wordcount = wordcount + 1
                if word in ddict.keys():
                       
                        print("Duplicate found")
                        wordDict[word] = wordDict[word] + "," + str(a)
                else:
                    wordDict[word] = str(a)
                    print("New word found")
                    
print ("Word Count: " + str(wordCount))
print("\n")
print("\n")
print ("Files Found: " + str(count))
print("\n")



while(1):
    s = str(raw_input("Enter term"))
    s=s.lower()
    result = ""

    #Checking for filenames
    for a in range(1, count + 1, 1):

        loc, fname = os.path.split(Files[str(a)])

        if s.lower() in [f.lower() for f in fname.split(".")]:
            print ("Filename found: " + Files[str(a)])
            

    if s in ddict.keys():
        result = ddict[sTerm]
        result = result.split(",")
        tmp = ""

        for x in result:

            
            if tmp != x:
                print("Found In " + Files[str(x)] + "\n")
            tmp = x
    else:
        print("Search Term Not Found In File Contents!")
         print("\n")


        #Muhammad Hamza Nasim
         #112361

