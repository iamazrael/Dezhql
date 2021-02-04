import os, colorama, sys
colorama.init()

banner = colorama.Fore.CYAN+'''
    ┌═════════════════════════════════════════════════┐
    █                     Dezhql                      █
    █             choose one of options               █
    █                                                 █
    └═════════════════════════════════════════════════┘\n'''

problems = colorama.Fore.CYAN+'''
_________________________
1 > i can not install pip|
2 > module not found     |
3 > exit                 |
-------------------------
[+] for more problems please ask your qoestions in github => issues\n'''

def install():

    while True:
        print(banner)
        print(colorama.Fore.CYAN+'''
-------------
1 > install
2 > problem
3 > exit
------------\n''')
        command = input(colorama.Fore.CYAN+'Dezhql ➮ ')
        
        if command == '3':
            print(colorama.Fore.RED+'\n[-] Bye bro')
            sys.exit()

        if command == '1':
            os.system('pip3 install halo && pip3 install requests && pip3 install bs4')

        if command == '2':
            print(problems)
            command_ = input(colorama.Fore.CYAN+'Dezhql ➮ ')
            
            if command_ == '1':
                os.system('curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
                os.system('python3 get-pip.py')
            
            if command_ == '2':
                os.system('pip3 install random && pip3 install halo && pip3 install requests && pip3 install bs4')
            
            if command_ == 'exit':
                sys.exit()


install()