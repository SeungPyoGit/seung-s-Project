import googletrans

trans = googletrans.Translator()

str1 = "안녕하세요. 파이썬 번역 코드 예제입니다."
str_result = trans.translate(str1, dest="en", src="auto")
print(str_result)
print(str_result.text)