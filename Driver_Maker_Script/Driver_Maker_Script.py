import subprocess
import customtkinter as ctk
import subprocess as sub
import os

NormalDelay = .10
BigDelay = 2


NormalDelay = .10
BigDelay = 5
color_mode_list = ['Dark', 'Light']
state = 3


def convert_button_func():
    global CFilePath
    CFilePath = ' '
    CFilePath = input_Entry.get()

    Script()
    input_Entry.delete(0, ctk.END)


def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)


def Script():
    global CFilePath

    if CFilePath.find(' ') != -1:
        cmd_output.insert(ctk.END, "="*48+'\n')
        cmd_output.insert(ctk.END, "Delete The Space From Folder Name\n ")
        cmd_output.insert(ctk.END, "="*48+'\n')

    else:
        Foldername = CFilePath.split('\\')[-1]

        if (CFilePath.find('.')) == -1 and CFilePath.endswith('"'):
            CFilePath = CFilePath[1:-1]
            Foldername = Foldername[:-1]
            state = 1
        elif CFilePath.find('.') == -1:
            state = 1
            pass
        else:
            cmd_output.insert(ctk.END, "="*48+'\n')
            cmd_output.insert(ctk.END, "Folder Required\n")
            cmd_output.insert(ctk.END, "="*48+'\n')
            state = 2
        if state == 1:
            Interface_Guard = Foldername + "_Interface"
            Config_Guard = Foldername + "_Cfg"
            Program_Guard = Foldername + "_Prog.c"
            Private_Guard = Foldername + "_Private"

            InterfacingFile = CFilePath + '\\' + Interface_Guard + '.h'
            ConfigFile = CFilePath + '\\' + Config_Guard + '.h'
            ProgramFile = CFilePath + '\\' + Program_Guard
            PrivateFile = CFilePath + '\\' + Private_Guard + '.h'

            try:
                # interfacing file
                sub.check_output(
                    f'echo #ifndef {Interface_Guard.upper()}_H_> {InterfacingFile}',shell=True)
                sub.check_output(
                    f'echo #define {Interface_Guard.upper()}_H_>> {InterfacingFile}',shell=True)
                sub.check_output(f'echo.>> {InterfacingFile}',shell=True)
                sub.check_output(f'echo #endif>> {InterfacingFile}',shell=True)

                # config file
                sub.check_output(
                    f'echo #ifndef {Config_Guard.upper()}_H_> {ConfigFile}',shell=True)
                sub.check_output(
                    f'echo #define {Config_Guard.upper()}_H_>> {ConfigFile}',shell=True)
                sub.check_output(f'echo.>> {ConfigFile}',shell=True)
                sub.check_output(f'echo #endif>> {ConfigFile}',shell=True)

                # program file
                sub.check_output(f'echo #include "{Private_Guard}.h"> {ProgramFile}',shell=True)
                sub.check_output(f'echo #include "{Config_Guard}.h">> {ProgramFile}',shell=True)
                sub.check_output(
                    f'echo #include "{Interface_Guard}.h">> {ProgramFile}',shell=True)
                sub.check_output(f'echo.>> {ProgramFile}',shell=True)

                # private file
                sub.check_output(
                    f'echo #ifndef {Private_Guard.upper()}_H_> {PrivateFile}',shell=True)
                sub.check_output(
                    f'echo #define {Private_Guard.upper()}_H_>> {PrivateFile}',shell=True)
                sub.check_output(f'echo.>> {PrivateFile}',shell=True)
                sub.check_output(f'echo #endif>> {PrivateFile}',shell=True)

                cmd_output.insert(ctk.END, "="*48+'\n')
                cmd_output.insert(ctk.END, f"Driver  = {Foldername} Driver\n")
                cmd_output.insert(ctk.END, "="*48+'\n')

                cmd_output.insert(ctk.END, "="*48+'\n')

                cmd_output.insert(
                    ctk.END, f"Interfacing File Extracted to : \n' '{InterfacingFile}'\n ")
                cmd_output.insert(ctk.END, "="*48+'\n')

                cmd_output.insert(
                    ctk.END, f"Private File Extracted to : \n' '{PrivateFile}'\n ")
                cmd_output.insert(ctk.END, "="*48+'\n')

                cmd_output.insert(
                    ctk.END, f"Config File Extracted to : \n' '{ConfigFile}'\n ")
                cmd_output.insert(ctk.END, "="*48+'\n')

                cmd_output.insert(
                    ctk.END, f"Program Files Extracted to : \n' '{ProgramFile}'\n ")
                cmd_output.insert(ctk.END, "="*48+'\n')

            except subprocess.CalledProcessError:
                cmd_output.insert(ctk.END,"Error extracting files :(\n ")


if __name__ == '__main__':

    # config my app
    ctk.ThemeManager.load_theme('blue')
    ctk.AppearanceModeTracker.set_appearance_mode('system')
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    icon_path="\icon.ico"
    app.iconbitmap(os.getcwd()+icon_path)
    app.title("Driver_Maker_Script\n ")
    app.geometry('600x548')
    app.resizable(False, False)
    app.grid_columnconfigure(2, weight=1)
    app.grid_rowconfigure(5 , weight=1)

    # opp

    titelfram = ctk.CTkFrame(
        app,
        border_width=0
    )

    setting_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    entry_frame = ctk.CTkFrame(
        app,
        border_width=0
    )
    

    maker_label = ctk.CTkLabel(
        titelfram,
        width=600,
        text="Driver_Maker_Script",
        font=ctk.CTkFont('Arial', 48, weight='bold'),
        text_color="#2888C9"
    )

    note_lable = ctk.CTkLabel(
        titelfram,
        text="Note : Driver Folder Must have no spaces",
        font=ctk.CTkFont('Arial', 20, weight='bold'),
    )

    apperance_Label = ctk.CTkLabel(
        setting_frame,
        text="Appearance Mode",
        font=ctk.CTkFont('Arial', 18, weight='bold'),
    )
    
    owner_label1 = ctk.CTkLabel(
        setting_frame,
        text="Made with 💖 By",
        font=ctk.CTkFont('Arial', 15, weight='bold'),
    )
    owner_label2 = ctk.CTkLabel(
        setting_frame,
        text="Osama Abd EL Mohsen",
        font=ctk.CTkFont('Arial', 15, weight='bold'),
        text_color="#2888C9"
    )

    input_Entry = ctk.CTkEntry(
        entry_frame,
        placeholder_text="Enter Driver Folder Path Here",
        font=ctk.CTkFont('Arial', 20),
        width=400,
        height=48,
        border_width=0)

    convert_button = ctk.CTkButton(
        entry_frame,
        text="Make Driver",
        font=ctk.CTkFont('Arial', 20),
        command=convert_button_func, height=48)

    cmd_output = ctk.CTkTextbox(
        app,
    )

    apperance_button = ctk.CTkOptionMenu(
        setting_frame,
        font=ctk.CTkFont('Arial', 18),
        values=['system','dark','light'],
        command=change_apperance_mode, height=48)
    
    

    cmd_output = ctk.CTkTextbox(
        app
        
    )


    

    titelfram.grid(row=0, column=0, padx=10, pady=10,columnspan=3, sticky="ew")
    entry_frame.grid(row=3, column=1,columnspan=2,padx=(10, 10), pady=(10, 10), sticky="nsew")
    setting_frame.grid(row=5, column=1,rowspan=2, padx=(10, 10), pady=(10, 10), sticky="nwse")

    maker_label.grid(row=1, column=0, padx=10, pady=10)
    note_lable.grid(row=2, column=0, padx=10, pady=10)

    input_Entry.grid(row=3, column=0, padx=(10,10), pady=(10,10))
    convert_button.grid(row=3, column=4, padx=(10,10), pady=(10,10))


    apperance_Label.grid(row=4 ,column=1, padx=(10,10), pady=(10,10) ,sticky="nwse")
    apperance_button.grid(row=5, column=1, padx=(10,10), pady=(10,10), sticky="nwse")

    owner_label1.grid(row=8 ,column=1,padx=(10,10), pady=(100,0) ,sticky="nwse")
    owner_label2.grid(row=9 ,column=1,padx=(10,10), pady=(0,10) ,rowspan=2 ,sticky="nwse")

    cmd_output.grid(row=5, column=2,padx=10, pady=10,sticky="nwse")
    

    app.mainloop()
