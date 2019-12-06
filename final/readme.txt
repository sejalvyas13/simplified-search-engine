Project :
Simplified Search Engine

Getting started :
This in an end to end project run on the same host. The python API will be hosted on port 5000 and the frontend on port 3000.
First run the basicApi.py from command prompt or python shell
Then run "npm install" followed by "npm start" from the frontend directory

Project flow :

A search query is entered by the user. This query, with the help of ajax is passed to the python API running at port 5000. 

basicApi.py : This file initializes the Input class and passes the search query to its 'search' function.

input.py : This file reads all the links given in inputLinks.txt
The inputlinks fetched from the file are passed to the SearchEngine class.
The resultant output links thus obtained are stored in output.txt

search.py :
It initialises the DataProcess and Trie classes. This class also does page ranking of all the fetched links. The logic is to find the maximum number of backlinks for all the URLs for a given search query and sort them based on these weights. 


process.py :
This file crawls, scrapes and processes the text content obtained from all the links. 
textProcessing function removes the stop words, blanks, punctuations. Then a dictionary of words aganist their occurence list is created.
Next Trie class is initialised.

Trie.py :
This file inserts all the words from the key of the dictionary created in process.py. It only enters all the english alphabets. 
The search function returns true or false based on the presence of word in the Trie (ie if end of node is reached)

From search.py, if the search query returns true, then for that word, we perform constant time search in the dictionary to obtain the corresponding occurence list. The reason for storing the occurrence lists outside the trie is to keep the size of the Trie data structure sufficiently small to fit in internal memory. 

If there are multiple words, then occurence list of each word is fetched, and they are merged. The repeated links are given higher ranks since they contain most words. The repeated links and non repeating links are passed to the pageRank function which sorts these links. The pageRank function scrapes each link to find all the links, checks if the any link scraped if present in the occurence list. If yes, then we increase the score/weight for that particular link that we found in our occurence list. 
After iterating all the links, these links are sorted based their weights and are returned.

Returned pages are displayed in the order on the front end and are also fed to an output text file as a part of projec requirement. 