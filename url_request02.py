import urllib.parse

#url 속 한글을 바꿔주는 퍼센트 인코딩 함수

a = urllib.parse.quote('파이썬')
print(a)

b = urllib.parse.unquote(a)
print(b)