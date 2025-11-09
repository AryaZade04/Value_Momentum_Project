from transformers import pipeline
import torch
import re

# ✅ Use GPU if available
device = 0 if torch.cuda.is_available() else -1
print("Using device:", "GPU (T4)" if device == 0 else "CPU")

# ✅ Use a lightweight summarization model for better speed + quality
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    device=device
)

def clean_text(text):
    """Clean input text by removing unnecessary symbols and spaces."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[•●▪–-]+', '', text)
    text = text.replace("\n", " ").strip()
    return text

def bullet_point_format(text):
    """Convert summary text into neat bullet points."""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    bullets = [f"• {s.strip()}" for s in sentences if len(s.strip()) > 10]
    return "\n".join(bullets)

def summarize_policy(text, target_word_count=250):
    """Summarize large policy text into clean 250-word bullet points."""
    text = clean_text(text)
    max_chunk = 1000  # safe chunk size
    sentences = re.split(r'(?<=[.!?]) +', text)
    current_chunk = ""
    chunks = []

    # Split text into chunks for summarization
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())

    print(f"🔹 Total chunks: {len(chunks)}")

    summaries = []
    for i, chunk in enumerate(chunks, 1):
        print(f"⏳ Summarizing chunk {i}/{len(chunks)} ...")
        summary = summarizer(
            chunk,
            max_length=150,
            min_length=60,
            do_sample=False
        )[0]["summary_text"]
        summaries.append(summary)

    combined_summary = " ".join(summaries)

    # Trim final summary to ~250 words
    words = combined_summary.split()
    if len(words) > target_word_count:
        combined_summary = " ".join(words[:target_word_count]) + "..."

    formatted_summary = bullet_point_format(combined_summary)
    return formatted_summary.strip()
