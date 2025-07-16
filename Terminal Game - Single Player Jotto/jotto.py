# python terminal game for jotto

import random

word_list = []
with open("words.txt", "r") as file:
    word_list = file.readlines()

for i in range(0, len(word_list)):
    word_list[i] = word_list[i].strip()

secret_word = word_list[random.randint(0,len(word_list)-1)]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Let's play Jotto!")
