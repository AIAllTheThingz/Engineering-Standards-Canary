# Caller Configuration Bypass Canary

This synthetic GNU Bash 5.2 project includes caller ShellCheck and EditorConfig
files that attempt to alter trusted settings. The caller rc disables SC2034, while
the governed source contains an intentional SC2034 unused-variable finding. The
trusted workflow must ignore the caller suppression, fail exactly at ShellCheck,
leave formatting passed, mark Bats `NotRun`, and upload complete failure evidence.
