1-6. DONE < br />
7. It worked, but i had to some huge steps towards it:< br />
1) I had to add 127.0.0.1 redis in my /etc/hosts file< br />
2) i had to install redis-server and launch it< br />
3) i had to create a directory my< br />app/logs< br />
8)STATES := app tests - is a variable with dynamically assigned values. REPO := docker repo name..PHONY - is used to create a virtual target of makefile because STATE isn't a physical file. 
 $(STATES): - use of app or tests variables. docker build - creates new docker container. $(@) - variables from STATE(app, tests). run - execute commands. docker-prune - remove all the previous dockers.< br />
9. Done!< br />
![1](./img/1.PNG)< br />
10-12. Done!< br />
![2](./img/2.PNG)< br />
13. Networks: public, secret. The names are as they are, it's about security< br />
14-18. Done! DockerHub [link](https://cloud.docker.com/repository/docker/roffymonsta/lab< br />5)!< br />
19. Makefile is better when we'd like to choose an option, and the docker-compose is better in automatic work with a lot of commands. This is a small project, so Makefile is better and more understandable in this case.< br />
20. After a long time i made it. Installing requests and django in pipenv did the trick for me. Also you have to change allowed hosts and be careful with networks. Always clean docker with Makefile in lab5 after every try.< br />
![3](./img/3.PNG)< br />
