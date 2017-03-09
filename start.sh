#!/bin/bash

APP_PATH=$(cd `dirname $0`; pwd)

cd $APP_PATH

py.test > apiTest.log  --html=report.html --self-contained-html

echo "run time: `date '+%Y-%m-%d %H:%M:%S'` \n" >> run.log

cat apitest.log >> run.log

echo "\n\n" >> run.log


python3 checkError.py;
