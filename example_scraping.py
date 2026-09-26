#!/usr/bin/env python3
"""
Example: Scraping - Adaptive scraper that survives design changes
"""

from scrapling import Scraper, ScraperConfig

# Configure the scraper
config = ScraperConfig(
    headless=True,
    auto_save=True,  # Save selectors on first run
    adaptive=True,   # Find elements by similarity after redesign
    timeout=10
)

scraper = Scraper(config=config)

# Example 1: First run - save selectors and data
print("=== First scrape (saving selectors) ===")
result = scraper.scrape(
    url="https://example-news.com",
    selectors={
        "headline": "h1.main-title",
        "date": "span.publish-date",
        "content": "div.article-body"
    }
)
print(f"Headlines: {result.data['headline']}")
print(f"Date: {result.data['date']}")

# Example 2: Recurring collection - adaptive mode finds moved elements
print("\n=== Recurring scrape (adaptive mode) ===")
# Even if the site redesigns and moves elements, adaptive=True finds them
result = scraper.scrape(
    url="https://example-news.com",
    selectors={
        "headline": "h1.main-title",
        "date": "span.publish-date",
        "content": "div.article-body"
    },
    adaptive=True  # Will find elements by similarity if moved
)
print(f"Headlines: {result.data['headline']}")

# Example 3: Extract to Markdown
print("\n=== Extract to Markdown ===")
# scrapling extract get 'https://example.com' output.md
# (or programmatically:)
result = scraper.extract_to_markdown(
    url="https://example.com",
    output_file="output.md",
    remove_hidden=True  # Remove hidden text (anti-AI injections)
)

# Example 4: Schedule recurring collection
print("\n=== Schedule weekly collection ===")
scraper.schedule(
    url="https://example.com",
    frequency="weekly",
    selectors={"title": "h1", "price": ".price"},
    output_file="weekly_scrape.csv"
)
print("Scheduled for every week")

# Example 5: Use as MCP Server (in Claude Code)
# After: pip install "scrapling[all]" && scrapling install
# Then: claude mcp add ScrapingServer "<path-to-scrapling>"
# Claude can then call it when needed without managing selectors manually
