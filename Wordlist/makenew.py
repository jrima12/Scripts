def parse_input_levels():
    pass

def main():
    filename = input("What is the name of your file (without any file extension. Ex: input test will make file test.txt)? - ")
    filename = input(
        """
        pick your levels
        1 - create list of input words (default is list of common words instead)
        2 - leet mode (replace letters with numbers leet => 1337)
        3 - sas mode (special characters involved as well sas => $@$)
        4 - include random numbers throughout the word
        5 - include random special characters throughout the word

        input can combine options with commas no spaces(example: 1,3,4)
        """
    )