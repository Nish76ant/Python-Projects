What can this A.I. assistant do for you?
It can send emails for you.
It can play music for you.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.
It is capable of opening your code editor or IDE with a single voice command.
Enough talk! Let's start building our own Assistant

1 – Starting VS Code
I am going to use the VS Code IDE in this video. Feel free to use any other IDE you are comfortable d with. Start a new project and make a file called jarvis.py.

2 – Defining Speak Function
The and first and foremost thing for an A.I. assistant is that it should be able to speak. To make our Assistant. talk, we will make a function called speak(). This function will take audio as an argument, and then, it will pronounce it.


Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.

What is pyttsx3?
A python library which will help us to convert text to speech. In short, it is a text-to-speech library.
It works offline, and it is compatible with Python 2 as well the Python 3.
Installation:


In case you receive such errors: 

No module named win32com.client
No module named win32
No module named win32api
Then, install pypiwin32 by typing the below command in the terminal 

Creating Our main() function: 
Now, we will create a main() function, and inside this main() Function, we will call our speak function.

Code:

Whatever you will write inside this speak() function will be converted into speech. Congratulations! With this, our J.A.R.V.I.S. has its own voice, and it is ready to speak.

2- Defining Wish me Function :
Now, we are going to make a wishme() function, that will make our J.A.R.V.I.S. wish or greet the user according to the time of computer or pc. To provide current or live time to A.I., we need to import a module called datetime. Import this module to your program, by:

