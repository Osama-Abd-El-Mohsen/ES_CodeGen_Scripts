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



    CFilePath = input("Drag & Drop C File Here : ")

    if CFilePath.endswith('.c'):
        pass
    elif  CFilePath.endswith('.c"') :
        CFilePath = CFilePath[1:-1]
        print(CFilePath)
    else:
        os.system("color 04")
        print("C File Required")
        time.sleep(BigDelay)
        print("="*70)
        os.system("cls")
        Script()

    asm_file_path = os.path.splitext(CFilePath)[0] + ".s"
    prepros_file_path = os.path.splitext(CFilePath)[0] + ".i"
    output_file = os.path.splitext(CFilePath)[0] + ".exe"

    try:
        os.system("color 02")
        subprocess.run(["cpp", '-E', CFilePath, '-o', prepros_file_path], check=True)
        time.sleep(NormalDelay)
        print("="*70)
        time.sleep(NormalDelay)
        print(f"{'PreProcessor code Extracted to':<30} {'->':>5} '{prepros_file_path}'")

        subprocess.run(["gcc", "-S", CFilePath, "-o", asm_file_path], check=True)
        time.sleep(NormalDelay)
        print("="*70)
        time.sleep(NormalDelay)
        print(f"{'Assembly code Extracted to':<30} {'->':>5} '{asm_file_path}'")

        subprocess.run(["gcc", CFilePath, "-o", output_file], check=True)
        time.sleep(NormalDelay)
        print("="*70)
        time.sleep(NormalDelay)
        print(f"{'Eex File Extracted to':<30} {'->':>5} '{output_file}'")
        time.sleep(NormalDelay)
        print("="*70)
        time.sleep(BigDelay)

    except subprocess.CalledProcessError:
        os.system("color 04")
        print("Error extracting files :(")
        time.sleep(BigDelay)
        os.system("cls")
        Script()
    
    def Options():
        os.system("cls")
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
        Option = int(input(""" Select Option --- Options :
            0- To Exit
            1- To See Your Code Output
            2- To Start Script Again 
"""))
        print("="*70)

        if Option in range(0,3): 
            if Option ==0 :
                print("bye :)")
                time.sleep(BigDelay)
                exit(0)
            elif Option == 1 :
                os.system(f"{output_file}")
            else :
                os.system("cls")
                Script()
        else :
            print("="*70)
            print("Pls Select Option From 0 to 2")
            print("="*70)
            time.sleep(BigDelay)
            os.system("cls")
            Options()
    Options()



Script()