sentences=input("Enter sentences:")
words=sentences.lower().split()
print("Words:",len(words))
print("chars:",len(sentences))

freq={}
for w in words:
    freq[w]=freq.get(w,0)+1
    most=max(freq,key=freq.get)
print(f"Most common: {most} ({freq[most]} times)")