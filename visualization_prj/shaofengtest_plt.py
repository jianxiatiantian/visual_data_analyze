
import numpy as np

import matplotlib.pyplot as plt
data = np.random.randn(1000)
# getting data of the histogram
count, bins_count = np.histogram(data, bins=11)
print(id(count))
print(count,type(count))
media_count = [(bins_count[i]+bins_count[i+1])/2 for i in range(len(bins_count)-1)]
print(media_count)

# finding the PDF of the histogram using count values
pdf = count / sum(count)

# using numpy np.cumsum to calculate the CDF
# We can also find using the PDF values by looping and adding
cdf = np.cumsum(pdf)
# plotting PDF and CDF
plt.plot(media_count, pdf, color="red", label="PDF")
plt.plot(media_count, cdf,color='yellow', label="CDF")
plt.legend()
plt.show()