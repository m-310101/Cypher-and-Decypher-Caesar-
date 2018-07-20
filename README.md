# Cypher-and-Decypher-Caesar-
Simple brute force cypher and decypher using the caesar cypher.

The All Ciphers file contains the algorithm that will display every single combination of the caesar cipher applied to a message. This means that you will be given every possible version of the message ciphered.

The mostCommon text file contains a list of words that are often used. They are ordered in a way in which the decipher algorithm will compare with the first items in the file. The way I have ordered them means that most common words (that don't have conflicting words within their cipher. For example, the word "the" can be caesar ciphered to the word "max" which is a rather common name which could cause an incorrect solution) are first checked in order to speed up deciphering speed.
