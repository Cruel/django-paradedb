# django-paradedb

[![CI](https://github.com/paradedb/django-paradedb/actions/workflows/ci.yml/badge.svg)](https://github.com/paradedb/django-paradedb/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/django-paradedb)](https://pypi.org/project/django-paradedb/)
[![Python](https://img.shields.io/pypi/pyversions/django-paradedb)](https://pypi.org/project/django-paradedb/)

ParadeDB full-text search integration for Django ORM.

## Installation

```bash
pip install django-paradedb
```

## Quick Start

```python
from django.db import models
from paradedb.indexes import BM25Index
from paradedb.search import ParadeDB

class Product(models.Model):
    description = models.TextField()
    category = models.CharField(max_length=100)

    class Meta:
        indexes = [
            BM25Index(
                fields={'id': {}, 'description': {'tokenizer': 'simple'}},
                key_field='id',
                name='product_search_idx',
            ),
        ]

# Search
Product.objects.filter(description=ParadeDB('shoes'))
```

## Documentation

Full documentation: https://paradedb.github.io/django-paradedb

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install

# Run tests
pytest

# Run linting
ruff check .
ruff format .

# Build docs locally
pip install -e ".[docs]"
mkdocs serve
```