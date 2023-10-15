# Comprehensive Push Docker 容器

这个Docker容器旨在通过HTTP请求向企业微信机器人发送消息。它监听9000端口，并期望设置特定的环境变量以进行配置。

## 开始

要开始使用这个Docker容器，请按照以下步骤操作：

### 先决条件

- 在您的系统上安装 [Docker](https://www.docker.com/get-started) 和 [Docker Compose](https://docs.docker.com/compose/install/)。

### 拉取Docker镜像

您可以使用以下命令从Docker Hub拉取容器的最新版本：

```bash
docker pull jerryliang/comprehensive_push:latest

### 使用Docker Compose运行容器
创建一个名为docker-compose.yml的文件，并将以下内容添加到文件中。请用您的实际配置值替换 <your_value>。
```bash
version: '3'
services:
  comprehensive_push:
    image: jerryliang/comprehensive_push:latest
    ports:
      - "9000:9000"
    environment:
      - wecom_aid=<your_value>
      - wxqy_secret=<your_value>
      - wxqy_id=<your_value>

### 运行容器
在运行容器之前，您需要设置所需的环境变量。这些变量用于配置企业微信集成。请用您的实际配置值替换 your_value。
```bash
docker run -d -p 9000:9000 \
    -e wecom_aid=your_value \
    -e wxqy_secret=your_value \
    -e wxqy_id=your_value \
    jerryliang/comprehensive_push:latest

- -d：在后台运行容器。
- -p 9000:9000：将容器内部的9000端口映射到您主机上的9000端口。
- -e wecom_aid=your_value：设置您的WeCom（企业微信） wecom_aid。
- -e wxqy_secret=your_value：设置您的WeCom wxqy_secret。
- -e wxqy_id=your_value：设置您的WeCom wxqy_id。

### 发送消息
您可以通过向以下URL发出GET请求来向企业微信机器人发送消息：
```bash
http://localhost:9000/wechat?name=your_name&message=your_message

- name：与消息相关的名称。
- message：您想要发送的消息。

容器将处理请求并将消息发送到配置的企业微信机器人。