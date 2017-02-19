#!/bin/bash
COUNTER=1
while [ $COUNTER -lt 6 ]; do
	./fastaToPhy.py sequence_$COUNTER.fasta sequence_$COUNTER.phy
	let COUNTER=COUNTER+1
done