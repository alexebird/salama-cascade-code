#!/usr/bin/env bash
set -euo pipefail
# set -v

main() {
    echo building

    # if git diff-index --quiet HEAD --; then
    #     # Working tree is clean
    #     sha=$(git rev-parse HEAD)
    #     # Attempt to get the tag name exactly on HEAD
    #     tag=$(git describe --tags --exact-match HEAD 2> /dev/null)
    #     if [ -n "$tag" ]; then
    #         # If there is a tag exactly on HEAD, append it to the SHA
    #         echo "${sha} (${tag})" > version.txt
    #     else
    #         # If no tag on HEAD, just write the SHA
    #         echo "$sha" > version.txt
    #     fi
    # else
    #     # Working tree is not clean
    #     sha=$(git rev-parse HEAD)
    #     # Attempt to get the tag name exactly on HEAD
    #     tag=$(git describe --tags --exact-match HEAD 2> /dev/null)
    #     if [ -n "$tag" ]; then
    #         # If there is a tag exactly on HEAD, append it to the SHA and mark as dirty
    #         echo "${sha}+dirty (${tag})" > version.txt
    #     else
    #         # If no tag on HEAD, just write the SHA and mark as dirty
    #         echo "${sha}+dirty" > version.txt
    #     fi
    # fi
    #
    # cat version.txt

    rm -rfv "${BIRD}/build/salama_cascade_out"
    mkdir -p "${BIRD}/build/salama_cascade_out/levels/salama_cascade"

    cp -a * "${BIRD}/build/salama_cascade_out/levels/salama_cascade"

    cd "${BIRD}/build/salama_cascade_out/levels/salama_cascade" && rm -rf .git .gitignore .gitattributes build.sh dev.txt dev
    rm -fv "${BIRD}/build/salama_cascade.zip"
    cd "${BIRD}/build/salama_cascade_out"
    zip -r "${BIRD}/build/salama_cascade.zip" ./*
    # zip -r "${BIRD}/build/salama_cascade.zip" ./* -x '*.git*' -x 'build.sh' -x 'dev.txt' -x 'dev'
    # rm -fv version.txt
    ls -ltrh "${BIRD}/build/"
}

main "$@"
