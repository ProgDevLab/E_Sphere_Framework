"""
E Sphere Framework Install Script
"""

# Generic Libs
import os
import json

CONFIG_FILE = "install.yml"

__author__ = "ProgOwer"
__copyright__ = "Copyright 2022, E Sphere Framework Install Script"
__credits__ = ["ProgOwer"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "ProgOwer"
__email__ = "progower0770@gmail.com"
__status__ = "Production"


def getConfig(path):
    data = None
    with open(path, 'r') as stream:
        data = json.load(stream)
    return data


def cloneProject(main_git_url):
    if not os.path.exists(".git"):
        os.popen(f"git clone {main_git_url} git_tmp")
        os.popen("mv -R git_tmp/.git .")


def configureGit(git_list):
    if not os.path.exists("tools"):
        os.makedirs("tools")

    with open('tools/git.sh', "w") as file:
        file.write("#!/bin/bash\n\n")
        file.write("# Git Repository\n")

        for gitName in git_list:
            file.write(f"git remote add {gitName} {git_list.get(gitName)}\n")
            file.write(f"git remote set-url --add --push origin {git_list.get(gitName)}\n\n")

        file.write("# Display Config\n")
        file.write("git remote show origin\n")
        file.write("git config --list\n")

    os.popen("tools/git.sh")


def searchAndReplace(fileList, searchAndReplaceList):
    for file in fileList:
        fileData = ""

        with open(file, 'r') as file_raw:
            fileData = file_raw.read()
        
        for word in searchAndReplaceList:
            fileData = fileData.replace('word', searchAndReplaceList.get(word))
        
        with open(file, 'w') as file_raw:
            file_raw.write(fileData)


if __name__ == '__main__':
    print("Init Installation Script ...")

    print("Read Config file ...")
    config = getConfig(path=CONFIG_FILE)

    print("Clone Git Project ...")
    cloneProject(main_git_url=config.get('main_git'))

    print("Configure Git Project ...")
    configureGit(git_list=config.get('gitList'))

    print("Search and Replace in each files ...")
    searchAndReplace(
        fileList=config.get('fileList'),
        searchAndReplaceList=config.get('searchAndReplaceList'))

    print("Complete Installation !")
    exit(0)
