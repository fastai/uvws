#!/usr/bin/env bash
cat repos.txt | xargs -P 16 -I+ bash -c 'cd "$(basename +)" && git pull -q --stat'

