# DOCKER

Docker is a containerization technology that allows you to run applications in a lightweight container.

We can create for example containers that run a web server, a database, a command line tool, or any other application.

It allow us to replicate the same setup in different environments.

A container contains all the things that we need to run our application.

# Docker Images

-   Like blueprints for containers

    -   Runtime environment
    -   Application code
    -   Any dependencies
    -   Extra configuration
    -   Commands to run

-   Images are read-only and can be shared between users

# Docker Containers [Isolated Process]

-   Running instance of an image
    -   Runs our application

[Image] => [Container]

# How an image is made

-   First Layer:

    -   Parent Image (OS & sometimes the runtime environment)

-   Source Code
-   Dependencies

To find parent images we can go to [dockerhub](https://hub.docker.com/).

To download an image we can use the [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/) command.

To create a image of our own we have to create a Dockerfile.

The differents line of our DockerFile are the different layers of our image.

Inside the docker file:

    -   FROM: Parent image
    -   WORKDIR: Directory where we want to run our application
    -   COPY: Copy files from the parent image
    -   RUN: Commands to run before the container starts
    -   EXPOSE: Expose port for the container
    -   CMD: Commands to run after the container starts

With FROM we can specify another images as the parent of ours.

-   FROM alpine:3.6

With copy, we can copy files from our computer to the container.

-   COPY relativePathMachine relativePathContainer
    COPY ./src/ ./src/

El punto simbolize el directorio en el que estamos actualmente escribiendo la dockerfile.

-   RUN echo "Hello World"
    RUN npm install

We run commands that we need to install dependencies for example.

-   WORKDIR /src

We have to specify a directory where we want to run our application. If we dont specify it, the default directory is the root of the image. So if we copy the code into an "app" folder and the next instruction on the dockerFile is to run npm install, it will run the command in the root directory

If we specify a workdir, in the next instruction like COPY we have to be aware the the instruction workdir affects our relativePath. Because our relative path will start in our workdir instead of the root

-   CMD ["node", "index.js"]

We can specify commands to run after the container starts.

We write the commands in a array, because we can specify multiple commands.

-   EXPOSE 3000

If we want access to our application from outside, we have to specify the port that the container will expose, but also we have to specify the port that our computer will connect to that container. This is done when we run the command `docker run -d -p 3000:3000` or in the docker desktop when we run the container.

# COMMANDS

    -   docker build -t <imageName> .
        -   Builds the image
        -   -t: name of the image
        -   .: current directory

    -   docker run [flags] [imagename]
        -   Runs the image and creates a container
        -   docker run -d -p 3000:3000 <imageName>

    -   docker images
        -   List all images

    -   docker ps
        -   List all containers currently running

    -   docker ps -a
        -   List all containers running or not

    -   docker start <containerId>
        -   Start an existing container

    -   docker stop <containerId>
        -   Stops a container

    -   docker rm <containerId>
        -   Removes a container

# DOCKER IGNORE

We can tell the docker engine to ignore certain files or directories.

We do this creating a file called .dockerignore in the root of our image.

And that files has the same syntax as the .gitignore file.
