from insights.parsers import httpd_open_nfs
from insights.parsers.httpd_open_nfs import HttpdOnNFSFilesCount
from insights.tests import context_wrap
import doctest

http_nfs = """
{"http_ids": [1787, 2399], "nfs_mounts": ["/data", "/www"], "open_nfs_files": 1000}
""".strip()


class TestHttpOpenNFS():
    def test_http_nfs(self):
        httpd_nfs_counting = HttpdOnNFSFilesCount(context_wrap(http_nfs))
        assert len(httpd_nfs_counting.data) == 3
        assert httpd_nfs_counting.data.get("http_ids") == [1787, 2399]
        assert httpd_nfs_counting.data.get("nfs_mounts") == ["/data", "/www"]
        assert httpd_nfs_counting.data.get("open_nfs_files") == 1000


def test_http_nfs_documentation():
    env = {
        'httpon_nfs': HttpdOnNFSFilesCount(context_wrap(http_nfs))
    }
    failed, total = doctest.testmod(httpd_open_nfs, globs=env)
    assert failed == 0
