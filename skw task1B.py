class NGramLanguageModel:
    def __init__(self, n):
        self.n = n
        self.ngrams = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.n):
            ngram = tuple(words[i:i + self.n])
            next_word = words[i + self.n]
            if ngram in self.ngrams:
                self.ngrams[ngram].append(next_word)
            else:
                self.ngrams[ngram] = [next_word]

    def predict_next_word(self, words):
        if len(words) < self.n:
            return "Need more words to predict"
        ngram = tuple(words[-self.n:])
        if ngram in self.ngrams:
            return max(set(self.ngrams[ngram]), key=self.ngrams[ngram].count)
        else:
            return "No prediction available"

def main():
    n = 2  # Change the value of n for different n-gram models
    model = NGramLanguageModel(n)

    # Train the model with some sample text
    sample_text = "This is a sample text used to demonstrate the n-gram language model"
    model.train(sample_text)

    while True:
        input_text = input("Enter a sequence of words (type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break
        words = input_text.split()
        prediction = model.predict_next_word(words)
        print("Predicted next word:", prediction)

if __name__ == "__main__":
    main()
