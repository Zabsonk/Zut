#!/bin/bash
#SO IS1 212B LAB07
#Kacper Zabiński
#zk51162@zut.edu.pl
case $1 in
"-p");;
"-u");;
*)
echo "podaj albo -p albo -u"
exit 0
esac

if [ $1 == "-p" ];then
	for i in $(ls /proc | grep -E "[[:digit:]]" | sort -n)
	do
		((cat /proc/$i/stat | cut -d ' ' -f1,4 )2>/dev/null) | tr "\n" " " &&
		((id $(cat /proc/$i/status | head -n 8 | tail -1 | tr ":" " " | tr "\t" " " | cut -d ' ' -f3)| tr "=" " " | cut -d ' ' -f2)2>/dev/null) | tr "\n" " "&&
		((cat /proc/$i/stat | cut -d ' ' -f2)2>/dev/null) | tr "(" " "| tr ")" " "
	done
elif [ $1 == "-u" ];then

	for i in $(ls /proc | grep -E "[[:digit:]]" | sort -n)
	do
		if [ -f "/proc/$i/status" ];then

			id1=$(cat /proc/$i/status | head -n 8 | tail -1 | tr ":" " " | tr "\t" " " | cut -d ' ' -f3)
    		id2=$(id -u)

			if [ $id2 == $id1 ] ;then
				((cat /proc/$i/stat | cut -d ' ' -f1 )2>/dev/null) | tr "\n" " " &&
				((cat /proc/$i/stat | cut -d ' ' -f2 )2>/dev/null) | tr "(" " " | tr ")" " " | tr "\n" " " &&
				readlink /proc/$i/cwd | tr "\n" " "
				printf "\n"
			fi
		fi 
	done

fi

