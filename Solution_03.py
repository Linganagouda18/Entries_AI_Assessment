
def freqcount(text):
    freq = {}
    words = text.split()

    for word in words:
        lowercase = word.lower()
        if lowercase in freq:
            freq[lowercase] += 1
        else:
            freq[lowercase] = 1

    max_freq = max(freq.values())
    highfreq = [word for word, freq in freq.items() if freq == max_freq]

    return min(highfreq)


text = "apple banana  cherry banana"
res = freqcount(text)
print(res)