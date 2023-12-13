#!/usr/bin/env python3

# Description: This script shows how to use string.methods().


sentence = "    DevOps is COOL!    "
length = len(sentence)
lower_case = sentence.lower()
upper_case = sentence.upper()
stripped_sentence = sentence.strip()
splitted_sentence = sentence.split()
joined_sentence = ' '.join(splitted_sentence)

print(sentence)
print(length)
print(lower_case)
print(upper_case)
print(stripped_sentence)
print(splitted_sentence)
print(joined_sentence)

