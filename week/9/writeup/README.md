# Writeup 9 - Forensics II

Name: Sophiya Chhetri
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri


## Assignment details

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked?
 - 142.93.136.81 : Found by running wireshark on given 'netlog.pcap'

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
 - Port scanning in open ports.Tools:nmap
 
3. What are the hackers' IP addresses, and where are they connecting from?
 - 159.203.113.181

4. What port are they using to steal files on the server?
 - 20

5. Which file did they steal? What kind of file is it? Do you recognize the file?
 - It is a 'findme.jpeg' file

6. Which file did the attackers leave behind on the server?
- 'greetz.fpff' file

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
- One countermeasure to prevent this kind of intrusion is to configure firewalls to look for potentially 
malicious behavior over time and have rules in the network traffic to cut off attacks if a certain threshold 
is reached, such as 10 port scans in 1 minute or 100 consecutive ping request

### Part 2 (55 Pts)
