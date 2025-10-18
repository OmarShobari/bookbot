def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_map = {}
    for char in text:
      char = char.lower()
      if char in char_map:
        char_map[char] +=1
      else:
        char_map[char] = 1
    return char_map
