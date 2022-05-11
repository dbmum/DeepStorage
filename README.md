# Overview

I am a software engineer who is always looking for a challenge and for a new way to integrate my ideas. I love the act of solving coding puzzles!

This program is a very base level social media - type platform using Firebase, a cloud database, for the storage of all of the user and post data. This includes post making, updating your password, deleting your account and viewing the general post feed. When you sign in you are authenticated for your current session in the program until you log out.

I wrote this software mainly to learn about and practice with cloud databases. I wanted to learn this technique on how to make my programs accessible to more people by providing storage in an online space. 


[Software Demo Video](https://youtu.be/o3E71fg_hEk)

# Cloud Database

I am using Google Firebase, a free online database with lots of the built in networking, authetification, and other file storage that you could want for small project, with paid application as well for scaled up projects.

The database I created features two collections, 'Posts' and 'Users', with documents and fields that the user helps populate. Users is mainly used for initial authentification, and posts is used once your are actually inside the app.

# Development Environment

Google Firebase

VS Code

Python3 with the firebase_admin library and the OS library

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Firebase Admin Documentation](https://firebase.google.com/docs/reference/admin)
* [Youtube tutorial](https://www.youtube.com/watch?v=UVzBQ0LkO28)

# Future Work


* More secure Username and password authentification.
* Designing of 'posts' collection to be able to view them based off of most recent and view only a few.
* The functionality to update posts that you post.