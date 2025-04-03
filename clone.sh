#|/usr/bin/env bash
cat repos.txt | xargs -P 16 -I + bash -c '[ -d "$(basename "$0")" ] || git clone git@github.com:$0.git' +

