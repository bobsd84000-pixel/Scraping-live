#!/usr/bin/env python3
"""
Example: Agent Reach - Access Reddit, X, YouTube, GitHub without API keys
"""

from agent_reach import AgentReach

# Initialize Agent Reach
agent = AgentReach()

# Example 1: Search Reddit for mentions (requires connected Reddit account)
reddit_results = agent.reddit_search(
    query="Claude AI",
    time_filter="week"
)
print("Reddit Results:")
for post in reddit_results[:5]:
    print(f"- {post['title']} (u/{post['author']})")

# Example 2: Search X/Twitter (requires connected account)
x_results = agent.x_search(
    query="web scraping",
    result_type="latest"
)
print("\nX Results:")
for tweet in x_results[:5]:
    print(f"- {tweet['text']}")

# Example 3: Get YouTube video transcription
youtube_results = agent.youtube_search(
    query="data extraction tutorial",
    max_results=3
)
print("\nYouTube Videos:")
for video in youtube_results:
    print(f"- {video['title']}")
    # Get transcript
    transcript = agent.youtube_transcript(video['video_id'])
    print(f"  Transcript preview: {transcript[:200]}...")

# Example 4: Search GitHub
github_results = agent.github_search(
    query="web scraper Python",
    language="python"
)
print("\nGitHub Repos:")
for repo in github_results[:3]:
    print(f"- {repo['name']} ({repo['stars']} stars)")

# Example 5: Read public LinkedIn profile (no login needed)
linkedin_profile = agent.linkedin_public_profile(
    profile_url="https://linkedin.com/in/someone"
)
print(f"\nLinkedIn: {linkedin_profile['name']}")
