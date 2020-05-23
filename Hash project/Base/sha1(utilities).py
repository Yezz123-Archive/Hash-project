"""
Demonstrates implementation of SHA1 Hash function in a Python class and gives utilities
to find hash of string or hash of text from a file.
Usage: python sha1.py --string "Hello World!!"
       python sha1.py --file "hello_world.txt"
       When run without any arguments, it prints the hash of the string "Hello World!! Welcome to Cryptography"
Also contains a Test class to verify that the generated Hash is same as that
returned by the hashlib library

SHA1 hash or SHA1 sum of a string is a crytpographic function which means it is easy
to calculate forwards but extremely difficult to calculate backwards. What this means
is, you can easily calculate the hash of  a string, but it is extremely difficult to
know the original string if you have its hash. This property is useful to communicate
securely, send encrypted messages and is very useful in payment systems, blockchain
and cryptocurrency etc.
The Algorithm as described in the reference:
First we start with a message. The message is padded and the length of the message
is added to the end. It is then split into blocks of 512 bits or 64 bytes. The blocks
are then processed one at a time. Each block must be expanded and compressed.
The value after each compression is added to a 160bit buffer called the current hash
state. After the last block is processed the current hash state is returned as
the final hash.


"""