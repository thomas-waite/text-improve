<p align="center"><img src="https://github.com/thomas-waite/text-improve/blob/master/webApp.png" width="650px"/></p>

**Deployed at: https://www.textgen.dev/**

[![Netlify Status](https://api.netlify.com/api/v1/badges/cede6557-06ec-49e7-9704-3ae62d49b440/deploy-status)](https://app.netlify.com/sites/inspiring-lumiere-e71e33/deploys)

# TextGen

A web app and backend server that uses NLP ML algorithms to auto-generate a paragraph of text from a short supplied sentence start.

## How it works

1. Web app - written in React, runs on the client. This has an input text box in which a user can place a sentence start. On pressing 'Generate' it sends the text to the backend Flask Python server
2. Flask server - has a `/predict` endpoint that accepts `POST` requests. Uses the NLP model to run inference on the text and generate the remainder of the paragraph
3. Model - based on simple high level Huggingface `pipeline` models

## Docker

The `app`, `model` and `server` have been dockerized for use of deployment. AWS ECS + ECR used for deploying.
