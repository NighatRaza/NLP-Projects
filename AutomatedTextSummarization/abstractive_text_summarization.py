from transformers import pipeline

import tkinter as tk

def summarize_text():
    # Get text from the input text box
    text = text_entry.get("1.0", "end-1c")

    summarizer = pipeline("summarization",model='t5-base',tokenizer='t5-base',framework='pt')

    summary = summarizer(text, max_length=100,min_length=10,do_sample=False)

    # Update the output text box with the summary
    output_text.delete("1.0", "end")
    output_text.insert("1.0", summary[0]['summary_text'])

# Create a Tkinter window
window = tk.Tk()
window.title("Abstractive Text Summarizer")

# Create input text box
text_entry = tk.Text(window, height=10, width=60)
text_entry.pack(pady=10)

# Create a button to trigger text summarization
summarize_button = tk.Button(window, text="Summarize", command=summarize_text)
summarize_button.pack()

# Create output text box
output_text = tk.Text(window, height=10, width=60)
output_text.pack(pady=10)

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="pt")

# Run the Tkinter event loop
window.mainloop()

