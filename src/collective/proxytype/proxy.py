import requests


def get_content(remote_url, context_url=None, replacement_map=None):

    res = requests.get(remote_url)
    ret = res.text

    if context_url:
        ret.replace(remote_url, context_url)

    for it in replacement_map:
        old, new = it.split('|')
        ret.replace(old, new)

    return ret
