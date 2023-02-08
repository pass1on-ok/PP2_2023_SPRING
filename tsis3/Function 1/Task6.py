def reverse_sentence(sent):
  words = sent.split()
  reversed_words = words[::-1]
  reversed_sentence = ' '.join(reversed_words)
  return reversed_sentence

sent = input()
print(reverse_sentence(sent)) 
