#!/bin/bash
sed -E 's/"([0-9]*),?([0-9]+),([0-9]+)"/\1\2\3/' tables/tableofSNPs.csv > tables/new.csv 
