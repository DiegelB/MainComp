#!/bin/bash

VAR=test
num=10
echo $VAR
echo $num

echo "hello world"

echo "what is your name"

read name

echo "you said $name"


echo "hello world" >> test.txt
echo "Please input something about yourself"
read story
echo $story >> test.txt

compNum=13
echo "guess my number 1=20"
read humanNum

if [ $humanNum = $compNum ]
then
	echo "you win!"
else
	echo "you lose!"
fi

for dodo in fuck face bitch ass pussy werido dumb-dumb
do
echo "yous a $dodo"
done

for arg in $@
do
echo "Thanks for the fish $arg"
done
