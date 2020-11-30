# Server

This is a basic Flask Python server that servers inference on ML models.

The `model` and `server` package both have `Dockerfile`s and are distributed as Docker images. To build these images, go to the root and run `make docker`.

## How to deploy

1. Go to the root
2. Run `make deploy` - build and tag all required docker images
3. Run `make push_docker` - push the built `model` and `server` images to the AWS ECR `text_improve` registry. Note before doing this, will likely need to authenticate with AWS
4. Run a new task in the `first-test` cluster with these containers. This cluster uses ECS and the Fargate service.

Note, the AWS aspects of this currently have to be done manually. TODO: add terraform to auto setup
