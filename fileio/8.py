



with open('text.txt', 'r') as file:
  data = file.read()

words = data.split()
words_without_a = [word for word in words if word != 'a']
words_without_the = [word for word in words_without_a if word != 'the']
words_without_an = [word for word in words_without_the if word != 'an']

new_data = ' '.join(words_without_an)

with open('new_text.txt', 'w') as file:
  file.write(new_data)