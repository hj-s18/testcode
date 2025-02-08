# testcode

### docker 설치

```bash
sudo yum install docker -y
systemctl start docker
systemctl enable docker
sudo usermod -aG docker $USER
docker --version
```

### docker 설치 확인

```bash
[ec2-user@private-ip pwd]$ docker --version
Docker version 25.0.6, build 32b99dd

[ec2-user@private-ip pwd]$ docker version
Client:
 Version:           25.0.6
 API version:       1.44
 Go version:        go1.22.7
 Git commit:        32b99dd
 Built:             Tue Dec  3 05:03:06 2024
 OS/Arch:           linux/amd64
 Context:           default

Server:
 Engine:
  Version:          25.0.6
  API version:      1.44 (minimum version 1.24)
  Go version:       go1.22.7
  Git commit:       b08a51f
  Built:            Tue Dec  3 05:03:35 2024
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.7.25
  GitCommit:        bcc810d6b9066471b0b6fa75f557a15a1cbf31bb
 runc:
  Version:          1.2.4
  GitCommit:        6c52b3fc541fb26fe8c374d5f58112a0a5dbda66
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

### docker-compose 설치

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### docker-compose 설치 확인

```bash
[ec2-user@private-ip pwd]$ docker-compose --version
docker-compose version 1.29.2, build 5becea4c

[ec2-user@private-ip pwd]$ docker-compose version
docker-compose version 1.29.2, build 5becea4c
docker-py version: 5.0.0
CPython version: 3.7.10
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

### docker-compose로 이미지 빌드, 컨테이너 run

```bash
docker-compose build
docker-compose up -d

# 컨테이너 삭제 (이미지는 남아있음)
docker-compose down
```
