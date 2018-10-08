#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : git_clone_all_repository.py
# @Author: lucas
# @Date  : 10/7/18
# @Desc  :


import os
import requests
from pprint import pprint


def get_all_repositories(group, name):
    page = 1
    while True:
        url = 'https://api.github.com/{0}/{1}/repos?per_page=100&page={2}'
        resp = requests.get(url.format(group, name, page))

        if resp.status_code == 200:
            resp_data = resp.json()
            repo_urls = [repo for repo in resp_data if repo is not None]

            if len(resp_data) >= 100:
                page += 1

            else:
                pprint('Found {0} repos.'.format(len(repo_urls)))
                break

        else:
            pprint(resp)
            return False

    return repo_urls


def clone_repositories(all_repositories):
    count = 1
    pprint('do cloning...')

    for repo in all_repositories:
        os.system('git clone %s' % repo)
        pprint('Completed #{0} of #{1} '.format(count, len(all_repositories)))
        count += 1


def run():
    group, name = 'ET-Planet', 'py-ai'
    total = get_all_repositories(group, name)

    if total:
        clone_repositories(total)


if __name__ == '__main__':
    run()
