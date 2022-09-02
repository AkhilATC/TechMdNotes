## Docker
Docker provides a single command that will clean up any resources —
images, containers, volumes, and networks — that are dangling (not tagged or associated with a container):

>docker system prune

To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:

>docker system prune -a

list :
> docker images -f dangling=true

> docker images -a # list all images

> docker images -a |  grep "pattern" # for specfic pattern
Remove :
> docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi # for remove 
