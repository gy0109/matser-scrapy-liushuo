s = '6.2万+'
import re

print(float(re.search('\d+\.\d+', s).group()) * 10)