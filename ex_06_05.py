text = "X-DSPAM-Confidence:    0.8475  "

colpos = text.find(':')
number = text[colpos+1:]
number = float(number.strip())
print(number)