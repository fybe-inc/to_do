import requests
import json
from datetime import datetime, timedelta
import os

# X API endpoint
SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

# Date range (Jan 13-16, 2025)
end_date = datetime(2025, 1, 16)
start_date = datetime(2025, 1, 13)

# Search queries
queries = [
    '(AI Agent) min_faves:300 lang:en',
    '(AI エージェント) min_faves:300 lang:ja'
]

def search_tweets():
    headers = {
        "Authorization": f"Bearer {os.environ.get('TWITTER_BEARER_TOKEN')}"
    }
    
    all_tweets = []
    
    for query in queries:
        params = {
            'query': query,
            'max_results': 100,
            'tweet.fields': 'created_at,public_metrics,lang',
            'start_time': start_date.isoformat() + 'Z',
            'end_time': end_date.isoformat() + 'Z'
        }
        
        try:
            response = requests.get(SEARCH_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data:
                all_tweets.extend(data['data'])
                
        except Exception as e:
            print(f"Error searching tweets: {e}")
    
    return all_tweets

def filter_tweets(tweets):
    """Filter tweets based on criteria"""
    filtered = []
    for tweet in tweets:
        # Check likes count
        if tweet['public_metrics']['like_count'] >= 300:
            # Add to filtered list if it contains tool/know-how content
            # (This would need manual review)
            filtered.append(tweet)
    return filtered

def format_for_markdown(tweets):
    """Format tweets for markdown table"""
    markdown_rows = []
    for tweet in tweets:
        created_at = datetime.fromisoformat(tweet['created_at'].replace('Z', '+00:00'))
        likes = tweet['public_metrics']['like_count']
        url = f"https://twitter.com/i/web/status/{tweet['id']}"
        
        row = f"| {created_at.strftime('%Y-%m-%d %H:%M')} | {url} | {likes} | TODO | TODO |"
        markdown_rows.append(row)
    
    return "\n".join(markdown_rows)

def main():
    tweets = search_tweets()
    filtered_tweets = filter_tweets(tweets)
    markdown_content = format_for_markdown(filtered_tweets)
    
    # Print results for manual review
    print(markdown_content)

if __name__ == "__main__":
    main()
