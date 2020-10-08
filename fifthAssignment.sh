#! /bin/bash

echo $NAME
echo "creating file"
touch myFile.txt && chmod 775 myFile.txt
echo "writing content into newly created file"
echo $NAME > myFile.txt

# part 2
echo "printing newly created file content"
cat myFile.txt

# part 3
echo "printing out disk free space"
df -h

# part 4
echo "moving file to world_of_games dir"
mv myFile.txt world_of_games/