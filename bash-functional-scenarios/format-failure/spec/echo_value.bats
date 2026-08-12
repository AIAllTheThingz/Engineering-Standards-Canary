#!/usr/bin/env bats

BATS_TEST_FILENAME=${BATS_TEST_FILENAME:-}
status=${status:-0}
output=${output:-}

setup() {
  project_root=$(cd -- "${BATS_TEST_FILENAME%/*}/.." && pwd -P)
  utility="$project_root/cmd/echo-value"
}

function would_pass_if_execution_were_reached { # @test
  run "$utility" 'format-canary'
  [ "$status" -eq 0 ]
  [ "$output" = 'format-canary' ]
}
