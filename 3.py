text=input("Введіть текст")
words=text.split(' ')
reversed_words=' '.join(words[::-1])
print("Введений текст", text)
print("Текст з реверсированими словами", reversed_words)