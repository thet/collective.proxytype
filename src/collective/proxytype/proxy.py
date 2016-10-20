# -*- coding: utf-8 -*-
from .interfaces import IProxyType
import plone.api.portal
import requests
import lxml

import re


def get_content(
    remote_url,
    content_selector=None,
    append_script=False,
    append_style=False,
    append_link=False
):
    """Get remote html content.
    """

    res = requests.get(remote_url)
    ret = res.text

    # Replace all relative URLs to absolute ones.
    tree = lxml.html.fromstring(ret)
    tree.make_links_absolute(remote_url)

    c_tree = tree.cssselect(content_selector) if content_selector else [tree]

    append = []
    if append_script:
        append += tree.cssselect('html head script')
    if append_style:
        append += tree.cssselect('html head style')
    if append_link:
        append += tree.cssselect('html head link')

    for el in append:
        # Append to last selected element
        c_tree[-1].append(el)

    # serialize all selected elements in order from the content tree
    ret = u'\n'.join([lxml.html.tostring(el) for el in c_tree])

    cat = plone.api.portal.get_tool('portal_catalog')
    res = cat.searchResults(
        object_provides=IProxyType.__identifier__
    )

    # Create a list of remote_url, absolute_url tuples for the replacement
    repl_map = [
        (
            it.getObject().remote_url,
            u'/'.join([it.getObject().absolute_url(), '@@proxyview']),
            it.getObject().exclude_urls
        )
        for it in res
    ]

    # Reverse sort the replacement values to support proxyviews in proxyviews
    repl_map.sort(
        key=lambda el: el[1],
        reverse=True
    )

    # Now, for all IProxyType, replace their remote_url with their absolute_url
    for remote_url_, absolute_url_, exclude_urls_ in repl_map:
        rec = re.compile('(?!({0})){1}'.format(
            '|'.join(exclude_urls_ or ()),
            remote_url_
        ))
        ret = rec.sub(absolute_url_, ret)

    return ret
