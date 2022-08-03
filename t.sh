#!/bin/bash

while getopts 'a:h' opt; do
  case "$opt" in
    a)
      echo "Processing option 'a'"
      ;;
   
    ?|h)
      echo "Usage: $(basename $0) [-a] [-b] [-c arg]"
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"