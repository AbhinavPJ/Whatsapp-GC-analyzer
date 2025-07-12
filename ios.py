import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from datetime import datetime
def clean_unicode(s):
    return s.replace('\u200e', '').replace('\u202f', ' ').strip()
def parse_line(line):
    pattern = r'^\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2})\u202f?(AM|PM)\] (.*?): (.*)'
    match = re.match(pattern, line)
    if match:
        date_str, time_str, am_pm, sender, message = match.groups()
        dt_str = f"{date_str} {time_str} {am_pm}"
        dt = datetime.strptime(dt_str, "%d/%m/%y %I:%M:%S %p")
        return dt, clean_unicode(sender), clean_unicode(message)
    return None
def is_message(line):
    return line.startswith("[")
def analyze_chat(filepath):
    records = []
    all_text = ""

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if is_message(line):
                parsed = parse_line(line)
                if parsed:
                    dt, sender, message = parsed

                    # Skip system messages
                    if "end-to-end encrypted" in message.lower():
                        continue
                    if "changed the group" in message.lower():
                        continue
                    if "turned on" in message.lower() or "turned off" in message.lower():
                        continue

                    records.append((dt, sender, message))
                    all_text += " " + message
    df = pd.DataFrame(records, columns=["datetime", "sender", "message"])
    df = df.dropna()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['date'] = df['datetime'].dt.date
    df['hour'] = df['datetime'].dt.hour
    df['word_count'] = df['message'].apply(lambda x: len(x.split()))
    msg_per_user = df['sender'].value_counts().head(30)
    plt.figure(figsize=(8,5))
    msg_per_user.plot(kind='bar', color='skyblue')
    plt.title("Messages per User")
    plt.ylabel("Number of messages")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("1a.png")
    words_per_day = df.groupby('date')['word_count'].sum()
    plt.figure(figsize=(10,5))
    words_per_day.plot()
    plt.title("Words Sent Per Day")
    plt.ylabel("Total words")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.savefig("2.png")
    avg_msgs_per_hour = df.groupby('hour').size()
    plt.figure(figsize=(8,5))
    avg_msgs_per_hour.plot(kind='bar', color='salmon')
    plt.title("Average Number of Messages Per Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of messages")
    plt.tight_layout()
    plt.savefig("3.png")
    STOPWORDS.add("Message")
    STOPWORDS.add("deleted")
    # ☁️ Word Cloud
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          stopwords=stopwords).generate(all_text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Most Common Words (Word Cloud)")
    plt.savefig("4.png")

# Call the function
analyze_chat("batch.txt")
