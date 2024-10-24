#!/usr/bin/env bash

echo "This is the standard output that will be silenced" > /dev/null
echo "This is the error msg that wil be silenced" > /dev/null >&2
exit 0
