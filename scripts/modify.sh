#!/bin/bash
sed -E 's/"([0-9]*),?([0-9]+),([0-9]+)"/\1\2\3/' tables/tableofSNPs.csv > tables/new.csv
sed -E 's/([^,].*),([^,].*),([^,].*)/"success"/g' tables/new.csv | sort | uniq

sed 's/T/t/g' tables/new.csv | sed 's/A/T/g' | sed 's/t/A/g' 
