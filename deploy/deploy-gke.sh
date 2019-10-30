#!/bin/bash

CLUSTER_NAME=pachyderm-pycon
GCP_ZONE=europe-north1-a

gcloud config set compute/zone ${GCP_ZONE}
gcloud config set container/cluster ${CLUSTER_NAME}

MACHINE_TYPE=n1-standard-2

gcloud container clusters create ${CLUSTER_NAME} --scopes storage-rw --machine-type ${MACHINE_TYPE}

kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)

