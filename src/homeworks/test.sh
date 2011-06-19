#!/bin/bash
for dir in *;do
    if test -d $dir ;then
	echo "entering $dir"
	cd $dir
	cp ps12.py ../ 
	cd ../
	python -m timeit -n 50 "import test11" "test11.main()"
	rm ps12.py
	rm ps12.pyc
    fi
done
