#!/bin/bash
#text=$1
readfile=$1
wordtocheck=$2
x=$(grep $wordtocheck $readfile | wc)
echo $x

