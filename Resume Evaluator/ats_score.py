from transformers import BertTokenizer, BertModel
import torch
import PyPDF2
import re
class ResumeMatcher:
    def __init__(self,resume_text):
        # Initialize BERT tokenizer and model
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.resume_text=resume_text
        self.resume_text = self.clean_resume(resume_text)
        
    def clean_resume(self, text):
        clean_text = re.sub(r'http\S+\s', ' ', text)  # Remove URLs
        clean_text = re.sub(r'RT|cc', ' ', clean_text)  # Remove retweets and cc
        clean_text = re.sub(r'#\S+\s', ' ', clean_text)  # Remove hashtags
        clean_text = re.sub(r'@\S+', ' ', clean_text)  # Remove mentions
        clean_text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), ' ', clean_text)  # Remove punctuation
        clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)  # Remove non-ASCII characters
        clean_text = re.sub(r'\s+', ' ', clean_text)  # Remove extra whitespace
        clean_text.strip()  # Strip leading and trailing whitespace
        return clean_text
    
    def get_embeddings(self, text):
        """Get BERT embeddings for the given text."""
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

    def compute_matching_score(self, resume_text, job_description_text):
        """Compute the matching score between resume and job description."""
        job_description_text = self.clean_resume(job_description_text)
        resume_embedding = self.get_embeddings(resume_text)
        job_description_embedding = self.get_embeddings(job_description_text)
        
        # Compute cosine similarity
        similarity_score = torch.nn.functional.cosine_similarity(resume_embedding, job_description_embedding)
        return similarity_score.item() * 100  # Convert to percentage
