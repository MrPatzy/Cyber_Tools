# Coding Project - Readme

This file provides a general outline of each project, associated resources, and origional goals plus ideas looking ahead. 
These projectes are for my own learning. These projects are for educational purposes only. None of these projects should be used in illegal activity.
I do not have much free time, so the advancement of any project will be slow. 


## Port Scanner (NEW 11/12/2022)
-----

### Overview

I found this project as a quick project that I could easily expand upon. This started with just identifiying if ports we're open on a single host. 

### Goals

- Make my own tool for cyber security
- Work with importing libraries and working with them in code.
- Gain knowledge in backend socket connections

### Looking Forward

- I have set up options to be passed into the program. Ironing those out, to make it more like an NMAP functionality
- Find ways to speed up scanning (Current scan rate is slow)
- Allow IP range to be scanned, and set up predefined port ranges to scan.
- Add additional functionality

### Resources 

[Write a port scanner in Python in 5 minutes](https://www.youtube.com/watch?v=t9EX2RAUoTU&ab_channel=DavidBombal)


## Keylogger 
-----

### Overview

I wanted to get my feet back into coding to make sure that I knew the basics, and that I knew how to write code.  
I figured this project would be easy enough to get rolling. I did follow along with two different tutorials.
I realized that while incredibly easy, one thing I need to work on is understanding what packages I need to import and what they contain.

### Goals

- Write my own program
- Learn/refresh Python skills

### Looking Forward

- How to send data back to a remote listener
- How to package and encrypt the data so that it doesn't look suspiscious amongst other traffic. 

### Resources 

[Version 1](https://www.youtube.com/watch?v=TbMKwl11itQ&ab_channel=freeCodeCamp.org)
[version 2](https://www.youtube.com/watch?v=XKoTwepEzPI&ab_channel=DavidBombal)



## Multiclipboard
-----

### Overview

Following a [Tech with Tim](https://www.youtube.com/c/TechWithTim) guide, I was looking into automation of certain tasks.
Yes, this is a feature that is already available in most OS, but I still wanted to tackle it as it was a little more involved than the keylogger. 

### Goals

- Understand saving to files
- Practice with JSON objects

### Issues

- Can successfully save the data to a .json file but can not successfully load a selected value back to the clipboard.
  - See line 32
  - I believe it has something to do with the `clipboard.copy` function, as the `(data[key])` does call the correct value.
  - Unsolved. 
  
### Looking Forward

- Improve Syntax
- Allow multiple branches (ie. IP list, Command list, etc)

### Resources

[Tech With Tim Tutorial](https://youtu.be/Oz3W-LKfafE?t=158)



## Text RPG
-----

### Overview

This is following a guide made by [Bryan Tong](https://www.youtube.com/c/BryanTongC) on making a small text based game.
This project is quite the undertaking and I'm not sure that I'll finish given the time I have available to dedicate to it. 
I also have grand ideas of making some really cool game, but a hard time reigning myself in when it comes to realizing how much effort and time it takes to get it to work.

### Goals
- Working with classes
- Understanding writing and working with user interfaces
- Allowing user input as a base to explore **command injection** at a later point. 
- Learning to defend against command injection through **input sanitazation**. 

### Looking Forward
- There's a long way to go. Milestones will include:
  - Getting a working opening screen and start to the game.
  - User guided class selection and ability distribution.
  - Loading a saved game.
  - Character Movement through entire map.
  - Any combat sequence.
  - Creating a triggered event.
  - A scripted end to the game.

### Resources

[Python Text RPG](https://www.youtube.com/watch?v=MFW8DJ6qsak&ab_channel=BryanTong)
This is part one of i believe a 6 part series. I took a lot of liberties with this already to make it my own. 



## Weather
-----

### Overview

This is another [Tech with Tim](https://www.youtube.com/c/TechWithTim) tutorial. I really liked the idea of working with APIs.
I have never worked with an API before, so understaning how to use, call, and interact with APIs was important. 
This is a basic program working with JSON objects, but it opened up some ideas as far as API interactions and automation.

### Goals

- Working with APIs
- Working with JSON objects

### Looking Forward

- Use this as a base for IoT and Smart Home automation. 
- Understanding APIs, what APIs exist that I can make custome programs for?

### Resources

[Weather-Fetcher](https://youtu.be/Oz3W-LKfafE?t=1775)

