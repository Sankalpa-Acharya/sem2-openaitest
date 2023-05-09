

with open('text.txt', 'r') as f:
  with open('new_text.txt', 'w') as new_f:
    for line in f:
      for word in line.split():
        if word not in ['a', 'the', 'an']:
          new_f.write(word + ' ')