#!/bin/zsh

for user in lingfeng gaosa zhenchang xuejiao chunyang lijing prakash
do
	cp $user-to.txt /var/www/html/stackoverflow-annotator/${user}.automatic_tags 
done 

cd /var/www/html/stackoverflow-annotator/
for user in lingfeng gaosa zhenchang xuejiao chunyang lijing prakash
do
	touch ${user}.annotation.log
	touch ${user}.annotation.tags
	chmod 777 ${user}.annotation.log
	chmod 777 ${user}.annotation.tags
done 
