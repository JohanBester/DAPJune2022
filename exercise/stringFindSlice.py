# 6.5 Write code using find() and string slicing (section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
colonPlace = text.find(":")
newText = float(text[colonPlace+1:].strip())
print(newText)
