# stat992_note
#Exercise
The table under `tables/tableofSNPs.csv ` is not formatted correctly: the numbers in the second column have commas in it.
### task
In order to fix the problem, I wrote a single line using sed to remove the commas betweens the digits in column "Minimum".
`sed -E 's/"([0-9]*),?([0-9]+),([0-9]+)"/\1\2\3/' tables/tableofSNPs.csv > tables/new.csv`

I also wrote a single line to check if I was doing correctly. If the screen prints a single "success", then it means I am right.
`sed -E 's/([^,].*),([^,].*),([^,].*)/"success"/g' tables/new.csv | sort | uniq`

### extra task
I changed all Ts to As and all As to Ts by 
`sed 's/T/t/g' tables/new.csv | sed 's/A/T/g' | sed 's/t/A/g' `

The `.csv` file with correct format will be `tables/new.csv`.

### binomial coefficient exercise
The binomial coefficient exercise .py file is scripts/binomial.py
