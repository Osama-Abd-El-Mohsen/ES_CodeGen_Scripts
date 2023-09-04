import os
import time
import subprocess

if __name__=='__main__' :

    NormalDelay=.10
    BigDelay = 5

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
        CFilePath = input("""Drag & Drop Python Script Here : """)
        if CFilePath.find('.py')== -1:
            os.system("color 04")
            print("="*70)
            print(f"{'Pls Drag Python Script':^70}")
            print("="*70)
            time.sleep(BigDelay)
            os.system("cls")
            Script()

        try:
            os.system("color 02")
            os.system(f'pyinstaller --onefile {CFilePath}')
            print("="*100)
            print(f"= {'your file extracted to folder called (dist) in your current directory':^96} =")
            print("="*100)
            time.sleep(BigDelay)
            print("="*70)
            os.system("cls")
            Script()

        except subprocess.CalledProcessError:
            os.system("color 04")
            print("Error extracting file :(")
            time.sleep(BigDelay)
            os.system("cls")
            Script()



    Script()