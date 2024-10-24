#!/usr/bin/bash


# Description: This script is cheking the size of any you want file in Linux...
# ... and prints, is this size 'ok' [ -le 1024 bytes ] or no - FAIL 


size=$(stat --format=%s ${1} 2> /dev/null)      # '2>' sending the 'stat' error
declare -i fail                                 #+ output from cmd line to null
fail=1024                                       #+ if ${1} not specified


if [ -z ${1} ]; then
       echo "Error! Put the path/to/file you want check" && exit
elif [ ${size} -le ${fail} ]; then 
	echo "OK"
else 
	echo "FAIL"
fi




# С помощью exit {was used like analog /dev/null} добился отсутствия вывода ошибки
# ожидания унарного оператора в строке elif, если не ввести переменную, так как
# не нашел способ записи в нулл для функций if, elif etc. но при этом если ввести
# переменную не полностью, (путь до файла или файл которого не существует) она
# всеравно выводится.
# В соответствии с ДЗ скрипт свои функции выполняет, это лишь мое желание.
