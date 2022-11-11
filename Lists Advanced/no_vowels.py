text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
text_wo_vowels = [no_vowel for no_vowel in text if no_vowel not in vowels]
final_text = ''.join(text_wo_vowels)
print(final_text)