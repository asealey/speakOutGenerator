SpeakOut Generator
==================
This is a first pass at creating a phrase generator for the SpeakOut game, as originally seen here: https://youtu.be/JgSzBqL61cM

Background
==========
This started as a weekend conversation with Tygh, and turned into a geek out coding Sunday.  

Approach
========
The code starts loads a wordlist (sourced from http://www.anc.org/data/anc-second-release/frequency-data/).  This includes a Part Of Speech field, based on the Penn Treebank POS project (https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

Using this wordlist, I created a few phrase templates based on phrases used in the video, and randomly generate several (100) phrases and print it out

Known Issues
============
The phrases aren't that great. :-( As I've spot checked, about 50% of them make absolutely no sense.

TODO
====
* Break the code into modules
* Find better ways to generate phrases
* ???
* Profit!

License
=======
[GPL 3](http://choosealicense.com/licenses/gpl-3.0/)

Copyright (C) 2016 Adam L. Sealey

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
