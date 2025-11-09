import numpy as np

def von_neumann_correction(bits: np.ndarray) -> np.ndarray:
    """
    Applies Von Neumann correction to a sequence of bits to extract
    an unbiased sequence.

    The algorithm works by taking bits in non-overlapping pairs:
    - (0, 0) -> Discard
    - (1, 1) -> Discard
    - (0, 1) -> Output 0
    - (1, 0) -> Output 1

    Args:
        bits: A 1D NumPy array of 0s and 1s.

    Returns:
        A new 1D NumPy array of unbiased bits. The length will be
        <= len(bits) / 2.
    """
    # Ensure input is a numpy array
    bits = np.asarray(bits)

    # 1. Trim the array to an even length
    n = bits.size
    if n < 2:
        return np.array([], dtype=bits.dtype)  # Not enough bits for a pair

    # Discard the last bit if the total number is odd
    even_len = n - (n % 2)
    trimmed_bits = bits[:even_len]

    # 2. Reshape into non-overlapping pairs
    #    [[b0, b1], [b2, b3], ...]
    pairs = trimmed_bits.reshape(-1, 2)

    # 3. Create a boolean mask to find pairs where bits are different
    #    (i.e., (0, 1) or (1, 0))
    #    pairs[:, 0] is the first column (b0, b2, ...)
    #    pairs[:, 1] is the second column (b1, b3, ...)
    mask = pairs[:, 0] != pairs[:, 1]

    # 4. Filter the pairs using this mask
    valid_pairs = pairs[mask]

    # 5. The output bit is the first bit of the valid pair
    #    (0, 1) -> outputs 0
    #    (1, 0) -> outputs 1
    #    So, we just select the first column from the valid pairs.
    corrected_bits = valid_pairs[:, 0]

    return corrected_bits.astype(int)

if __name__ == "__main__":
    arr = np.array([1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1])
    print(von_neumann_correction(arr))