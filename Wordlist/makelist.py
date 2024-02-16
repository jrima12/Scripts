import sys
import makenew
import addto

def main():

    if(len(sys.argv) > 1):
        if sys.argv[1] == "-m":
            makenew.main()

        elif sys.argv[1] == "-a":
            addto.main()
    
        else:
            print("""
            USEAGE:
            $ python3 wordlist -arg
            args:
                -h - displays this menu option
                -m - makes a new or rewrites an existing wordlist
                -a - adds on to an existing wordlist    
            """)
    else:
            print(
        """
         _______ _    _ ______ 
        |__   __| |  | |  ____|
           | |  | |__| | |__   
           | |  |  __  |  __|  
           | |  | |  | | |____ 
           |_|  |_|  |_|______|
        
         ____  ______  _____ _______ 
        |  _ \|  ____|/ ____|__   __|
        | |_) | |__  | (___    | |   
        |  _ <|  __|  \___ \   | |   
        | |_) | |____ ____) |  | |   
        |____/|______|_____/   |_|   
        __          ______  _____  _____  _      _____  _____ _______ 
        \ \        / / __ \|  __ \|  __ \| |    |_   _|/ ____|__   __|
         \ \  /\  / / |  | | |__) | |  | | |      | | | (___    | |   
          \ \/  \/ /| |  | |  _  /| |  | | |      | |  \___ \   | |   
           \  /\  / | |__| | | \ \| |__| | |____ _| |_ ____) |  | |   
            \/  \/   \____/|_|  \_\_____/|______|_____|_____/   |_|   
                                                               
        USEAGE:
        $ python3 wordlist -arg
        args:
            -h - displays this menu option
            -m - makes a new or rewrites an existing wordlist
            -a - adds on to an existing wordlist                 
        """ 
    )
    
        
if __name__ == "__main__":
    main()