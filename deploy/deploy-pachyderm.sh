#!/bin/bash

STORAGE_SIZE=10
BUCKET_NAME=pachyderm-pycon

pachctl deploy google ${BUCKET_NAME} ${STORAGE_SIZE} --dynamic-etcd-nodes=1
