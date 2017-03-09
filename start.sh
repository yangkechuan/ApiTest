#!/bin/bash

APP_PATH=$(cd `dirname $0`; pwd)

cd $APP_PATH

py.test > apiTest.log  --html=report.html --self-contained-html


echo "run time: `date '+%Y-%m-%d %H:%M:%S'`" >> run.log

echo "\n" >> run.log

cat apiTest.log >> run.log

echo "\n \n" >> run.log



python checkError.py;
