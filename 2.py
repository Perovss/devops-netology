#!/usr/bin/env python3
import os
cd_dir=os.getcwd()
print(cd_dir)
#bash_command = ["cd ~/devops-netology/", "git status"]
#result_os = os.popen(' && '.join(bash_command)).read()
#is_change= False
#for result in result_os.split('\n'):
#    if result.find('новый файл') != -1:
#        prepare_result = result.replace('\tновый файл:    ', '')
#        print(os.getcwd()+"/devops-netology/"+prepare_result)
#    if result.find('изменено') != -1:
#        prepare_result = result.replace('\tизменено:    ', '')
#        print(os.getcwd()+"/devops-netology/"+prepare_result)
