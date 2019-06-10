import unidecode
import codecs

filepath = 'cacat_de_oaie.csv'
f = open('formatat.csv', 'w')

with codecs.open(filepath,'r', 'utf-8') as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       unaccented_string = unidecode.unidecode(line)
       f.write(unaccented_string)
       cnt += 1

f.close()
print(cnt)