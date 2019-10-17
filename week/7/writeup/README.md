# Writeup 7 - Forensics I

Name: Sophiya Chhetri
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sophiya Chhetri

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it?
- This is a jpeg file. Found by using "file image" command.

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.
- City: Chicage
- State: IL
- Name of the building: John Hancock Center.
- Found by searching latitude and longitude in google maps that I got by running "exiftool image" command.

3. When was this photo taken? Provide a timestamp in your answer.
- 2018/08/22 11:33:24.801 (Command used: exiftool image)

4. What kind of camera took this photo?
- iPhone 8 back camera 3.99m f/1.8 (command used: exiftool image)

5. How high up was this photo taken? Provide an answer in meters.
- 539.5m Above sea level (command used: exiftool image)

6. Provide any found flags in this file in standard flag format.
- CMSC389R-{look_I_f0und_a_str1ng}: found by running "strings image | grep -C1 "CMSC"" command.
- CMSC389R-{abr@cadabra} 
	- Command used : binwalk --dd="png:png" image
			- opened 248F20.png file from "_image.extracted" folder

