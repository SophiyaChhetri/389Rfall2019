# Writeup 2 - Pentesting

Name: Sophiya Chhetri
Section: 0101
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri

## Assignment Writeup

### Part 1 (45 pts)

To get the flag, I first read the slides and command injection tutorial linked in the project description page. I also 
referred to following online tutorials:
-[7 Demonstration of Command Injection Attack](https://www.youtube.com/watch?v=BVI1-ikJ-xw)
-[Command Injection Explained - Part 1: The Basics](https://www.youtube.com/watch?v=dQ-_TO1zuvA)
-[Security tutorials](https://securitytutorials.co.uk/command-injection/)
-[command Injection cheatsheet](https://hackersonlineclub.com/command-injection-cheatsheet/)

At first I tried just with ip address(157.230.179.99) found from assignment2. Then I started testing with each commands
that I came across with while searching online(mostly from command injection cheatsheet). In one url, I read that most common command injection command was ';ls'. I 
tried that command and it gave me a list of directories. Then I started looking in each directory starting 
from the top (bin,boot,dev,etc,home,...) using ls followed by cd followed by ls again(;ls && cd bin && ls). The first four 
did not had any particular files that stood out to me. In the home directory, there was a flag text file. I used (;ls && cd home && cat flag.txt) 
to get the flag.
-The flag is CMSC389R-{p1ng_as_a_$erv1c3}
-I would suggest eric to try to avoid command line calls altogether and blacklist characters like 
";, & , |,-,etc" and any linux command words like "cd, ls, cat,..."

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
