#!/bin/bash

for py_file in $(find $YOUR_FOLDER -name *.py)
do
    python $py_file
done
