import re
abc=re.compile(r'(((\d\d\d)))-\d\d\d-(\d\d\d\d)')
search_string=abc.search('my phone is 408-643-5990')
print(search_string.group())
print(search_string.group(1))
print(search_string.groups())
print(f"searchSS_string is ----> {search_string.group()}")