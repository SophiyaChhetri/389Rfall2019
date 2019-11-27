# Writeup 10 - Crypto I

Name: Sophiya Chhetri
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri

## Assignment details

### Part 1 (45 Pts)
1. What is the structure of the ledger file format? Include exact byte offsets when static.
- The structure of the ledger file format is 'key_hash','ctext_hash','iv',and 'ctext'. The first 3 are of 16 bytes each and ctext is of length 'ctext_len'.

2. What specific cryptographic implementations are used by the program? I.e. not "hashing", but a specific algorithm. Why might this pose a risk?
- It uses 'aes128_encrypt' and 'md5_hash'

3. What information, if any, are you able to derive from [ledger.bin](ledger.bin) without decrypting it at all?
- I wasn't able to derive any infomation from 'ledger.bin'. All I was able to know was it store encrypted text. 

4. How does the application ensure Confidentiality? How is the encryption key derived?
- It ensures Confidentiality by encrypting messages before writing to the file. The key is derived by using 'md5' and 'aes128' encryption.

5. How does the application ensure Integrity? Is this flawed in any way?
- It ensures Integrity by checking for hash in a file to see if it is as expected.

6. How does the application ensure Authenticity? Is this flawed in any way?
- It ensures Authenticity by checking if file key hash and generated key hash are same. 

7. How is the initialization vector generated and subsequently stored? Are there any issues with this implementation?
- 16 bytes IV are generated randomly by using 'RAND_bytes'. There aren't any issue with this implementation. 

### Part 2 (45 Pts)

### Part 3 (10 Pts)
- 'Kerckhoffs's Principle' follows that the system must be practically, if not mathematically indecipherable. While 'security through obscurity' is the reliance on design or implementation to be secret. In my opinion, there should be usage of both principles to make the system more secure. First try to make the software as indecipherable as possible then hide the design implementation so it would be accessible to only specific group. Because no matter how secure the system is there will be someone is able to break into the system. So, our main goal would be to make the system as heavily encrypted and as difficult as possible.

