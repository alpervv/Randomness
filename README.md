Given an audio signal $X=(x_1, x_2, \ldots x_t)$, we apply the following operation:

1.  We apply Hilbert transform to the signal to get $X^h = hilbert(X)$
2.  We filter out the elements whose absolute value is below a certain threshold $\epsilon$ to get a new signal $X' = ({x'}_1, {x'}_2, ... {x'}_{t'})$.
3.  We amplify the signal by $\alpha$ to get $X'' = \alpha X'$.
4.  We reduce $\alpha X''$ mod $p$ and keep the decimal part. $Z = X'' \pmod{p}$. Note that multiplying by $\alpha$ is not the same as multiplying by $\alpha \pmod{p}$ since elements of the thresholded signal need not be integers.
5.  From Z, we generate a binary sequence with the following rule: If $Z_n < Z_{n+1}$ we generate 1, else 0.
6.  If we use multiple audio sources, resulting sequences are XORed together.

---

Here we present some empirical findings. In the following experiments $\epsilon$ was set to $\frac{1}{\alpha}$.

1.  $(p,\alpha) \in \{(3,93),(3,1009),(3,10007),(7,93),(7,1009),(7,10007), (17,93),(17,1009),(17,10007)\}$ on 3 different audio files. NIST test documents are named p-α-analysis.txt corresponding to relevant p and $\alpha$ values.
2.  1st case with von-neumann correction applied to resulting bit sequence. NIST test results are named p-α-neumann-analysis.txt corresponding to relevant p and $\alpha$ values.

Skeptical that the source of entropy was the different audio sources instead of the algorithm we propose, we tested variants of the algorithm on the same audio file with different $p$ and $\alpha$.

3.  $(p,\alpha) = (3,1009),(7,1009),(17,1009)$ applied to the same source, and results XORed. Analysis document is named "3-dif-prime-same-file-analysis.txt". A separate test was also conducted by applying von-neumann correction to the resulting sequence.
4.  $(p,\alpha) = (7,93),(7,1009),(7,10007)$ applied to the same source, and results XORed. Analysis document is named "3-dif-alpha-same-file-analysis.txt". A separate test was also conducted by applying von-neumann correction to the resulting sequence.

**The results above suggest that our transformation increases the inherent entropy of the number sequence.**
