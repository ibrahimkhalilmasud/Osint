#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
python -m pip install holehe maigret h8mail sherlock-project socialscan theHarvester

if ! command -v amass >/dev/null 2>&1; then
  echo "amass binary must be provided in base image or host package manager"
fi
if ! command -v subfinder >/dev/null 2>&1; then
  echo "subfinder binary must be provided in base image or host package manager"
fi
if ! command -v dnsx >/dev/null 2>&1; then
  echo "dnsx binary must be provided in base image or host package manager"
fi
if ! command -v exiftool >/dev/null 2>&1; then
  echo "exiftool missing; install package libimage-exiftool-perl"
fi
