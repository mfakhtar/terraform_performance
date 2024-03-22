#!/bin/bash

ARGUMENT=$1

cd resource
bash resource.sh $ARGUMENT

cd ../count
bash resource.sh $ARGUMENT

cd ../for_each
bash resource.sh $ARGUMENT
