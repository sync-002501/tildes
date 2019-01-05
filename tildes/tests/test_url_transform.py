# Copyright (c) 2018 Tildes contributors <code@tildes.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

from tildes.lib.url_transform import apply_url_transformations


def test_remove_utm_query_params():
    """Ensure that utm query params are removed but others are left."""
    url = "http://example.com/path?utm_source=tildes&utm_campaign=test&something=ok"
    cleaned_url = apply_url_transformations(url)

    assert cleaned_url == "http://example.com/path?something=ok"


def test_non_utm_params_unaffected():
    """Ensure that non-utm_ query params aren't removed."""
    url = "http://example.com/path?one=x&two=y&three=z"
    cleaned_url = apply_url_transformations(url)

    assert cleaned_url == url


def test_twitter_mobile_conversion():
    """Ensure that links to the Twitter mobile version are converted."""
    url = "https://mobile.twitter.com/acarboni/status/976545648391553024"
    cleaned_url = apply_url_transformations(url)

    assert cleaned_url == "https://twitter.com/acarboni/status/976545648391553024"


def test_other_mobile_subdomain_not_removed():
    """Ensure that the Twitter mobile conversion isn't hitting other domains."""
    url = "http://mobile.example.com/something"
    cleaned_url = apply_url_transformations(url)

    assert cleaned_url == url
