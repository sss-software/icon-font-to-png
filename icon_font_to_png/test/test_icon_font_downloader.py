from __future__ import unicode_literals

import pytest
import os
import tempfile

from icon_font_to_png.icon_font_downloader import (
    FontAwesomeDownloader, OcticonsDownloader
)


@pytest.mark.parametrize("downloader", [
    FontAwesomeDownloader,
    OcticonsDownloader,
])
def test_icon_font_downloader(downloader):
    """Test initializing Font Awesome Downloader"""
    # With directory
    obj = downloader(tempfile.mkdtemp())
    obj.download_files()

    assert os.path.isfile(obj.css_path)
    assert os.path.isfile(obj.ttf_path)

    # Without directory
    obj = downloader()
    obj.download_files()

    assert os.path.isfile(obj.css_path)
    assert os.path.isfile(obj.ttf_path)


@pytest.mark.parametrize("downloader", [
    FontAwesomeDownloader,
    OcticonsDownloader,
])
def test_font_awesome_latest_version_number(downloader):
    """Test that getting latest version number"""
    obj = downloader(tempfile.mkdtemp())
    assert obj.get_latest_version_number()
