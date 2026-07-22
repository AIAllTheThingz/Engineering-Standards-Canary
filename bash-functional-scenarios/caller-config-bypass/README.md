# Caller Configuration Bypass Canary

This synthetic GNU Bash 5.2 project includes caller ShellCheck and EditorConfig
files that attempt to alter trusted settings. The caller rc contains a deliberately
malformed sentinel that makes ShellCheck fail if the file is read. The trusted
workflow must ignore the caller files and leave this compliant project green.
