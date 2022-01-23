#!/bin/bash


# Git Setup Multiple Repository
git remote add gitlab git@gitlab.com:progdevlab/e_sphere_framework.git
git remote set-url --add --push origin git@gitlab.com:progdevlab/e_sphere_framework.git

git remote add github git@github.com:ProgDevLab/E_Sphere_Framework.git
git remote set-url --add --push origin git@github.com:ProgDevLab/E_Sphere_Framework.git


# Display Config
git remote show origin

git config --list
