#!/bin/bash
git init
git remote remove main
git remote set-url origin https://github.com/asharien/BOJ_ProblemSolve13000-14000.git
git remote add origin https://github.com/asharien/BOJ_ProblemSolve13000-14000.git
git branch -m origin main
git branch
git remote -v
git status
git log

