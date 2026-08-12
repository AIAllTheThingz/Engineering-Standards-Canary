#!/usr/bin/env bats

BATS_TEST_FILENAME=${BATS_TEST_FILENAME:-}
status=${status:-0}
output=${output:-}

setup() {
  project_root=$(cd -- "${BATS_TEST_FILENAME%/*}/.." && pwd -P)
  utility="$project_root/cmd/echo-value"
}

function prints_a_synthetic_value { # @test
  run "$utility" 'functional-canary'
  [ "$status" -eq 0 ]
  [ "$output" = 'functional-canary' ]
}
