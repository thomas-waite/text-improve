# TextGen

A web app that will auto-generate a paragraph of text from a short supplied sentence start. 

## How it works
1. Web app - written in React, runs on the client. This has an input text box in which a user can place a sentence start. On pressing 'Generate' it sends the text to the backend Flask Python server
2. Flask server - has a `/predict` endpoint that accepts `POST` requests. Uses the NLP model to run inference on the text and generate the remainder of the paragraph
3. Model - based on simple high level Huggingface `pipeline` models

## Docker
The `app`, `model` and `server` have been dockerized for use of deployment. AWS ECS + ECR used for deploying.
