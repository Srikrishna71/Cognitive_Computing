import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
import re
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = """In a world that never stops moving, moments of stillness often hold the greatest value. Whether it’s the quiet before sunrise or the pause between two decisions, these small silences offer space for reflection and clarity. While technology races ahead, nature reminds us of the power in patience and balance. Life isn’t always about constant progress—it’s also about appreciating where we are. Sometimes, the most meaningful growth happens not in motion, but in stillness."""

# Q1

clean_text = re.sub(r'[^\w\s]', '', text.lower())
print("\n1. Cleaned text:\n", clean_text)

words = word_tokenize(clean_text)
sentences = sent_tokenize(text)
print("\n2. Word tokens:", words[:10], "...")
print("   Sentence tokens:", sentences[:2])

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]
print("\n3. After stopword removal:", filtered_words[:10], "...")

fdist = FreqDist(filtered_words)
print("\n4. Most common words:")
fd=FreqDist(filtered_words)
print(fd)
fd.plot(10, title="Top Words")

# Q2
# Initialize stemmers and lemmatizer
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_porter = [porter.stem(word) for word in filtered_words]
stemmed_lancaster = [lancaster.stem(word) for word in filtered_words]
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nOriginal words:", filtered_words[:10])
print("Porter stems:", stemmed_porter[:10])
print("Lancaster stems:", stemmed_lancaster[:10])
print("Lemmatized:", lemmatized[:10])

# Q3
# 2a
long_words = re.findall(r'\b\w{6,}\b', clean_text)
print("\na. Words with >5 letters:", long_words)

# 2b
numbers = re.findall(r'\d+', clean_text)
print("b. Numbers found:", numbers)

# 2c
capitalized = re.findall(r'\b[A-Z][a-z]+\b', text)
print("c. Capitalized words:", capitalized)

# 3a
alpha_words = re.findall(r'\b[a-z]+\b', clean_text)
print("\na. Alphabetic words:", alpha_words[:10], "...")

# 3b
vowel_words = re.findall(r'\b[aeiou][a-z]*\b', clean_text)
print("b. Words starting with vowels:", vowel_words)

# Q4
def custom_tokenizer(text):
    pattern = r"""
        \b\w+(?:'\w+)?\b          # words with optional contractions
        | \b\d+\.\d+\b            # decimal numbers
        | \b\d+\b                 # integers
        | \b\w+(?:-\w+)+\b        # hyphenated words
    """
    return re.findall(pattern, text, re.VERBOSE)

test_text = text + " Contact me at esingla_be23@thapar.edu or visit https://eshansingla.com. Call +91 9876543210."

tokens = custom_tokenizer(test_text.lower())
print("\n2. Custom tokens:", tokens)

cleaned_text = test_text
cleaned_text = re.sub(r'\S+@\S+', '<EMAIL>', cleaned_text)  
cleaned_text = re.sub(r'https?://\S+', '<URL>', cleaned_text)  
cleaned_text = re.sub(r'(\+\d{1,3} \d{10}|\d{3}-\d{3}-\d{4})', '<PHONE>', cleaned_text)  

print("\n3. After regex substitutions:")
print(cleaned_text)
