#!/usr/bin/env bash

canary_print_value() {
  if (($# != 1)); then
    return 64
  fi
    printf '%s\n' "$1"
}
