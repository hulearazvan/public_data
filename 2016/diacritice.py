import unidecode
import codecs

filepath = 'radiate2.csv'
f = open('final2016_4.csv', 'w')

with codecs.open(filepath,'r', 'utf-8') as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       line = fp.readline()
       unaccented_string = unidecode.unidecode(line)
       f.write(unaccented_string)
       cnt += 1
f.close()