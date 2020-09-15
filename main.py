import jieba
import gensim
import difflib
import pstats
import cProfile
import sys

path1=sys.argv[1]
path2=sys.argv[2]
path3=sys.argv[3]

f = open(path1,encoding='utf-8')   #设置文件对象
s1 = f.read()
f.close()
f = open(path2,encoding='utf-8')
s2 = f.read()
f.close()

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
result=(round(string_similar(s1,s2),2))

with open(path3,"a",encoding='utf-8') as f:	
		f.write(str(result))
		f.write("\n")

# import cProfile
# import re
# cProfile.run('re.compile("foo|bar")')
