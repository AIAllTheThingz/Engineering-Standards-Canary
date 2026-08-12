#!/usr/bin/env bash

unused_marker='caller-rc-must-not-suppress-SC2034'

canary_print_value() {
  if (($# != 1)); then
    return 64
  fi
  printf '%s\n' "$1"
}
