1-6. DONE
7. It worked, but i had to some huge steps towards it:
1) I had to add 127.0.0.1 redis in my /etc/hosts file
2) i had to install redis-server and launch it
3) i had to create a directory my_app/logs
8.STATES := app tests - is a variable with dynamically assigned values. REPO := docker repo name..PHONY - is used to create a virtual target of makefile because STATE isn't a physical file. 
 $(STATES): - use of app or tests variables. docker build - creates new docker container. $(@) - variables from STATE(app, tests). run - execute commands. docker-prune - remove all the previous dockers. 
9. Done!
![1](./img/1.PNG)
10-12. Done!
![2](./img/2.PNG)
13. Networks: public, secret. The names are as they are, it's about security
14-18. Done! DockerHub [link](https://cloud.docker.com/repository/docker/roffymonsta/lab_5)!
19. Makefile is better when we'd like to choose an option, and the docker-compose is better in automatic work with a lot of commands. This is a small project, so Makefile is better and more understandable in this case.

