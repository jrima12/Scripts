from nltk.corpus import words

#global vars:
#Intentionally hard coded so one can go in and remove letters if desired
lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
full_special = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','"',"'",'/','?','>','<','.',',','~','`']
special_characters = []
specific_words = []
full_use_list = []

def set_special():
    specials = input("please input all the special characters you want to use separated by spaces. if none, press enter: ")
    specials = specials.split()
    global special_characters
    for i in specials:
        special_characters += i

def set_specific_words():
    words = input("please input all the words you want to use separated by spaces. ")
    words = words.split()
    global specific_words
    for i in words:
        specific_words += i

def set_parameters():
    bool_use_lower = False
    bool_use_upper = False
    bool_use_digit = False
    bool_use_full_special = False
    bool_use_special = False
    bool_use_specific_words = False
    use_lower_case = input("Do you want to use all lower case letters? (y/Y or n/N) ")
    if(use_lower_case.lower() == "y"):
        bool_use_lower = True
    use_upper_case = input("Do you want to use all upper case letters? (y/Y or n/N) ")
    if(use_upper_case.lower() == "y"):
        bool_use_upper = True
    use_digits = input("Do you want to use all digits 0-9? (y/Y or n/N) ")
    if(use_digits.lower() == "y"):
        bool_use_digit = True
    use_full_special = input("Do you want to use all special characters (y/Y) or input your own (n/N)? ")
    if(use_full_special.lower() == "y"):
        bool_use_full_special = True
    else:
        set_special()
        if (special_characters != []):
            bool_use_special = True
    use_specific_words = input("Do you want to add specific words (y/Y or n/N) ")
    if(use_specific_words.lower() == "y"):
        set_specific_words()
        bool_use_specific_words = True
    return [bool_use_lower, bool_use_upper, bool_use_digit, bool_use_full_special, bool_use_special, bool_use_specific_words]

def generate_word(s,lower, upper,j,k, use_list, string_list, i):
    if(len(s) < lower):
        s = s + use_list[k]
        return generate_word(s,lower, upper,j,k, use_list, string_list, i)
    if(len(s) > upper):
        return string_list

    s = s[:i] + use_list[k] + s[i+1:]
    string_list += s
    print(s)
    if(k < j):
        return generate_word(s, lower, upper, j, k+1, use_list, string_list, i)
    else:
        k = 0 
        if i > len(s) - 1:
            return generate_word(s, lower + 1, upper, j, k, use_list, string_list, 0)
        else:
            return generate_word(s, lower, upper, j, k, use_list, string_list, i+1)


fileName = input("please type in the desired name for your worldist (include the .txt extension) ")
list_set = set_parameters()
potential_set = [lower_case_letters, upper_case_letters, digits, full_special, special_characters, specific_words]
use_set = []
for index, l in enumerate(list_set):
    if l == True:
        use_set += potential_set[index]
# print(use_set)
lower_value = int(input("what Wis the shortest length password? "))
upper_value = int(input("what is the longest length password? "))

n = len(use_set)
print(generate_word("",lower_value, upper_value, n, 0, use_set,[], 0))

# for i in range(lower_value, upper_value):
#     while True:

# for j in use_set:
#     print(j)

