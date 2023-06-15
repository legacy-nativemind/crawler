# Web Crawler and Backlink Collector

This is a Python project aimed at crawling the internet starting from a set of seed domains and collecting backlinks across websites. It utilizes a structured MySQL database for organizing and storing the crawled information. 

## Table of Contents

1. [Data Structure](#data-structure)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Contribute](#contribute)

## Data Structure

The application operates on four main tables:

1. `domains` 
2. `links`
3. `pages`
4. `zones`

### Domains Table

This table stores information about each domain that the crawler visits. 

- `id`: Unique identifier for the domain.
- `zone_id`: Identifier linking to the `zones` table.
- `domain`: The domain name.
- `domain_is2`: Binary value indicating a condition for the domain.
- `add_timestamp`: The timestamp when the domain was added to the database.
- `check_timestamp`: The timestamp when the domain was last checked.
- `expire_timestamp`: The timestamp when the domain is set to expire.
- `is_free`: Binary value indicating whether the domain is free.
- `is_offline`: Binary value indicating whether the domain is offline.
- `level`: Integer indicating the depth level of the domain in the crawl.
- `disabled`: Binary value indicating whether the domain is disabled.

### Links Table

This table stores data about the links that are discovered during the crawl.

- `id`: Unique identifier for the link.
- `from_page_id`: Identifier for the page where the link originates.
- `to_page_id`: Identifier for the page where the link leads.
- `has_a_text`: Binary value indicating whether the link has anchor text.
- `a_text`: The anchor text of the link.
- `before_text`: The text before the link on the page.
- `after_text`: The text after the link on the page.
- `first_seen_timestamp`: The timestamp when the link was first seen.
- `last_seen_timestamp`: The timestamp when the link was last seen.
- `blinked`: Integer indicating the number of times the link blinked (disappeared and reappeared).

### Pages Table

This table contains data about individual pages on a domain.

- `id`: Unique identifier for the page.
- `domain_id`: Identifier linking to the `domains` table.
- `url`: The URL of the page.
- `is_index`: Binary value indicating whether the page is the index page of the domain.
- `add_timestamp`: The timestamp when the page was added to the database.
- `crawled`: Binary value indicating whether the page has been crawled.
- `success`: Binary value indicating whether the page was successfully crawled.
- `crawl_timestamp`: The timestamp when the page was last crawled.

### Zones Table

This table categorizes domains into various zones.

- `id`: Unique identifier for the zone.
- `zone`: The name of the zone.
- `disabled`: Binary value indicating whether the zone is disabled.

## Setup

[Details on setup and installation.]

## Usage

[Details on how to use the software.]

## Contribute

[Information on how to contribute to the project.]

This repository is open for enhancements, bug-fixing, or any other forms of contribution. Please follow the standard procedure for submitting pull requests.

## License

[License details.]


