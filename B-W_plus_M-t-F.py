from string import ascii_lowercase


def bwt(s) -> tuple[str, int]:
    """Apply Burrows-Wheeler transform to input string."""

    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column), table.index(s)  # Convert list of characters into string


def ibwt(r, idx):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = table[idx]  # Find the correct row
    return s


def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence


def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)


if __name__ == '__main__':
    encoded, row = bwt("banana")
    print(f"Encoded BWT {encoded}")
    encoded_m2f = move2front_encode(encoded, list(ascii_lowercase))
    print(f"Encoded M2F {encoded_m2f}")
    decoded_m2f = move2front_decode(encoded_m2f, list(ascii_lowercase))
    print(f"Decoded M2F {decoded_m2f}")
    decoded = ibwt(decoded_m2f, row)
    print(f"Decoded BWT {decoded}")


