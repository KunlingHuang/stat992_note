#!/bin/bash
echo "script name: $0"
echo "first argument: $1"
echo "number of arguments: $#"
(head -n 2; tail -n 2) < "$1"
