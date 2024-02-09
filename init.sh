#!/bin/bash
git init
git remote remove main
git remote set-url origin https://github.com/asharien/BOJ_ProblemSolve13000-14000.git
git remote add origin https://github.com/asharien/BOJ_ProblemSolve13000-14000.git
git branch -m origin main
git remote -v
git pull origin main
git config pull.rebase true
git branch --set-upstream-to=origin/main

