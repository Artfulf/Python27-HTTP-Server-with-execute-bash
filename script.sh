#!/bin/bash
if [ $# -eq 0 ]
  then
    cp tmp/test.txt tmp/test2.txt
  else
    FILE="tmp/$1"
    if [ -f "$FILE" ]; then
      cp tmp/$1 tmp/$2
    else
      exit 1
  fi
fi
