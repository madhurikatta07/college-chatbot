import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.tokenize import word_tokenize

# Make sure NLTK dependencies are downloaded
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print(f"Warning: NLTK download failed visually: {e}")

def load_intents():
    with open('intents.json', 'r') as f:
        data = json.load(f)
    return data

def train():
    print("Loading data...")
    data = load_intents()
    
    X = []
    y = []

    for intent in data['intents']:
        tag = intent['tag']
        for pattern in intent['patterns']:
            X.append(pattern)
            y.append(tag)
            
    print(f"Loaded {len(X)} training samples.")
    
    # Text vectorization and model pipeline
    print("Building model pipeline...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            tokenizer=word_tokenize, 
            stop_words='english',
            token_pattern=None # Suppress warning when using custom tokenizer
        )),
        ('clf', MultinomialNB())
    ])
    
    print("Training model...")
    pipeline.fit(X, y)
    
    # Test accuracy on training set
    accuracy = pipeline.score(X, y)
    print(f"Training Accuracy: {accuracy * 100:.2f}%")
    
    print("Saving model and data to model.pkl...")
    model_data = {
        "pipeline": pipeline,
        "intents": data
    }
    with open('model.pkl', 'wb') as f:
        pickle.dump(model_data, f)
        
    print("Model generated successfully.")

if __name__ == "__main__":
    train()
