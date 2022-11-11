from typing import List


def pytest_collection_modifyitems(items: List):
    items.sort(key=lambda item: item.name)
