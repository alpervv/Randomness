from scipy.io import wavfile
import numpy as np
from scipy.fft import fft
from scipy.signal import hilbert
from von_neuman import von_neumann_correction


# alpha = 1000
# threshold = 1/alpha
# p = 7
normalize = False

def modular_transform(data,p,alpha,threshold,normalize = True):
    if normalize:
        data = data/np.max(np.abs(data))
    data = data[np.abs(data) >= threshold]
    data = alpha*data
    print(data[1000:1500])
    data = np.mod(data, p)
    binary_seq = (data[:-1] < data[1:])
    return binary_seq

# for p in [3,7,17]:
#     for alpha in [93,1009,10007]:

p, alpha = 3, 1009
threshold = 1/alpha
samplerate, data = wavfile.read(r"data\Bike recording (Aga - Skarsatra).wav")
data = np.abs(hilbert(data[:4000000]), dtype=np.float64)
binary_seq1 = modular_transform(data,p,alpha,threshold,normalize)

# p, alpha = 7, 1009
# threshold = 1/alpha
# samplerate, data = wavfile.read(r"data\Bike recording (Aga - Skarsatra).wav")
# data = np.abs(hilbert(data[:4000000]), dtype=np.float64)
# binary_seq2 = modular_transform(data,p,alpha,threshold,normalize)

# p,alpha = 17,1009
# threshold = 1/alpha
# samplerate, data = wavfile.read(r"data\Bike recording (Aga - Skarsatra).wav")
# data = np.abs(hilbert(data[:4000000]), dtype=np.float64)
# binary_seq3 = modular_transform(data,p,alpha,threshold,normalize)

alpha = 93
samplerate, data = wavfile.read(r"data\Nordic Wellness Aga Recording.wav")
data = np.abs(hilbert(data[:4000000]), dtype=np.float64)
binary_seq2 = modular_transform(data,p,alpha,threshold,normalize)

alpha = 10007
samplerate, data = wavfile.read(r"data\riding-through-blue-skies-298649.wav")
data = data[:,0]
data = np.abs(hilbert(data[:4000000]), dtype=np.float64)
binary_seq3 = modular_transform(data,p,alpha,threshold,normalize)

min_len = min(len(binary_seq1), len(binary_seq2), len(binary_seq3))
binary_seq1, binary_seq2, binary_seq3 = binary_seq1[:min_len], binary_seq2[:min_len], binary_seq3[:min_len]
binary_seq = np.bitwise_xor(np.bitwise_xor(binary_seq1, binary_seq2), binary_seq3).astype(int)
binary_seq = von_neumann_correction(binary_seq)

save_file_name = "output/”3-dif-alpha-same-file-neumann.txt"
save_file = open(save_file_name, "w")
save_file.write("".join([str(int(k)) for k in binary_seq]))
save_file.close()