#!/usr/bin/env python

"""Tests for `async_get_web` package."""

import pytest


from async_get_web import *


@pytest.fixture
def webpages():
    urls = ["http://ruslan.rv.ua", "https://itvdn.com"]
    webpages = get_webpages(urls)
    return webpages


def test_content(webpages):
    from easy_file import TextFile

    assert len(webpages) == 2
    print()
    for w in webpages:
        print(f"{w.url} - {w.title}")
        TextFile(f"{w.title.split()[0]}.html").save(w.html)
