# KeyWord-Search-Engine
Key Word Search Engine
I will be pre-processing a txt fyle and PDF by defining a function in python then convert the entire text into a spacy document object.
For 50000 entries its work in constant time.

Step:-----
->Load file via defined function <br />
->Clean text and convert it into Spacy doc object <br />
->Load pre-trained english language model en_core_web_lg <br />
->Convert docs into DocBin and store it into '.spacy' file <br />
->Store '.spacy' file on cloud <br />
->Read '.spacy' file using spacy_to_doc function <br />
->Search keyword using search_for_keyword function <br />

