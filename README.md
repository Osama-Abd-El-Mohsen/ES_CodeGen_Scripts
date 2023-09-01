# ES_CodeGen_Scripts
`ES_CodeGen_Scripts`  is a collection of Python scripts designed to streamline the process of generating microcontroller driver files.  also helping to extract assembly and processing files (.i &amp; .s)

# 🛠️ Technologies Used:
- Python: Scripting and automation
- GCC: Compilation, preprocessing, and 
- CMD



# Scripts:

## 1 [Driver_Maker_Script.py](https://github.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/tree/main/Driver_Maker_Script#readme) : 

Driver_Maker_Script.py is a Python script to automate the extraction of Microcontroller Driver Files  . 
This script takes Driver_Empty Folder  and generates corresponding header and source files with file guard.

- `Driver_Cfg.h` `With File Gaurd`
- `Driver_Interfac.h` `With File Gaurd`
- `Driver_Private.h` `With File Gaurd`
- `Driver_Program.c` `With .h Driver Files Include`

# Usage 

1- Drag C File into the script

![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image.png)

![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image-1.png)


2- Hold off until the script is done executing.

![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image-2.png)

# Result
![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image-3.png)

|.C File| .h Files |
|--|--|
|![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image-4.png) |![Alt text](https://raw.githubusercontent.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/main/Driver_Maker_Script/image-5.png)|


## 2 [c_preprocess_extractor](https://github.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/tree/main/c_preprocess_extractor_python#readme) : 
c_preprocess_extractor.py is a Python script to automate the extraction of preprocessed C source code (.i files) and assembly code (.s files) from input C files. This tool streamlines the compilation process while providing developers with valuable insights into their code's preprocessing and assembly stages.

# Usage 

![Alt text](https://github.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/blob/main/c_preprocess_extractor_python/myFile8-24-2023_85531_AM-1.gif?raw=true)

1- Drag C File into the script

![image](https://github.com/Osama-Abd-El-Mohsen/c_preprocess_extractor/assets/62304741/a3092f90-57bc-4fc4-b8cb-19ab46d34638)


![image](https://github.com/Osama-Abd-El-Mohsen/c_preprocess_extractor/assets/62304741/edf4f356-36c3-476c-a797-21a5785e7781)

2- Hold off until the script is done executing.

![image](https://github.com/Osama-Abd-El-Mohsen/c_preprocess_extractor/assets/62304741/bf85c200-5938-4d0c-a6b7-fe2318c59225)

3- Then you can Exit - see your file output and start the script again


![image](https://github.com/Osama-Abd-El-Mohsen/c_preprocess_extractor/assets/62304741/e1354e67-9f85-4e2a-913c-13663c8ad6f8)

 # Downlaoding :
you can download the latest verison from the link below ⬇️

# [Download Me](https://github.com/Osama-Abd-El-Mohsen/ES_CodeGen_Scripts/releases/tag/v3.0)


Contributions to ES_CodeGen_Scripts are welcome! If you have ideas for improvements, bug fixes, or additional features, feel free to open issues or pull requests.
