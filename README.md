##End to End Machine Learning Project


## Run from terminal

docker build -t mlproject.azurecr.io/mltest:latest

docker login mlproject.azurecr.io

docker push mlproject.azurecr.io/mltest:latest
