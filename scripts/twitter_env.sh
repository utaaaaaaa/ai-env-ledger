#!/bin/bash
# twitter_env.sh — run a command with Twitter credentials + local proxy loaded.
# Usage: bash twitter_env.sh twitter search "query" -n 5
# Loads AUTH_TOKEN/CT0 from ~/.config/bird/credentials.env into TWITTER_* vars.

CRED="$HOME/.config/bird/credentials.env"
if [ ! -f "$CRED" ]; then
  echo "credential file missing: $CRED" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
. "$CRED"
set +a

export TWITTER_AUTH_TOKEN="${AUTH_TOKEN:-}"
export TWITTER_CT0="${CT0:-}"
# Always prefer the local mihomo core; the ambient HTTP_PROXY may point elsewhere.
# Override with TWITTER_PROXY=... if needed.
PROXY="${TWITTER_PROXY:-http://127.0.0.1:7890}"
export HTTP_PROXY="$PROXY"
export HTTPS_PROXY="$PROXY"

if [ "$#" -eq 0 ]; then
  echo "Twitter env loaded (TWITTER_AUTH_TOKEN=${#TWITTER_AUTH_TOKEN} chars, proxy=$HTTP_PROXY)"
  exit 0
fi

exec "$@"