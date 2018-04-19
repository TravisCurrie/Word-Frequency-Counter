import re
import string
slack_text = open("slack.txt", "r")
text_string = slack_text.read().lower()
freq = {}
match_freq = re.findall(r'\b[a-z]{2,20}\b', text_string)
 
for word in match_freq:
    count = freq.get(word,0)
    freq[word] = count + 1
     
freq_list = freq.keys()

for words in freq_list:
    print words, freq[words]
    