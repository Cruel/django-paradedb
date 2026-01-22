# Indexing

## BM25 Index Configuration

The `BM25Index` class defines which fields are searchable and how they're tokenized.

```python
from paradedb.indexes import BM25Index

BM25Index(
    fields={
        'id': {},
        'description': {
            'tokenizer': 'simple',
            'filters': ['lowercase', 'stemmer'],
            'stemmer': 'english',
        },
        'category': {
            'tokenizer': 'simple',
            'filters': ['lowercase'],
        },
    },
    key_field='id',
    name='product_search_idx',
)
```

## JSON Field Indexing

Index specific keys from JSON fields:

```python
BM25Index(
    fields={
        'id': {},
        'metadata': {
            'json_keys': {
                'title': {'tokenizer': 'simple', 'filters': ['lowercase']},
                'brand': {'tokenizer': 'simple', 'filters': ['lowercase']},
            }
        }
    },
    key_field='id',
    name='product_metadata_idx',
)
```
