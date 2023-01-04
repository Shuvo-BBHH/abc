import os,sys
def mahdi():
    os.system("clear")
    os.system("cls")
    print("""\033[1;32m  
╔═════════════════════════════════════════════════╗\033[1;31m
║           WELCOME TO MAHDI SHORTCUT             ║\033[1;33m
║═════════════════════════════════════════════════║\033[1;33m                     
║\033[0;37m##     ##    ###    ##     ## ########  ####     ║
║\033[1;92m###   ###   ## ##   ##     ## ##     ##  ##      ║
║\033[1;93m#### ####  ##   ##  ##     ## ##     ##  ##      ║
║\033[1;91m## ### ## ##     ## ######### ##     ##  ##      ║
║\033[1;92m##     ## ######### ##     ## ##     ##  ##      ║
║\033[1;93m##     ## ##     ## ##     ## ##     ##  ##      ║
║\033[1;33m##     ## ##     ## ##     ## ########  ####     ║ 
║                                    \033[1;33mVERSION 4.2  ║
║╭──────────────\033[1;91m[POWERED BY MAHDI HASAN ]\033[1;33m─────────║
│ ╭──────────────────────────────────────────────╮│
│ │ [A] AUTHOR   :\033[0;37mMAHDI HASAN SHUVO              ││
│ │ \033[1;32m[F] FACEBOOK :m.me/bk4human                  ││
│ │ \033[1;32m[G]GITHUB    : SHUVO-BBHH                    ││ 
│ │ \033[1;37m[W] WHATSAPP : 01616406924                   ││
│ ╰─\033[1;33m─────────────────────────────────────────────╯│
╰\033[1;33m─────────────────────────────────────────────────╯\033[1;32m""")
    print('\033[1;97m====================================================') 
    print('        \x1b[97m\033[37;41m[ WELL COME TO MAHDI SHOTCUT  ]\033[0;m')
    print('\033[1;97m====================================================') 
    print("\033[1;97m[01] \033[1;92mCONTACT ME         \033[1;96m")
    print("\033[1;97m[02] \033[1;92mFACEBOOK  ")
    print("\033[1;97m[03] \033[1;92mRANDOM CLOINIG TOOL ")
    print("\033[1;97m[04] \033[1;92mFILE CLONING TOLL ")
    print("\033[1;97m[05] \033[1;92mNET MIX OKK TOOL")
    print("\033[1;97m[06] \033[1;92mUPDATE")
    print("\033[1;97m====================================================")                    
    m=input('\033[1;97mCOUSE :')
    if m in['1','01']:
        os.system("xdg-open https://chat.whatsapp.com/+8801616406924")
    if m in['2','02']:
        os.system("xdg-open https://www.facebook.com/bk4human")
        os.system("xdg-open https://www.facebook.com/m4d1")

    if m in ['3','03']:
        os.system("rm -rf Random")
        os.system("git clone https://github.com/Shuvo-BBHH/Random")
        os.system("cd Random && python Mahdi.py")
    if m in['4','04']:
        os.system("rm -rf FILE")
        os.system("git clone https://github.com/Shuvo-BBHH/FILE")
        os.system("cd FILE && python mahdi.py")

    if m in['05','5']:
        os.system("rm -rf GREEN_CLONING")
        os.system("git clone https://github.com/Shuvo-BBHH/GREEN_CLONING")
        os.system("cd GREEN_CLONING && python Mahdi.py")
    if m in['6','06']:
        os.system('pip uninstall mahdi')
        os.system('pip install mahdi')



    elif m :
        mahdi()

    elif m in ['']:
        mahdi()    

mahdi()
