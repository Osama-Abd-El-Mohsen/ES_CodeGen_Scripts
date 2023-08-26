import os
import time
import subprocess


NormalDelay=.10
BigDelay = 2

def Script():

    os.system("color 03")
    print('''
    ██████╗░██╗░░░██╗  ██╗  ░█████╗░░██████╗░█████╗░███╗░░░███╗░█████╗░
    ██╔══██╗╚██╗░██╔╝  ╚═╝  ██╔══██╗██╔════╝██╔══██╗████╗░████║██╔══██╗
    ██████╦╝░╚████╔╝░  ░░░  ██║░░██║╚█████╗░███████║██╔████╔██║███████║
    ██╔══██╗░░╚██╔╝░░  ░░░  ██║░░██║░╚═══██╗██╔══██║██║╚██╔╝██║██╔══██║
    ██████╦╝░░░██║░░░  ██╗  ╚█████╔╝██████╔╝██║░░██║██║░╚═╝░██║██║░░██║
    ╚═════╝░░░░╚═╝░░░  ╚═╝  ░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

    ░█████╗░██████╗░██████╗░  ███████╗██╗░░░░░  ███╗░░░███╗░█████╗░██╗░░██╗░██████╗███████╗███╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██║░░░░░  ████╗░████║██╔══██╗██║░░██║██╔════╝██╔════╝████╗░██║
    ███████║██████╦╝██║░░██║  █████╗░░██║░░░░░  ██╔████╔██║██║░░██║███████║╚█████╗░█████╗░░██╔██╗██║
    ██╔══██║██╔══██╗██║░░██║  ██╔══╝░░██║░░░░░  ██║╚██╔╝██║██║░░██║██╔══██║░╚═══██╗██╔══╝░░██║╚████║
    ██║░░██║██████╦╝██████╔╝  ███████╗███████╗  ██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗██║░╚███║
    ╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚══════╝╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝''')


    print("="*70)
    time.sleep(.5)


    CFilePath = ' '
    CFilePath = input("""Drag & Drop Driver Folder Here : 
Note : Driver Folder Must have no spaces """)
    
    if CFilePath.find(' ') != -1 :
        os.system("color 04")
        print("Delete The Space From Folder Name")
        time.sleep(BigDelay)
        print("="*70)
        os.system("cls")
        Script()

    FolderNmae = CFilePath.split('\\')[-1]
    
    if (CFilePath.find('.')) == -1 and CFilePath.endswith('"'):
        CFilePath = CFilePath[1:-1]
        FolderNmae = FolderNmae[:-1]
    elif  CFilePath.find('.') == -1  :
        pass
    else:
        os.system("color 04")
        print("Folder Required")
        time.sleep(BigDelay)
        print("="*70)
        os.system("cls")
        Script()

    print(f"Driver  = {FolderNmae} Driver")

    Interface_Guard   =  FolderNmae + "_Interfac"
    Config_Guard      =  FolderNmae + "_Cfg"
    Program_Guard     =  FolderNmae + "_Prog.c"
    Private_Guard     =  FolderNmae + "_Private"
    


    InterfacingFile = CFilePath + '\\' + Interface_Guard +'.h'
    ConfigFile      = CFilePath + '\\' + Config_Guard +'.h'
    ProgramFile     = CFilePath + '\\' + Program_Guard
    PrivateFile     = CFilePath + '\\' + Private_Guard +'.h'

    try:
        os.system("color 02")
        #interfacing file
        os.system(f'echo #ifndef {Interface_Guard.upper()}_H_> {InterfacingFile}')
        os.system(f'echo #define {Interface_Guard.upper()}_H_>> {InterfacingFile}')
        os.system(f'echo.>> {InterfacingFile}')
        os.system(f'echo #endif>> {InterfacingFile}')

        #config file
        os.system(f'echo #ifndef {Config_Guard.upper()}_H_> {ConfigFile}')
        os.system(f'echo #define {Config_Guard.upper()}_H_>> {ConfigFile}')
        os.system(f'echo.>> {ConfigFile}')
        os.system(f'echo #endif>> {ConfigFile}')

        #program file
        os.system(f'echo #include "{Private_Guard}.h"> {ProgramFile}')
        os.system(f'echo #include "{Config_Guard}.h">> {ProgramFile}')
        os.system(f'echo #include "{Interface_Guard}.h">> {ProgramFile}')
        os.system(f'echo.>> {ProgramFile}')


        #private file
        os.system(f'echo #ifndef {Private_Guard.upper()}_H_> {PrivateFile}')
        os.system(f'echo #define {Private_Guard.upper()}_H_>> {PrivateFile}')
        os.system(f'echo.>> {PrivateFile}')
        os.system(f'echo #endif>> {PrivateFile}')

        time.sleep(NormalDelay)
        print("="*70)
        time.sleep(NormalDelay)
        print(f"{'Interfacing File Extracted to':<30} {'->':>5} '{InterfacingFile}'")
        print(f"{'Private File Extracted to':<30} {'->':>5} '{PrivateFile}'")
        print(f"{'Config File Extracted to':<30} {'->':>5} '{ConfigFile}'")
        print(f"{'Program Files Extracted to':<30} {'->':>5} '{ProgramFile}'")
        print("="*70)
        time.sleep(BigDelay)
        os.system("cls")
        Script()

    except subprocess.CalledProcessError:
        os.system("color 04")
        print("Error extracting files :(")
        time.sleep(BigDelay)
        os.system("cls")
        Script()
    
    



Script()