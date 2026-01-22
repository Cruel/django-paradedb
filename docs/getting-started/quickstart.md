# Quick Start

## Define your model with a BM25 index

```python
from django.db import models
from paradedb.indexes import BM25Index

class Product(models.Model):
    description = models.TextField()
    category = models.CharField(max_length=100)
    rating = models.IntegerField()

    class Meta:
        indexes = [
            BM25Index(
                fields={
                    'id': {},
                    'description': {
                        'tokenizer': 'simple',
                        'filters': ['lowercase', 'stemmer'],
                    },
                    'category': {
                        'tokenizer': 'simple',
                        'filters': ['lowercase'],
                    },
                },
                key_field='id',
                name='product_search_idx',
            ),
        ]
```

## Search your data

```python
from paradedb.search import ParadeDB

# Find products with "shoes"
Product.objects.filter(description=ParadeDB('shoes'))

# Find products with "running" AND "shoes"
Product.objects.filter(description=ParadeDB('running', 'shoes'))
```

See the [Guide](../guide/basic-search.md) for more examples.
