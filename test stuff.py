# open a file for reading
import codecs

myvar = codecs.open("mobyposi.i", "r",'utf-8')

# read in all data as one long string
alldata = myvar.read()

# close the file
myvar.close()

# dict_split = alldata.split()

for i in alldata:
    if i == "◊":
        print("hello world")
