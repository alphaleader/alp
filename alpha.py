from socket import *

print("-------------------------------------------")
print('|                  |^_^|                  |')
print('|       coded by alpha leader        |')
print('|   telegram >>> @alpha_leader   |')
print("-------------------------------------------")
print()
print()
#-----------------------------------------------------------------
apt_list = [' 01 >>> get ip site', ' 02 >>> wp tools hacking [file maker]', ' 03 >>> get user name wordpress',' 04 >>> about me']
print(apt_list[0])
print(apt_list[1])
print(apt_list[2])
print(apt_list[3])
#----------------------list tools codes functions------------------------------------------

def ip_site():
    print(gethostbyname(input('enter target>>>')))
def w_f_p():
     print("wp tool")
     lord = input("enter target>>>")
     wp_lists = ['/wp-admin','/wp-content', '/wp-includes', '/wp-config.php','wp-login.php','/wp-mail.php'
                 ,'/wp-content/language','/wp-content/plugins','/wp-content/themes','/wp-content/upgrades'
                 ,'/wp-content/uploades']
     for wp_lista in wp_lists:
         print(lord + wp_lista)
def get_user_wp():

    jdk = input('enter target wordpress>>>')
    f8 = "/wp-json/wp/v2/users"
    print("1-first copy url and open in browser")
    print("2- the username is the name front[name : usernname")
    print("your url:>>>")
    print("#-------------#")
    print( jdk + f8)
    print("#-------------#")

def about():
    print('created by alpha learer')
    print("connect")
    print("telegram > @ALPHA_LEADER")
    
#------------------end of functions files---------------------------------------------------------
ifrom = input("alpha>")
if ifrom == "01" or ifrom == "1":
    ip_site()
    
elif ifrom == "02" or ifrom == "2":
    w_f_p()
    
elif ifrom == "03" or ifrom == "3":
    get_user_wp()
    
elif ifrom == "04" or ifrom == "4":
    about()
    
else :
    print("this tool is not to list")
    
