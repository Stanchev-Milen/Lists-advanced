#no_vowels_list = []
#text = input().lower()
#for i in range(len(text)):
#    char = text[i]
 #   if char == 'a' or char == 'o' or char == 'u' or char == 'e' or char == 'i' or char == ' ':
  #      continue
   # else:
     #   no_vowels_list.append(char)

#print(''.join(no_vowels_list))
###################################################################################################
#no_vowels_list2 = []
#vowels = ['a', 'o', 'u', 'e', 'i']
#text2 = input()

#for j in range(len(text2)):
 #   char2 = text2[j]
   # if char2 not in vowels:
  #      no_vowels_list2.append(char2)
#print(''.join(no_vowels_list2))
##################################################################################################
text3 = input()
vowels3 = ['a', 'o', 'u', 'e', 'i']
no_vowels_list3 = [chr for chr in text3 if chr not in vowels3]
print(''.join(no_vowels_list3))
