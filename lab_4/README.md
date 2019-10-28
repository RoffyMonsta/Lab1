1. Done
2. Done
![1](./img/1.PNG)
3. Done
![2](./img/2.PNG)
4. Done
5-6. Done
![3](./img/3.PNG)
[Docker HUB](https://cloud.docker.com/repository/registry-1.docker.io/roffymonsta/lab_4)

Видалення image: docker image rm roffymonsta/lab_4:django
7. DOne
![4](./img/4.PNG)
8.
docker build -f DockerFileSecond -t roffymonsta/lab_4:djangoMONITORING .
docker push roffymonsta/lab_4:djangoMONITORING
docker run -it --name=djangoMONITORING --rm --net=host roffymonsta/lab_4:djangoMONITORING
DONE
