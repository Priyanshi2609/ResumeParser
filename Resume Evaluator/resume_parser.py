import re
class ResumeParser:
    def __init__(self, resume_text):
        self.resume_text=resume_text
        
    def extract_name_from_resume(self):
        name = None
        lines = self.resume_text.strip().splitlines()  # Use self.resume_text here
        name_pattern = r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$|^[A-Z]+(?: [A-Z]+)+$"
        first_line = lines[0].strip()
        if re.match(name_pattern, first_line):
            name = first_line
        else:
            for line in lines[:5]:
                if re.match(name_pattern, line.strip()):
                    name = line.strip()
                    break
        return name
    
    def extract_contact_number_from_resume(self):
        contact_number = None
        pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
        match = re.search(pattern, self.resume_text)  # Use self.resume_text here
        if match:
            contact_number = match.group()
        return contact_number

    
    def extract_email_from_resume(self):
        email = None
        # Use regex pattern to find a potential email address
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        match = re.search(pattern, self.resume_text)  # Use self.resume_text here
        if match:
            email = match.group()
        return email

    
    def extract_skills_from_resume(self):
        skills_list = [
        'Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 
        'Deep Learning', 'SQL', 'Tableau', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS', 
        'React', 'Angular', 'Node.js', 'MongoDB', 'Express.js', 'Git', 'Research', 'Statistics',
        'Quantitative Analysis', 'Qualitative Analysis', 'SPSS', 'R', 'Data Visualization', 
        'Matplotlib', 'Seaborn', 'Plotly', 'Pandas', 'Numpy', 'Scikit-learn', 'TensorFlow', 
        'Keras', 'PyTorch', 'NLTK', 'Text Mining', 'Natural Language Processing', 'Computer Vision', 
        'Image Processing', 'OCR', 'Speech Recognition', 'Recommendation Systems', 
        'Collaborative Filtering', 'Content-Based Filtering', 'Reinforcement Learning', 
        'Neural Networks', 'Convolutional Neural Networks', 'Recurrent Neural Networks', 
        'Generative Adversarial Networks', 'XGBoost', 'Random Forest', 'Decision Trees', 
        'Support Vector Machines', 'Linear Regression', 'Logistic Regression', 'K-Means Clustering', 
        'Hierarchical Clustering', 'DBSCAN', 'Association Rule Learning', 'Apache Hadoop', 
        'Apache Spark', 'MapReduce', 'Hive', 'HBase', 'Apache Kafka', 'Data Warehousing', 
        'ETL', 'Big Data Analytics', 'Cloud Computing', 'Amazon Web Services (AWS)', 
        'Microsoft Azure', 'Google Cloud Platform (GCP)', 'Docker', 'Kubernetes', 'Linux', 
        'Shell Scripting', 'Cybersecurity', 'Network Security', 'Penetration Testing', 
        'Firewalls', 'Encryption', 'Malware Analysis', 'Digital Forensics', 'CI/CD', 'DevOps', 
        'Agile Methodology', 'Scrum', 'Kanban', 'Continuous Integration', 'Continuous Deployment', 
        'Software Development', 'Web Development', 'Mobile Development', 'Backend Development', 
        'Frontend Development', 'Full-Stack Development', 'UI/UX Design', 'Responsive Design', 
        'Wireframing', 'Prototyping', 'User Testing', 'Adobe Creative Suite', 'Photoshop', 
        'Illustrator', 'InDesign', 'Figma', 'Sketch', 'Zeplin', 'InVision', 'Product Management', 
        'Market Research', 'Customer Development', 'Lean Startup', 'Business Development', 
        'Sales', 'Marketing', 'Content Marketing', 'Social Media Marketing', 'Email Marketing', 
        'SEO', 'SEM', 'PPC', 'Google Analytics', 'Facebook Ads', 'LinkedIn Ads', 'Lead Generation', 
        'Customer Relationship Management (CRM)', 'Salesforce', 'HubSpot', 'Zendesk', 'Intercom', 
        'Customer Support', 'Technical Support', 'Troubleshooting', 'Ticketing Systems', 'ServiceNow', 
        'ITIL', 'Quality Assurance', 'Manual Testing', 'Automated Testing', 'Selenium', 'JUnit', 
        'Load Testing', 'Performance Testing', 'Regression Testing', 'Black Box Testing', 
        'White Box Testing', 'API Testing', 'Mobile Testing', 'Usability Testing', 
        'Accessibility Testing', 'Cross-Browser Testing', 'Agile Testing', 'User Acceptance Testing', 
        'Software Documentation', 'Technical Writing', 'Copywriting', 'Editing', 'Proofreading', 
        'Content Management Systems (CMS)', 'WordPress', 'Joomla', 'Drupal', 'Magento', 'Shopify', 
        'E-commerce', 'Payment Gateways', 'Inventory Management', 'Supply Chain Management', 
        'Logistics', 'Procurement', 'ERP Systems', 'SAP', 'Oracle', 'Microsoft Dynamics', 'Tableau', 
        'Power BI', 'QlikView', 'Looker', 'Data Warehousing', 'ETL', 'Data Engineering', 
        'Data Governance', 'Data Quality', 'Master Data Management', 'Predictive Analytics', 
        'Prescriptive Analytics', 'Descriptive Analytics', 'Business Intelligence', 'Dashboarding', 
        'Reporting', 'Data Mining', 'Web Scraping', 'API Integration', 'RESTful APIs', 
        'GraphQL', 'SOAP', 'Microservices', 'Serverless Architecture', 'Lambda Functions', 
        'Event-Driven Architecture', 'Message Queues', 'GraphQL', 'Socket.io', 'WebSockets', 
        'Ruby', 'Ruby on Rails', 'PHP', 'Symfony', 'Laravel', 'CakePHP', 'Zend Framework', 
        'ASP.NET', 'C#', 'VB.NET', 'ASP.NET MVC', 'Entity Framework', 'Spring', 'Hibernate', 
        'Struts', 'Kotlin', 'Swift', 'Objective-C', 'iOS Development', 'Android Development', 
        'Flutter', 'React Native', 'Ionic', 'Mobile UI/UX Design', 'Material Design', 
        'SwiftUI', 'RxJava', 'RxSwift', 'Django', 'Flask', 'FastAPI', 'Falcon', 'Tornado', 
        'WebSockets', 'GraphQL', 'RESTful Web Services', 'SOAP', 'Microservices Architecture', 
        'Serverless Computing', 'AWS Lambda', 'Google Cloud Functions', 'Azure Functions', 
        'Server Administration', 'System Administration', 'Network Administration', 
        'Database Administration', 'MySQL', 'PostgreSQL', 'SQLite', 'Microsoft SQL Server', 
        'Oracle Database', 'NoSQL', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 
        'Firebase', 'Google Analytics', 'Google Tag Manager', 'Adobe Analytics', 
        'Marketing Automation', 'Customer Data Platforms', 'Segment', 
        'Salesforce Marketing Cloud', 'HubSpot CRM', 'Zapier', 'IFTTT', 'Workflow Automation', 
        'Robotic Process Automation (RPA)', 'UI Automation', 'Natural Language Generation (NLG)', 
        'Virtual Reality (VR)', 'Augmented Reality (AR)', 'Mixed Reality (MR)', 'Unity', 
        'Unreal Engine', '3D Modeling', 'Animation', 'Motion Graphics', 'Game Design', 
        'Game Development', 'Level Design', 'Unity3D', 'Unreal Engine 4', 'Blender', 'Maya', 
        'Adobe After Effects', 'Adobe Premiere Pro', 'Final Cut Pro', 'Video Editing', 
        'Audio Editing', 'Sound Design', 'Music Production', 'Digital Marketing', 'Content Strategy', 
        'Conversion Rate Optimization (CRO)', 'A/B Testing', 'Customer Experience (CX)', 
        'User Experience (UX)', 'User Interface (UI)', 'Persona Development', 
        'User Journey Mapping', 'Information Architecture (IA)', 'Wireframing', 'Prototyping', 
        'Usability Testing', 'Accessibility Compliance', 'Internationalization (I18n)', 
        'Localization (L10n)', 'Voice User Interface (VUI)', 'Chatbots', 'Natural Language Understanding (NLU)', 
        'Speech Synthesis', 'Emotion Detection', 'Sentiment Analysis', 'Image Recognition', 
        'Object Detection', 'Facial Recognition', 'Gesture Recognition', 'Document Recognition', 
        'Fraud Detection', 'Cyber Threat Intelligence', 'Security Information and Event Management (SIEM)', 
        'Vulnerability Assessment', 'Incident Response', 'Forensic Analysis', 
        'Security Operations Center (SOC)', 'Identity and Access Management (IAM)', 
        'Single Sign-On (SSO)', 'Multi-Factor Authentication (MFA)', 'Blockchain', 
        'Cryptocurrency', 'Decentralized Finance (DeFi)', 'Smart Contracts', 'Web3', 
        'Non-Fungible Tokens (NFTs)'
        ]
        skills=[]
        for skill in skills_list:
            pattern = r"\b{}\b".format(re.escape(skill))
            if re.search(pattern,self.resume_text, re.IGNORECASE):  # Use self.resume_text here
                skills.append(skill)
        return skills