#!/bin/zsh

cd /var/www/html/stackoverflow-annotator/
for user in lingfeng gaosa zhenchang xuejiao chunyang lijing
do
	cd $user
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
	do
		touch ${user}${i}.annotation.log
		touch ${user}${i}.annotation.tags
		chmod 777 ${user}${i}.annotation.log
		chmod 777 ${user}${i}.annotation.tags
	done
	cd ..
done 
