# Oracle-of-Bacon
Python solution to the 6 Degrees of Kevin Bacon problem. The baconator.py script crawls the IMDB website, storing connections in a web.pickle file. The connections are stored using the node class provided in node.py. A breadth-first search algorithm is used concurrently with the websraping in order to find the shortest link between the given actor, inputed when the program is first executed, and Kevin Bacon

# Output
The script will output an individual's Bacon number, the number of people in the chain connecting them to Kevin Bacon, as well as the people in the chain and the movie they were in.

# Time
Currently, as it is a live webcrawler, this script is fairly impractical; it would be foolish to expect it to find any Bacon Number greater than 3 in a reasonable amount of time. The data storage cuts down on this time, but it is still signifigant. Possible solutions involve finding an alternative to webscraping data
