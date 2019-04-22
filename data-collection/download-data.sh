#!/bin/bash

wget http://www.zubiaga.org/datasets/hurricane-sandy-tweets/hurricane-sandy-tweets.tar.bz2 
mv hurricane-sandy-tweets.tar.bz2 ../dataset/.
tar -vxjf ../dataset/hurricane-sandy-tweets.tar.bz2