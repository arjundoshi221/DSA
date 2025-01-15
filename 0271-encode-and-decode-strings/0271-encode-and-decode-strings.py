class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""

        for word in strs:
            word+="~*$()"
            encoded_string += word
        
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        encoder = "~*$()"

        decoded_string = s.split(encoder)
        decoded_string.pop(-1)
        print(decoded_string)

        return decoded_string
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))