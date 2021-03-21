import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
import nltk
import praw
user_agent = "Scraper 1.0 by /u/sivahawking"
reddit = praw.Reddit(
    client_id="q1MeAXQMnJfPRQ",
    client_secret="t6euxwaBh9jMtHp8rNZZQMouHSNXGw",
    user_agent=user_agent
)

headlines = set()
for submission in reddit.subreddit('politics').hot(limit=None):
     print(submission.title)
     print(submission.id)
     print(submission.author)
     print(submission.score)
     print(submission.upvote_ratio)
     #break
     headlines.add(submission.title)
print(len(headlines))

df = pd.DataFrame(headlines)
print(df.head())
df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia=SIA()
results=[]
for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)
pprint(results[:3], width=100)
df= pd.DataFrame.from_records(results)
print(df.head())
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()
df2=df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv', encoding='utf-8',index=False)
print(df.label.value_counts())
df.label.value_counts(normalize=True) * 100
print("positive headlines:\n")
pprint(list(df[df['label']==1].headline)[:5], width=200)
print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)
fig, ax = plt.subplots(figsize=(8, 8))
counts = df.label.value_counts(normalize=True) * 100
sns.barplot(x=counts.index, y=counts, ax=ax)
ax.set_xticklabels(['negative','neutral','positive'])
ax.set_ylabel('Percentage')
plt.show()