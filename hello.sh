#!/bin/bash
echo '====================================='
echo '  Hello from a BASH script (via Fluwent)'
echo '====================================='
echo
echo "Host:      $(hostname)"
echo "User:      $(whoami)"
echo "OS:        $(uname -srm)"
echo "Date:      $(date -Iseconds)"
echo "Script:    $0"
echo
echo 'sys argv equivalent ($@):'
i=1
for arg in "$@"; do
  echo "  arg[${i}] = ${arg}"
  i=$((i+1))
done
echo
echo 'Status: SUCCESS'
