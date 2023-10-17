#!/usr/bin/bash

echo "This is a standart output" > ~/ITstation/git_study/lesson_01/HW/stdout.txt
echo "This is an error msg" > ~/ITstation/git_study/lesson_01/HW/stderr.txt >&2
exit 0
