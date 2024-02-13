#!/bin/bash

r=15 #105
n=450000 #518488

i=1

while [ $i -lt $r ]; do
    echo $i
    python3 jiaxin_pred_bash.py $n
    (( n += 5000 ))
    (( i += 1 ))
    
done
