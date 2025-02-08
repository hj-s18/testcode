# testcode

### docker 설치

```bash
sudo yum install docker -y
systemctl start docker
systemctl enable docker
sudo usermod -aG docker $USER
docker --version
```

### docker-compose 설치

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### docker-compose로 이미지 빌드, 컨테이너 run

```bash
docker-compose build
docker-compose up -d

# 컨테이너 삭제 (이미지는 남아있음)
docker-compose down
```
