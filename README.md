# KeyWord-Search-Engine
Key Word Search Engine
I will be pre-processing a txt fyle and PDF by defining a function in python then convert the entire text into a spacy document object.
For 50000 entries its work in constant time.

Step:-----
->Load file via defined function
->Clean text and convert it into Spacy doc object
->Load pre-trained english language model en_core_web_lg
->Convert docs into DocBin and store it into '.spacy' file
->Store '.spacy' file on cloud
->Read '.spacy' file using spacy_to_doc function
->Search keyword using search_for_keyword function

