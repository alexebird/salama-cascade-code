#!/usr/bin/env bash
set -euo pipefail

gsutil rsync \
    -r -d -u \
    -x "(\.git/.*|dev/Caches/.*|dev/blender_out|dev/build_gaea|dev/tmp|dev/build_gaea_stage2|dev/build_geoscatter|dev/build_old|.gitignore|.gitattributes|dev/.gitignore|.*\.blend1)" \
    ./ \
    gs://beamng-maps/salama_cascade/
