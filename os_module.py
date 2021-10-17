# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 08:45:14 2021

@author: vijay kalimuthu
"""
import os

#segment1 - To know the class&method in os package 
dir(os)  

#segment2 - To know the current working directory 
os.getcwd()

#segment3 - Navigate to the directory furhter
os.chdir("complete path to the directory for change")

#segment4 - To list the list of file in certain directory
os.listdir()

#segment5 - To create new folder in particular directory
os.mkdir("name of the folder you want to create ")

#segment6 - To remove folder in particular directory
os.rmdir("name of the folder you want to remove")

#segment7 - To rename the folder
os.rename("exist name","new name")

#segment8 - To walk through path,directory,files in given path
for path,direct,file in os.walk("name of the directory you want to walk"):
    print(path)
    print(direct)
    print(file)
    
#segment9  
os.getlogin() #To know the name of login
os.cpu_count() #To know no of cpu
os.getpid() #To know the processing ID
os.name #To know the name of os







    



