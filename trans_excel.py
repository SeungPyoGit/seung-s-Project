import googletrans

#한글 포함된 텍스트 파일 열기
with open('123.txt', 'r', encoding='utf-8') as f:
    english_text = f.read()

#구글 번역을 사용하여 번역진행
trans = googletrans.Translator()
trans_result = trans.translate(english_text, dest='en')

#번역결과를 새 텍스트 파일로 저장
with open('123_result.txt', 'w', encoding='utf-8') as f:
    f.write(trans_result.text)