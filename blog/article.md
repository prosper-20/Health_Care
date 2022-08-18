# How to Connect a local repository to a Gitbhub Repository

 

In this article, I am going to show you how connect your local repository (A repository on your PC) to a remote repository (GitHub). This article is suitable for readers with no experience in Git. 

 

Before going deeper into this, It's necessary to know what git is..  

 

 

Now, that we have a basic understanding of what Git is, let's dive right into it. 

 

## 1. Create A Repository on Gitbhub 

Simply login into your Github account and click on the new button to create a new repo. For the same of this article, we are going to create a new repository using only default settings. 

 

## 2. Change directory into your local Project 

Next, we are to CD into our local Project via our git bash terminal. In our case, the file we want to Connect to github exists in the following path: 

> ` C:/Users/User/documents/python/index.py. `

Ensure that you activate your virtual environment if you have one. 

 

## 3. Initialize an empty repository in your project. 

To do this, simply run the git init command. You should get a response similar to this: 

 

 

## 4. Add the file to the staging area 

Simply run the git add -A command. The essence of this command is to add all files present in our repository to the remote repository. In our case, we have only one file which is our main.py file 

 

## 5. Commit the file  

Next, run the git commit -m command. The -m extension stands for message. The message is usually a brief description included by the user. It helps you identify the change made. 

 

## 6. Pushing to the remote repository

THE 2 previous steps were preparatory steps to this step. To push our files to the remote repository, run the following command: 

>`git remote add origin https://github.com/prosper-20/PROJECT.git `

 

Generic syntax: `git remote add origin https://github.com/<username>/<project_name>.git  `

 

git remote-v 