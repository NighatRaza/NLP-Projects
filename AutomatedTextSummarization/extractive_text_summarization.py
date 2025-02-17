
# importing libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
import pandas as pd
from heapq import nlargest

# GUI tkinter libraries
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import END

def summarize_text():
    # Get text from the text box
    text = text_box.get("1.0", "end-1c")

    # loading model
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    # word tokenization and removal of stop words, punctuation and line break char
    tokens = [token.text.lower() for token in doc
            if not token.is_stop and
                not token.is_punct and
                token.text != '\n']

    # words frequency count
    word_freq = Counter(tokens)

    # largest frequency count
    max_freq = max(word_freq.values())

    # normalizing the word frequency count by dividing it with largest frequency count
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # sentence tokenization
    sent_token = [sent.text for sent in doc.sents]

    # sentence scoring
    sent_score = {}
    for sent in sent_token:
        for word in sent.split():
            if word.lower() in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] += word_freq[word]



    num_sentences = 3
    summarized_sentences = nlargest(num_sentences, sent_score, key=sent_score.get)

    # Display summarized text in the result box
    result_box.delete(1.0, END)
    result_box.insert(END, " ".join(summarized_sentences))

# GUI setup
root = tk.Tk()
root.title("Extractive Text Summarizer")

# Text box for input
text_box = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_box.pack(pady=10)

# Entry field for the number of sentences
num_sentences_label = tk.Label(root, text="Number of Sentences:")
num_sentences_label.pack()
num_sentences_entry = tk.Entry(root, width=10)
num_sentences_entry.insert(END, "3")  # Default value
num_sentences_entry.pack()

# Button to summarize
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=5)

# Result box for output
result_box = scrolledtext.ScrolledText(root, width=50, height=5, wrap=tk.WORD)
result_box.pack(pady=10)

root.mainloop()