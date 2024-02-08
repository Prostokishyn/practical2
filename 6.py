text=input("Введіть текст")
unique_char = set(text)
for c in unique_char:
    print(c, text.count(c))