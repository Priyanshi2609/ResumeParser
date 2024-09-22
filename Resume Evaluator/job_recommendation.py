import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class JobRecommendation:
    def __init__(self, resume_text):
        self.resume_text = resume_text
        self.df = pd.read_csv("uploads/jobs_dataset_with_features.csv")
        self.tfidf_vectorizer = TfidfVectorizer()
        self.rf_classifier = RandomForestClassifier()
        self._prepare_data()

    def _prepare_data(self):
        min_count = 6500
        role_counts = self.df['Role'].value_counts()
        dropped_classes = role_counts[role_counts < min_count].index
        filtered_df = self.df[~self.df['Role'].isin(dropped_classes)].reset_index(drop=True)
        self.df = filtered_df.sample(n=10000)

        self.X = self.df['Features']
        self.y = self.df['Role']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # TF-IDF vectorization
        self.X_train_tfidf = self.tfidf_vectorizer.fit_transform(X_train)
        self.X_test_tfidf = self.tfidf_vectorizer.transform(X_test)

        # Train the classifier
        self.rf_classifier.fit(self.X_train_tfidf, y_train)

        # Predictions and accuracy
        y_pred = self.rf_classifier.predict(self.X_test_tfidf)
        accuracy = accuracy_score(y_test, y_pred)
        print("Model Accuracy:", accuracy)

    def clean_resume(self, text):
        clean_text = re.sub(r'http\S+\s', ' ', text)  # Remove URLs
        clean_text = re.sub(r'RT|cc', ' ', clean_text)  # Remove retweets and cc
        clean_text = re.sub(r'#\S+\s', ' ', clean_text)  # Remove hashtags
        clean_text = re.sub(r'@\S+', ' ', clean_text)  # Remove mentions
        clean_text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), ' ', clean_text)  # Remove punctuation
        clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)  # Remove non-ASCII characters
        clean_text = re.sub(r'\s+', ' ', clean_text)  # Remove extra whitespace
        return clean_text.strip()  # Strip leading and trailing whitespace

    def recommend_job(self):
        cleaned_resume = self.clean_resume(self.resume_text)
        resume_tfidf = self.tfidf_vectorizer.transform([cleaned_resume])
        predicted_role = self.rf_classifier.predict(resume_tfidf)[0]
        return predicted_role
