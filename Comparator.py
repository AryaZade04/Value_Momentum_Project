#older
def compare_policies(policies):
    summaries = []
    for i, text in enumerate(policies):
        summaries.append(f"Policy {i+1}: {len(text.split())} words long.")
    result = "\n".join(summaries)
    return "Comparison result:\n" + result

from transformers import pipeline
import re

# Load summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def clean_text(text):
    """Remove unwanted characters and compress whitespace."""
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text.strip()

def safe_summarize(text):
    """Summarize text safely."""
    text = clean_text(text)
    if not text or len(text.split()) < 30:
        return "Not enough content to summarize."

    # Truncate overly long text
    words = text.split()
    if len(words) > 800:
        text = " ".join(words[:800])

    try:
        output = summarizer(text, max_length=200, min_length=50, do_sample=False)
        if isinstance(output, list) and len(output) > 0 and "summary_text" in output[0]:
            return output[0]["summary_text"]
        else:
            return "Summary not available."
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def compare_policies(policies):
    """Compare and recommend best auto insurance policy."""
    summaries = []
    for i, text in enumerate(policies):
        summary = safe_summarize(text)
        summaries.append({"policy": f"Policy {i+1}", "summary": summary})

    # Keyword scoring for auto insurance relevance
    keywords = ["coverage", "premium", "claim", "limit", "deductible", "damage", "vehicle", "theft"]
    scores = []
    for s in summaries:
        score = sum(s['summary'].lower().count(k) for k in keywords)
        scores.append(score)

    best_index = scores.index(max(scores)) if scores else 0

    # Construct a readable comparison output
    comparison_text = "📊 Auto Insurance Policy Comparison\n"
    for s, sc in zip(summaries, scores):
        comparison_text += f"\n{s['policy']}:\n{s['summary']}\n⭐ Keyword Relevance Score: {sc}\n"

    comparison_text += f"\n🏆 Recommendation: {summaries[best_index]['policy']} appears to offer stronger coverage and better benefits overall."
    return comparison_text
