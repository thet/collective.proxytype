# -*- coding: utf-8 -*-
from .interfaces import IProxyType
import plone.api.portal
import requests
import lxml


def get_content(remote_url):
    """Get remote html content.
    """

    res = requests.get(remote_url)
    ret = res.text

    # Replace all relative URLs to absolute ones.
    tree = lxml.html.fromstring(ret)
    tree.make_links_absolute(remote_url)
    ret = lxml.html.tostring(tree)

    cat = plone.api.portal.get_tool('portal_catalog')
    res = cat.searchResults(
        object_provides=IProxyType.__identifier__
    )

    # Create a list of remote_url, absolute_url tuples for the replacement
    repl_map = [
        (it.getObject().remote_url, it.getObject().absolute_url())
        for it in res
    ]
    # Reverse that list, so that longest remote_url paths are first.
    repl_map.sort(
        cmp=lambda x, y: cmp(len(x[0].split('/')), len(y[0].split('/'))),
        reverse=True
    )
    # Not, for all IProxyType, replace their remote_url with their absolute_url
    for remote_url, absolute_url in repl_map:
        ret = ret.replace(remote_url, absolute_url)

    return ret
