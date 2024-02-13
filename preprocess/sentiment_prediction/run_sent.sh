#!/bin/bash

r=5 #105 67-70
n=330000 #518488

i=1

while [ $i -lt $r ]; do
    echo $i
    python3 sentiment_pred_bash.py $n
    (( n += 5000 ))
    (( i += 1 ))

done


