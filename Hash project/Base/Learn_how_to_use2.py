"""    
    * how to use:
            to be used you must declare how many parity bits (sizePari)
        you want to include in the message.
            it is desired (for test purposes) to select a bit to be set
        as an error. This serves to check whether the code is working correctly.
            Lastly, the variable of the message/word that must be desired to be
        encoded (text).

    * how this work:
            declaration of variables (sizePari, be, text)

            converts the message/word (text) to binary using the
        text_to_bits function
            encodes the message using the rules of hamming encoding
            decodes the message using the rules of hamming encoding
            print the original message, the encoded message and the
        decoded message

            forces an error in the coded text variable
            decodes the message that was forced the error
            print the original message, the encoded message, the bit changed
        message and the decoded message.
    * All     
"""