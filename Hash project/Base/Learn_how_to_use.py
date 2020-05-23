"""
# Example how to use

# number of parity bits
sizePari = 4

# location of the bit that will be forced an error
be = 2

# Message/word to be encoded and decoded with hamming
# text = input("Enter the word to be read: ")
text = "Message01"

# Convert the message to binary
binaryText = text_to_bits(text)

# Prints the binary of the string
print("Text input in binary is '" + binaryText + "'")

# total transmitted bits
totalBits = len(binaryText) + sizePari
print("Size of data is " + str(totalBits))

print("\n --Message exchange--")
print("Data to send ------------> " + binaryText)
dataOut = emitterConverter(sizePari, binaryText)
print("Data converted ----------> " + "".join(dataOut))
dataReceiv, ack = receptorConverter(sizePari, dataOut)
print(
    "Data receive ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Data integrity: "
    + str(ack)
)


print("\n --Force error--")
print("Data to send ------------> " + binaryText)
dataOut = emitterConverter(sizePari, binaryText)
print("Data converted ----------> " + "".join(dataOut))

# forces error
dataOut[-be] = "1" * (dataOut[-be] == "0") + "0" * (dataOut[-be] == "1")
print("Data after transmission -> " + "".join(dataOut))
dataReceiv, ack = receptorConverter(sizePari, dataOut)
print(
    "Data receive ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Data integrity: "
    + str(ack)
)
"""
