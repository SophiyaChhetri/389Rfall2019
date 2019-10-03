# Writeup 3 - Operational Security and Social Engineering

Name: Sophiya Chhetri
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri

## Assignment Writeup

### Part 1

I would find Eric's mother name from his social media account and his mother's phone number from one of the OSINT techniques. Similar to the video shown in the class, 
I would call his mother and pretend to be from her bank. I would then proceed to tell her that her account was showing that she has been purchasing items in another 
country. I was calling just making sure if she was the one spending her money overseas or if her account has been hacked. In order not to lose any money,this creates 
a sense of urgency to resolve the problem as soon as possible. Then I would reassure that there is nothing to worry about, we can still secure her account. Then I 
would ask her to open a computer. Ask her if she knows if there are any browser that she can log into the bank account. This will give me her primary browser name. 
Then I would ask her to login with her username and password. She might be suspicious/confused when she doesn't see any unusual activity in her bank account. I would 
explain that since this activity seemed suspicious, this information is visible only to the administrators of the bank. And we would post the activity only after 
resolving this issue with her so that she wouldn't lose any money. I would simultaneously ask her for ATM pin number and explain her that I need her ATM pin number 
so that I can also login to her bank account from my browser and help her make the bank more secure. I would inform her that I would be spending few minutes to figure 
out the best way to solve this issue. After she is in the bank's webpage, I would say that we will be resetting her account inorder to make it more secure. To do 
that, she would need to provide us some infomation. This infomation would be used to create security questions that she can use this to login from next time onwards. 
Then I would ask her to give me her mother's maiden name, the city she was born and her first pet name. After getting this infomation, I would ask her to wait 
for few moments. Then after few moments I would assure her that her bank account is secure now. And she would be getting an email confirmation after 24 hours. 
Then thank her for her time and hang up the phone.

### Part 2
The three vulnerabilities are
- open ports
	- Explanation: Attackers use open ports to find the vulnerability so that they can run an exploit. Like for example with the help of exposed port I was able to run 'nc' command which helped me to get Eric's password
	- Suggestion: As suggested by watchguard.com (https://www.watchguard.com/wgrd-resource-center/security-fundamentals/what-is-a-port), one should monitor your network traffic to see what hits your system. And also learn how to manually allow and deny services and ports.
- weak password
	- Explanation: The weak passwords are generally cracked within a short period of time. This will make attacker to perform the attack easily.
	- Suggestion: Encrypt the password and add your public key in place of password. So, even if someone is able to access your password, he/she won't be able to make anything much out of it.
- IP addresses
	- Explanation: This becomes a threat because with the help of IP address, attackers can find your personal infomation like your location, etc.
	- Suggestion: Use VPN. This will help you gain some anonymity online by hiding your true location and also allows to bypass geographic restriction on websites.