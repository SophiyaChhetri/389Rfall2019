# Writeup 8 - Binaries II

Name: Sophiya Chhetri
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?
 - Per-session administrator password of length 16 is generated by assigning random letter to each space. Since the password
 length is fixed with none special characters and numbers, there is possibility of getting password by trying several combination of letters.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
 - In cipher method, line 46 `printf(output)`- one can print the output on the stack by messing around with the printf format strings. One way to solve this is to
 not print the output.
 - In exec_command method, line 68 `gets(buff)` - It is not safe because it could give buffer overflow error because it do
 not check maximum limit of input characters. Can use fgets() instead of gets(). fgets is safer as it checks the array
 bound and follow some parameter as maximum length. [fgets() and gets() explanation](https://www.geeksforgeeks.org/fgets-gets-c-language/)

3. What is the flag?

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
 - I was not able to obtain the flag. In order to find the flag, I first went over server.c throughly. Also ran the program in debugging mode to see what each line does starting from main_prompt() method.
 