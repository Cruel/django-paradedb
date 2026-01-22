"""Tests for SQL generation.

This plugin tests SQL string generation only - no database required.
Uses syrupy for snapshot testing. Run `pytest --snapshot-update` to update.

Example test pattern:
    def test_and_search(snapshot):
        queryset = Product.objects.filter(description=ParadeDB('a', 'b'))
        assert str(queryset.query) == snapshot
"""


class TestParadeDBLookup:
    """Test ParadeDB lookup SQL generation."""

    def test_placeholder(self) -> None:
        """Placeholder - replace with SQL generation tests."""
        # Example:
        # queryset = Product.objects.filter(description=ParadeDB('shoes'))
        # sql = str(queryset.query)
        # assert sql == snapshot
        assert True
