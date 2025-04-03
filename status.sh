#!/usr/bin/env bash
while read repo; do
   d=$(basename $repo)
   pushd "$d" >/dev/null || continue
   changes=$(git status -s)
   unpushed=$(git log --branches --not --remotes 2>/dev/null | grep commit)
   if [[ -n "$changes$unpushed" ]]; then
     echo -e "\n=== $d ===\n$changes$unpushed"
   fi
   popd >/dev/null
done < repos.txt
