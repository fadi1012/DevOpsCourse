#! /bin/bash

echo $NAME
touch myFile.txt && chmod 775 myFile.txt
echo $NAME > myFile.txt

# part 2
cat myFile.txt

# part 3

df -h

# part 4
mv myFile.txt world_of_games/