#! /bin/sh

# Wait for postgres to respond on port 5432
while ! nc -z postgres 5432; do sleep 2; done

# Run unit tests
scrapy check

# Run scraper(s)
scrapy crawl pep
