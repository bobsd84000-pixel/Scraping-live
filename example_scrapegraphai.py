#!/usr/bin/env python3
"""
Example: ScrapeGraphAI - Extract data from a page with a simple phrase
"""

from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

load_dotenv()

graph_config = {
    "llm": {
        "model": "ollama/llama3.2",  # Use local Ollama model (free)
        "temperature": 0,
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

# Simple phrase to describe what you want
prompt = "Get the title and price of each product"

# Create the scraper
scraper = SmartScraperGraph(
    prompt=prompt,
    source="https://example-ecommerce.com/products",
    config=graph_config
)

# Run and get results
result = scraper.run()
print(result)

# For multiple pages at once
# from scrapegraphai.graphs import SmartScraperMultiGraph
# urls = ["url1", "url2", "url3"]
# multi_scraper = SmartScraperMultiGraph(prompt=prompt, source=urls, config=graph_config)
# results = multi_scraper.run()
