# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:29:30 2024

@author: Jack
"""

"""
Created on Sat Mar  9 17:12:30 2024

@author: Sriram Pemmaraju
"""

###############################################################################
#
# Specification: This function uses the binary search algorithm to search for 
# the given word w in the sublist L[first:last+1]. 
# It assumes that L is sorted in non-decreasing order. The function returns -1 if w is 
# not in L; otherwise it returns the index of w in L. If there are multiple occurances 
# of w in L, it just returns the index of an arbitrary occurance of w.
#
###############################################################################
def binarySearch(L, w, first, last):
    if (first > last):
        return -1
    
    mid = (first + last) // 2
    if (w == L[mid]):
        return mid
    elif (w < L[mid]):
        return binarySearch(L, w, first, mid-1)
    else:
        return binarySearch(L, w, mid+1, last)

###############################################################################
#
# Specification: This function searches for the given word w in the given list L by
# calling the binarySearch function. It assumes that L is sorted in non-decreasing order.
# The function returns -1 if w is not in L; otherwise it returns the index of w in
# L. If there are multiple occurances of w in L, it just returns the index of 
# an arbitrary w.
# 
###############################################################################
def getIndex(L, w):
    return binarySearch(L, w, 0, len(L)-1)

###############################################################################
#
# Specification: This function takes two nonempty, equal-length strings w1 and w2 and 
# returns True if w2 is obtained from w1 by replacing one character
# in w1 by another (different) character; otherwise the function returns False. 
#
# Note: The replacement character cannot be identical to the character being replaced.
#
# Examples:
# >>> areNeighbors("Hello", "cello")
# True
# >>> areNeighbors("Hello", "cells")
# False
# >>> areNeighbors("Hello", "hello")
# True
# >>> areNeighbors("Hello", "belto")
# False
# >>> areNeighbors("Hello", "Hello")
# False
#
###############################################################################
def areNeighbors(w1, w2):
    if len(w1) != len(w2):
        return False
    differences = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            differences += 1
            if differences > 1:
                return False
    
    return differences == 1




###############################################################################
#
# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
#
# Examples:
# >>> L = readWords()
# >>> len(L)
# 5757
# >>> L[len(L)-1]
# 'zowie'
# >>> L[0:10]
# ['aargh',
#  'abaca',
#  'abaci',
#  'aback',
#  'abaft',
#  'abase',
#  'abash',
#  'abate',
#  'abbey',
#  'abbot']
# >>> L[1000]
# 'coney'
# >>> sorted(L)==L
# True
#
###############################################################################
def readWords():
    words = [] 
    with open('words.txt', 'r') as file: 
        for line in file:  
            word = line.strip() 
            if len(word) == 5:  
                words.append(word)  
    return words 


    
######################################################################
#
# Specification: You are given a list L of distinct, equal-length strings. We 
# define two distinct strings w1 and w2 to be neighbors if w2 can be obtained from 
# w1 by replacing one character in w1 by another (different) character. In other words, w1 and w2 
# are neighbors if areNeighbors(w1, w2) is True. The function is required to return 
# the list of neighbor lists of each word in L. 
#
# EXAMPLE 1
#L = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided','sided', 'tided']
#
# makeNeighborLists(L) returns
#
# [['anded'],
# ['aides'],
# ['aider'],
# ['aimed', 'aired'],
# ['ailed', 'aired'],
# ['ailed', 'aimed'],
# ['added'],
# ['sided', 'tided'],
# ['bided', 'tided'],
# ['bided', 'sided']]
#
# In this example, "added" is the first word in L and it has one neighbor
# in L, which is "anded". So ["anded"] is the first item in the returned list.
# The 4th word in L is "ailed" and it has two neighbors "aimed" and "aired".
# So the 4th item in the returned list is ["aimed", "aired"].
#
# EXAMPLE 2
# L = ['joked', 'poked', 'toked', 'yokel', 'yokes', 'yodel', 
#      'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 
#      'yores', 'folks', 'yolky', 'folky', 'yolks']
#
# makeNeighborLists(L) returns
#
# [['poked', 'toked', 'yoked', 'jokes'],
# ['joked', 'toked', 'yoked', 'pokes'],
# ['joked', 'poked', 'yoked', 'tokes'],
# ['yokes', 'yodel', 'yoked'],
# ['yokel', 'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 'yores'],
# ['yokel'],
# ['joked', 'poked', 'toked', 'yokel', 'yokes'],
# ['yokes', 'jokes', 'pokes', 'tokes'],
# ['joked', 'yokes', 'cokes', 'pokes', 'tokes'],
# ['poked', 'yokes', 'cokes', 'jokes', 'tokes'],
# ['toked', 'yokes', 'cokes', 'jokes', 'pokes'],
# ['yokes'],
# ['yokes'],
# ['folky', 'yolks'],
# ['folky', 'yolks'],
# ['folks', 'yolky'],
# ['folks', 'yolky']]
#
#
# NOTES
# (i) The neighbor lists should appear in the order corresponding to words in L. In 
# other words if we call the returned list nbrList, then the list of neighbors of
# the word L[0] should appear as nbrList[0].
# (ii) Each list of neighbors should contain words in the same order as in L. For
# example, the neighbor list of "ailed" should be ["aimed", "aired"] rather than
# ["aired", "aimed"].
# (iii) The neighbor relationship is only defined for distinct words. So a word
# cannot be its own neighbor.
#
# ADDITIONAL EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> makeNeighborLists(L1)
# [['aided'], ['added', 'bided'], ['aided']]
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> makeNeighborLists(L2)
# [['jokes'],
#  ['joked', 'yokes'],
#  ['yokes'],
#  ['yokes'],
#  ['jokes', 'yikes', 'yokel']]
# 
######################################################################
def makeNeighborLists(wordList):
    neighborLists = []
    for i, word1 in enumerate(wordList):
        neighbors = []
        for j, word2 in enumerate(wordList):
            if i != j and areNeighbors(word1, word2):
                neighbors.append(word2)
        neighborLists.append(neighbors)
    return neighborLists


###############################################################################
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. In addition, it takes
# a word w in wordList and returns the list of neighbors of this word in wordList.
# The returned list of neighbors is sorted (in increasing alphabetical order). 
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> getNeighbors(L1, nL1, 'aided')
# ['added', 'bided']
# >>> getNeighbors(L1, nL1, 'added')
# ['aided']
# >>> getNeighbors(L1, nL1, 'bided')
# ['aided']
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> nL2 = makeNeighborLists(L2)
# >>> getNeighbors(L2, nL2, 'yokes')
# ['jokes', 'yikes', 'yokel']
# >>> getNeighbors(L2, nL2, 'joked')
# ['jokes']
# >>> getNeighbors(L2, nL2, 'jokes')
# ['joked', 'yokes']
#
###############################################################################
def getNeighbors(wordList, nbrsList, w):
    index = wordList.index(w)
    neighbors = nbrsList[index]
    sorted_neighbors = sorted(neighbors)
    return sorted_neighbors
    

###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns all words 
# with 0 neighbors, i.e., isolated nodes.
#
# EXAMPLES:
# >>> L = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedNodes(L, nL)
# ['abbey', 'young']    
# >>> L = ['aargh',
#          'abaft',
#          'abbey',
#          'abbot',
#          'abeam',
#          'abhor',
#          'absit',
#          'abuzz',
#          'abyss',
#          'achoo',
#          'acids',
#          'acrid',
#          'actin',
#          'actor',
#          'acute',
#          'adage',
#          'addle',
#          'adieu',
#          'adios',
#          'adlib']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedNodes(L, nL)
# ['aargh',
#  'abaft',
#  'abbey',
#  'abbot',
#  'abeam',
#  'abhor',
#  'absit',
#  'abuzz',
#  'abyss',
#  'achoo',
#  'acids',
#  'acrid',
#  'actin',
#  'actor',
#  'acute',
#  'adage',
#  'addle',
#  'adieu',
#  'adios',
#  'adlib']  
#
###############################################################################
def getIsolatedNodes(wordList, nbrsList):
    isolated = []
    for word, neighbors in zip(wordList, nbrsList):
        if not neighbors:  
            isolated.append(word)  
    return isolated



###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns all pairs of 
# nodes that are connected to each other, but to no other node.
# 
# EXAMPLES:
# >>> L = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# [['audio', 'audit']]
# >>> L.extend(['joked', 'jokes'])
# >>> L.sort()
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# [['audio', 'audit'], ['joked', 'jokes']]
# >>> L = ['aided', 'bided', 'sided', 'tided']
# >>> nL = makeNeighborLists(L)
# >>> getIsolatedEdges(L, nL)
# []
#
###############################################################################
def getIsolatedEdges(wordList, nbrsList):
    isolated_edges = []  
    

    for index, word in enumerate(wordList):
     
        if len(nbrsList[index]) == 1:
        
            neighbor = nbrsList[index][0]
           
            neighbor_index = wordList.index(neighbor)
            
            if len(nbrsList[neighbor_index]) == 1 and nbrsList[neighbor_index][0] == word:
                
                isolated_edges.append(sorted([word, neighbor]))
    
    unique_isolated_edges = []
    for edge in isolated_edges:
        if edge not in unique_isolated_edges:
            unique_isolated_edges.append(edge)
    
    return unique_isolated_edges

                

###############################################################################
# 
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list 
# of words in wordList but in non-decreasing order of degree. Remember that the 
# degree of a node in the network is the number of neighbors it has. Two words 
# with the same degree appear in alphabetical order.
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> sortByDegree(L1, makeNeighborLists(L1))
# ['added', 'bided', 'aided']
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> sortByDegree(L2, makeNeighborLists(L2))
# ['joked', 'yikes', 'yokel', 'jokes', 'yokes']  
# >>> L3 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
# >>> sortByDegree(L3, makeNeighborLists(L3))
# ['added',
#  'aider',
#  'aides',
#  'anded',
#  'ailed',
#  'aimed',
#  'aired',
#  'bided',
#  'sided',
#  'tided']
#
###############################################################################
def sortByDegree(wordList, nbrsList):
    words_with_degrees = [(word, len(neighbors)) for word, neighbors in zip(wordList, nbrsList)]
    
    words_with_degrees.sort(key=lambda x: x[1])
    
    return [word for word, _ in words_with_degrees]

        
###############################################################################
# 
# Specification: This function returns the distributions of the degrees of the nodes
# in the word network specified by wordList and nbrsList. wordList is a non-empty, 
# sorted (in increasing alphabetical order) list of words  and nbrsList is the word 
# network of wordList represented as the corresponding list of neighbor lists. The
# function returns a list of nonnegative integers, where the integer at index i is the
# number of nodes in the word network with degree i. The length of the returned list
# is 1 plus the maximum degree of the word network.
#
# EXAMPLES:
# >>> L1 = ['added', 'aided', 'bided']
# >>> degreeDistribution(L1, makeNeighborLists(L1))
# [0, 2, 1]
# >>> L2 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
# >>> degreeDistribution(L2, makeNeighborLists(L2))
# [0, 3, 1, 1]
# >>> L3 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
# >>> degreeDistribution(L3, makeNeighborLists(L3))
# [0, 4, 6]
#
###############################################################################
def degreeDistribution(wordList, nbrsList):
    degrees = [len(neighbors) for neighbors in nbrsList]
    
    max_degree = max(degrees) if degrees else 0
    
    distribution = [0] * (max_degree + 1)
    
    for degree in degrees:
        distribution[degree] += 1
    
    return distribution

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and it performs a breadth first search of the word network starting from
# the word source. It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Examples: 
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> searchWordNetwork(L1, nL1, "aided")
# [['aided', '', 'aided'], [1, 0, 1]]
# >>> searchWordNetwork(L1, nL1, "added")
# [['', 'added', 'aided'], [0, 1, 2]]
#
# Notes: 
# (a) If the length of wordList is n, then the returned list contains two lists,
# each of length n.
# (b) If the returned list is [L1, L2] and a word w has index i in wordList, then
# the parent information of w is stored in L1[i] and the distance information of
# w is stored in L2[i].
# (c) The parent information of a word is "" if it is the source word or if it
# is not reachable from the source word.
# (d) The distance information for any word that is not reachable from the source
# word is -1.
#
# Two more examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> searchWordNetwork(L2, nL2, "tides")
# [['bides', 'tides', 'sides', 'tides', 'tides', ''], [2, 1, 2, 1, 1, 0]]
#
###############################################################################


def searchWordNetwork(wordList, nbrsList, source):
    parents = {word: '' for word in wordList}
    distances = {word: -1 for word in wordList}
    queue = [source]
    distances[source] = 0

    while queue:
        current_word = queue.pop(0)
        current_index = wordList.index(current_word)

        for neighbor in nbrsList[current_index]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_word] + 1
                parents[neighbor] = current_word
                queue.append(neighbor)

    parents_list = [parents[word] if word != source else '' for word in wordList]
    distances_list = [distances[word] for word in wordList]

    return [parents_list, distances_list]



###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and a word called target. The function returns a shortest path
# from the source word to the target word, if there is a path between these two
# words. Otherwise, the function returns []. This function calls searchWordNetwork
# to compute the parent list and then follows the parent pointers from target 
# to source to compute a path; this path is then reversed and returned.
#
# Examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> findPath(L2, nL2, "tides", "sided")
# ['tides', 'sides', 'sided']
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findPath(L3, nL3, "curve", "taste")
# ['curve', 'curse', 'purse', 'parse', 'passe', 'paste', 'taste']
#
###############################################################################
def findPath(wordList, nbrsList, source, target):
    parents, distances = searchWordNetwork(wordList, nbrsList, source)
    if distances[wordList.index(target)] == -1:
        return []
    path = []
    current_word = target
    while current_word != '':
        path.append(current_word)
        current_word = parents[wordList.index(current_word)]
    path.reverse()
    return path

            
        
###############################################################################     
#
# Specification:  This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list of
# connected components in the word network.
#
# Definition: A connected component of a network is the set of all nodes that can
# be reached from each other via paths in the network.
#
# Examples: 
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findComponents(L3, nL3)
# [['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]   
# >>> L4 = L3 +["sided", "tided", "bided"]
# >>> L4.sort()
# >>> nL4 = makeNeighborLists(L4)
# >>> findComponents(L4, nL4)
#  [['bided', 'sided', 'tided'],
#   ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
# >>> L5 = ["abhor"] + L4
# >>> nL5 = makeNeighborLists(L5)
# >>> findComponents(L5, nL5)
# [['abhor'],
#  ['bided', 'sided', 'tided'],
#  ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
#
# Notes: 
# (a) The nodes in each connected component should appear in the same order
# as they appear in wordList. 
# (b) The components themselves should be sorted by the first word in the component.
#
###############################################################################            
def findComponents(wordList, nbrsList):
    visited = [False] * len(wordList)
    components = []

    for i, word in enumerate(wordList):
        if not visited[i]:
            stack = [word]
            component = []

            while stack:
                current = stack.pop()
                if not visited[wordList.index(current)]:
                    visited[wordList.index(current)] = True
                    component.append(current)

                    for neighbor in nbrsList[wordList.index(current)]:
                        if not visited[wordList.index(neighbor)]:
                            stack.append(neighbor)

            components.append(sorted(component, key=lambda x: wordList.index(x)))

    return components

# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
#
# NEW: if the file word.txt is missing, this function should just return [] instead
# of causing the program to cause an exception.
#
# Examples:
# >>> L = readWords()
# >>> len(L)
# 5757
# >>> L[len(L)-1]
# 'zowie'
# >>> L[0:10]
# ['aargh',
#  'abaca',
#  'abaci',
#  'aback',
#  'abaft',
#  'abase',
#  'abash',
#  'abate',
#  'abbey',
#  'abbot']
# >>> L[1000]
# 'coney'
# >>> sorted(L)==L
# True
#
###############################################################################
def readWords():
    try:
        with open("words.txt", "r") as file:
            words = file.read().split()
            five_letter_words = [word for word in words if len(word) == 5]
        return five_letter_words
    except FileNotFoundError:
        return []
    
###############################################################################     
#
# Specification:  This function takes a list of words and a list of file names.
# It reads from each file in the given list of file names and extracts words from
# the file. For each word in the list of words, it computes the frequency of this
# word in all the files in the given list of file names. The function returns
# the list of frequencies. The order in which frequencies appear in the frequency
# list should match the order in which words appear in the given word list. In other
# words, the frequency in slot 0 should be the frequency of smallerWordList[0],
# the frequency in slot 1 should be the frequency of smallerWordList[1], etc.
# The function should use "try and except" to gracefully deal with missing files.
# If a file is missing, it should just skip over to the next file. If all files
# are missing, then the frequency list returned should contain all 0's.
#
###############################################################################   
def computeFrequencies(smallerWordList, fileNameList):
    word_count = {word: 0 for word in smallerWordList}

    for fileName in fileNameList:
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                words_in_file = file.read().lower().split()
                for word in words_in_file:
                    if word in word_count:
                        word_count[word] += 1
        except FileNotFoundError:
            continue

    return word_count
        

############################################################################### 
# You can add as many other functions as you want to make your code streamlined,
# readable, and efficient
############################################################################### 


############################################################################### 
# main program starts here
############################################################################### 

# STEP 1: Identify the list of words in the largest connected component
# (a) Read the list of all words in words.txt. Make sure that the 
# program exits gracefully if words.txt is not available
# (b) Build the adjacency list representation of the word network of this list of 
# words
# (c) Find all connected components of this word network
# (d) Identify the largest connected component and create a list with the words 
# in the largest connected component in sorted order
def read_words(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().split()
    except FileNotFoundError:
        print("Error: The file could not be found.")
        exit()

def is_connected(word1, word2):
    if len(word1) != len(word2):
        return False
    differences = sum(1 for a, b in zip(word1, word2) if a != b)
    return differences == 1

def build_adjacency_list(words):
    adjacency_list = {word: [] for word in words}
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_connected(words[i], words[j]):
                adjacency_list[words[i]].append(words[j])
                adjacency_list[words[j]].append(words[i])
    return adjacency_list

def dfs(adjacency_list, start, visited):
    stack = [start]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return component

def find_components(adjacency_list):
    visited = set()
    components = []
    for word in adjacency_list:
        if word not in visited:
            component = dfs(adjacency_list, word, visited)
            components.append(component)
    return components

# STEP 2: Compute the frequencies of all the words in the largest connected component
# and designate the p % of the words with highest frequency as "easy" words  
# (a) Create a list containing all the names of text files downloaded from Project Gutenberg
# (b) Call the function computeFrequencies to read from these files, extract words, and
# update the frequencies of the words in the largest connected component  
# (c) Read from the file parameters.txt to get the value of parameter p
# (d) Designate the most frequent  p % of these words as "easy" words and the rest
# as "hard" words 
import os
import re

def get_filenames(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]

def read_parameter_p(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('p ='):
                    p_value = float(line.split('=')[1].strip())
                    return p_value
    except FileNotFoundError:
        print("Error: Parameter file not found.")
        exit()
    except ValueError as e:
        print(f"Error: Could not convert string to float. {e}")
        exit()

def categorize_words(word_frequencies, p):
    total_words = len(word_frequencies)
    cutoff_index = int(total_words * (p / 100))
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    easy_words = [word for word, _ in sorted_words[:cutoff_index]]
    hard_words = [word for word, _ in sorted_words[cutoff_index:]]
    return easy_words, hard_words

def compute_frequencies(largest_component, filenames):
    word_freq = {word: 0 for word in largest_component}
    for filename in filenames:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                contents = file.read().lower()
                words = re.findall(r'\b[a-z]{2,}\b', contents)
                for word in words:
                    if word in word_freq:
                        word_freq[word] += 1
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            continue
    return word_freq



# STEP 3: Write into the file gameInformation.txt
# (a) Open the file "gameInformation.txt" for writing
# (b) Write the number of easy words, followed by the easy words themselves in alphabetical order
# (c) Write the number of hard words, followed by the hard words themselves in alphabetical order
# (d) Write the adjacency list representation of the word network of the largest connected component
# Make sure that everything is written into the file gameInformation.txt as per the specifications
# in the project 1 handout

def write_game_information(filename, easy_words, hard_words, adjacency_list):
    with open(filename, 'w') as file:
        file.write(f"Number of Easy Words: {len(easy_words)}\n")
        for word in sorted(easy_words):
            file.write(f"{word}\n")

        file.write(f"Number of Hard Words: {len(hard_words)}\n")
        for word in sorted(hard_words):
            file.write(f"{word}\n")

        file.write("Adjacency List Representation:\n")
        for word in sorted(adjacency_list.keys()):
            neighbors = ', '.join(sorted(adjacency_list[word]))
            file.write(f"{word}: {neighbors}\n")
            
def main():
    filenames = get_filenames("C:/Users/Jack/Downloads/projectfiles")
    words = read_words("words.txt")
    adjacency_list = build_adjacency_list(words)
    components = find_components(adjacency_list)
    largest_component = max(components, key=len)
    largest_component_sorted = sorted(largest_component)

    word_frequencies = compute_frequencies(largest_component_sorted, filenames)
    p = read_parameter_p('parameters.txt')
    easy_words, hard_words = categorize_words(word_frequencies, p)

    write_game_information('gameInformation.txt', easy_words, hard_words, adjacency_list)

if __name__ == "__main__":
    main()

from collections import deque

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It takes the 
# word network of all the words in wordList, represented as the corresponding 
# list of neighbor lists. It also takes a word called source in wordList and 
# it performs a breadth first search of the word network starting from
# the word source. In addition, it takes a list of words called easyWordList,
# all of which belong to wordList. These words have weight 0, whereas the remaining
# words have weight given by the non-negative integer parameter w.
# It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Definition: The length of a path is the sum of the number of edges in the path
# plus the sum of the weights of all the nodes in the path.
#
# Definition: The distance between a pair of nodes u and v is the length of the
# shortest path betwwen them.
#
# Notes: 
# (a) If the length of wordList is n, then the returned list contains two lists,
# each of length n.
# (b) If the returned list is [L1, L2] and a word w has index i in wordList, then
# the parent information of w is stored in L1[i] and the distance information of
# w is stored in L2[i].
# (c) The parent information of a word is "" if it is the source word or if it
# is not reachable from the source word.
# (d) The distance information for any word that is not reachable from the source
# word is -1.
#
###############################################################################
def searchWeightedWordNetwork(wordList, nbrsList, source, easyWordList, w):
    index_map = {word: idx for idx, word in enumerate(wordList)}
    easy_set = set(easyWordList)
    parentList = [""] * len(wordList)
    distanceList = [-1] * len(wordList)

    queue = deque([(source, 0)])
    parentList[index_map[source]] = None
    distanceList[index_map[source]] = 0

    while queue:
        current_word, current_distance = queue.popleft()

        for neighbor in nbrsList[current_word]:
            neighbor_index = index_map[neighbor]
            if distanceList[neighbor_index] == -1:
                parentList[neighbor_index] = current_word
                if neighbor in easy_set:
                    neighbor_distance = current_distance
                else:
                    neighbor_distance = current_distance + w
                distanceList[neighbor_index] = neighbor_distance
                queue.append((neighbor, neighbor_distance))

    return [parentList, distanceList]


###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It also takes a word 
# called source in wordList and a list of distances of all nodes in wordList
# from this network. It returns a list of words, in aphabetical order,
# that are between distance d1 and d2 from source (inclusive of d1 and d2).
# You can assume that d1 and d2 are non-negative integers and d1 <= d2. 
#
# You can assume that distanceList has been produced by a call to searchWordNetwork
# or searchWeightedWordNetwork. 
#
###############################################################################
def wordsAtDistanceRange(wordList, source, distanceList, d1, d2):
    return [word for word, distance in zip(wordList, distanceList) if d1 <= distance <= d2]
###############################################################################
# Main program

# Read parameters.txt; use default values if parameters.txt is missing
# The paremeters.txt file has the format:
#   p = value1
#   w = value2
#   ed1 = value3, ed2 = value4
#   hd1 = value5, hd2 = value6
#   eh = value7, hh = value8
#   r = value9
# ADD CODE HERE. Ideally, this should be a fuction call
def read_parameters_from_file(filename):
    params = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                pairs = line.strip().split(',')
                for pair in pairs:
                    key, value = pair.strip().split('=')
                    params[key.strip()] = float(value.strip()) if '.' in value else int(value.strip())
    except FileNotFoundError:
        print("Parameters file not found, using default settings.")
    return params

# Read gameInformation.txt 
# Create easyWordList, hardWordList, wordList, nbrsList
# if gameInformation.txt is missing, provide a message to the user and construct all these lists
# from scratch.
# ADD CODE HERE. Ideally, this should be a function call

def read_game_information(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        parts = content.split("Adjacency List Representation:")
        word_section = parts[0].splitlines()
        adjacency_list = parts[1].splitlines()

        easy_word_index = next(i for i, line in enumerate(word_section) if "Number of Easy Words:" in line)
        hard_word_index = next(i for i, line in enumerate(word_section) if "Number of Hard Words:" in line)

        num_easy_words = int(word_section[easy_word_index].split(':')[1].strip())
        num_hard_words = int(word_section[hard_word_index].split(':')[1].strip())

        easyWordList = [line.strip() for line in word_section[easy_word_index + 1: easy_word_index + 1 + num_easy_words]]
        hardWordList = [line.strip() for line in word_section[hard_word_index + 1: hard_word_index + 1 + num_hard_words]]
        wordList = easyWordList + hardWordList

        nbrsList = {word: [] for word in wordList}
        
        for line in adjacency_list:
            if ": " in line:
                key, value = line.split(": ", 1)
                nbrsList[key.strip()] = [word.strip() for word in value.split(',')]

        return easyWordList, hardWordList, wordList, nbrsList
    except FileNotFoundError:
        print("Game information file not found, initializing default data.")
        return [], [], [], {}
    except Exception as e:
        print(f"Error reading game information: {e}")
        return [], [], [], {}

# Start initial user interaction
# Welcome them to the game and ask them to pick game playing mode.
# E for "easy mode" and H for "hard mode"
# ADD CODE HERE
def get_user_mode():
    mode = input("Choose your mode (E for Easy, H for Hard): ").upper()
    while mode not in ['E', 'H']:
        mode = input("Invalid choice. Please choose E for Easy or H for Hard: ").upper()
    return mode



# Once user has picked a mode, initialize parameter values for the game.
# (a) [d1, d2] = [ed1, ed2] for easy mode, [d1, d2] = [hd1, hd2] for hard mode
# (b) numWordHints = eh for easy mode, numWordHints = hh for hard mode 
# (c) distanceHintRate = r
# ADD CODE HERE
def initialize_game_settings(mode, params):
    settings = {
        'd1': params['ed1'] if mode == 'E' else params['hd1'],
        'd2': params['ed2'] if mode == 'E' else params['hd2'],
        'numWordHints': params['eh'] if mode == 'E' else params['hh'],
        'distanceHintRate': params['r']
    }
    return settings
    



# In the easy mode, pick a random word from easyWordList
# In the hard mode, pick a random word from wordList
# This is your target word.
# ADD CODE HERE
import random

def select_target_word(mode, easyWordList, wordList):
    if mode == 'E':
        if not easyWordList:  
            print("Easy word list is empty.")
            return None  
        return random.choice(easyWordList)  
    else:
        if not wordList:  
            print("Word list is empty.")
            return None  
        return random.choice(wordList)  







# (a) Call searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w) 
# to get parentList and distanceList
# (b) Call wordsAtDistanceRange(wordList, target, distanceList, d1, d2)
# to obtain all words at distance in the range [d1, d2] from target.
# Pick a word at random from this list; this is your source word
# ADD CODE HERE
def setup_game_play(wordList, nbrsList, target, easyWordList, w, d1, d2):
    parentList, distanceList = searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w)
    words_in_range = wordsAtDistanceRange(wordList, target, distanceList, d1, d2)
    if words_in_range:
        source_word = random.choice(words_in_range)
    else:
        source_word = None
    return source_word, parentList, distanceList



# Start main user interaction
# Provide the source word and target word. Ask the user to complete the word ladder
# from source word to target word. Let them know if they need to type the source word 
# and target word also. Inform them that they can type "Q" to quit the game at any 
# point and "H" if they want a next word hint.
# MAke sure messsages are clear. For example, you could use:
# "Excellent!" if the next word they type is a valid word in the ladder
# "Not a word in my dictionary!" if the next word they typs is not a word in wordList
# "The ladder can't go from xxxxx to yyyyy!" if the current word yyyyy is not a neighbor 
# of the previous word "xxxxx"
# ADD CODE HERE
# Main program setup for the Word Ladder game

# Read game parameters from the parameters.txt file
# Setup game with a broader range or adjusted weights
# Main program setup for the Word Ladder game
def main():
    params = read_parameters_from_file('parameters.txt')
    easyWordList, hardWordList, wordList, nbrsList = read_game_information('gameInformation.txt')

    mode = get_user_mode()
    game_settings = initialize_game_settings(mode, params)

    if mode == 'E':
        target_word = select_target_word(mode, easyWordList, wordList)
    else:
        target_word = select_target_word(mode, hardWordList, wordList)

    if not target_word:
        print("No valid target word could be selected. Exiting game setup.")
    else:
        source_word, parentList, distanceList = setup_game_play(wordList, nbrsList, target_word, easyWordList, params['w'], game_settings['d1'], game_settings['d2'])
        if source_word:
            print("Game is ready to start.")
            main_game_loop(wordList, nbrsList, source_word, target_word, parentList, distanceList, game_settings['numWordHints'], params['r'])
        else:
            print("No valid source word could be found within the specified distance range. Please try again or adjust the game settings.")


def main_game_loop(wordList, nbrsList, source, target, parentList, distanceList, numWordHints, distanceHintRate):
    print(f"Source word: {source}")
    print(f"Target word: {target}\n")
    current_word = source
    word_ladder = [source]
    hints_used = 0

    while current_word != target:
        next_word = input("Enter the next word in the ladder: ").lower()
        if next_word == "Q":
            print("You have quit the game.")
            return
        elif next_word == "H":
            if hints_used < numWordHints:
                hint_word = parentList[wordList.index(current_word)] if parentList[wordList.index(current_word)] else "No more hints."
                print(f"Hint: Consider the word {hint_word}")
                hints_used += 1
            else:
                print("No more hints available.")
            continue
        if next_word in wordList and next_word in nbrsList[current_word]:
            current_word = next_word
            word_ladder.append(next_word)
            if random.random() < distanceHintRate:
                distance_to_target = distanceList[wordList.index(next_word)]
                print(f"Distance to target: {distance_to_target} words")
        else:
            print("Invalid word or not a neighbor. Try again.")

    print("Congratulations! You've completed the word ladder:")
    print(" -> ".join(word_ladder))
main();