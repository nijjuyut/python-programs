#program to check check for string palindrome

#take user input
S1 = input('Enter the String :')
#initialize string and save reverse of 1st string
S2 = S1[::-1]
#check if both matches
if S1 == S2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')
