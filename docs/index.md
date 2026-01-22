# django-paradedb

**ParadeDB full-text search integration for Django ORM**

django-paradedb brings Elasticsearch-quality full-text search to your Django applications using PostgreSQL and [ParadeDB](https://paradedb.com).

## Features

- **BM25 Search** - Industry-standard ranking algorithm
- **Django ORM Integration** - Familiar QuerySet interface
- **Search Expressions** - Phrase, Fuzzy, Regex, and more
- **Scoring & Snippets** - Relevance scores and highlighted excerpts
- **Faceted Search** - Aggregations for filtering UI

This is a **Django ORM plugin** that extends Django's query capabilities with ParadeDB operators. It generates the SQL - your PostgreSQL + ParadeDB instance executes it.

## Quick Example

```python
from paradedb.search import ParadeDB, Phrase
from paradedb.functions import Score, Snippet

# Simple search
Product.objects.filter(description=ParadeDB('running', 'shoes'))

# Phrase search with scoring
Product.objects.filter(
    description=ParadeDB(Phrase('wireless bluetooth'))
).annotate(
    score=Score(),
    snippet=Snippet('description')
).order_by('-score')
```

## Installation

```bash
pip install django-paradedb
```

See the [Getting Started](getting-started/installation.md) guide for full setup instructions.
