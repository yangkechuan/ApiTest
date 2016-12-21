#!/bin/bash

APP_PATH=$(cd `dirname $0`; pwd)

cd $APP_PATH

py.test3 > apiTest.log  --html=report.html --self-contained-html;
python3 checkError.py;
