# Requirements and instalation


## Requirements
### Hardware

This is not entirely requirement, but more os suggestion.
### CPU
At least mobile Intel core i5 gen 7 or corresponding AMD processor with 8 GB of RAM. Running nodes itself or data visualisation from sensors such as 2d lidar can be (and very often is handled) by Intel Atom processors or raspberry pi. For simulation there is no upper bound of computation power. Since this example aims on simulation i5 is advised.

### GPU
TL;DR Nvidia at least Pascal architecture and 2 GB of RAM. It will work with Intel integrated graphics and AMD graphics but simulations won't run as smoothly and data processing for point clouds will take much much longer.

Intel and AMD GPUs work... The biggest advantage can be taken from Nvidia GPUs. Personally I only happen to have experience with Intel and Nvidia cards and from that I can tell there is hudge gap between those two. Nvidia has a variety of computation libraries. On the other hand as time of writing this tutorial AMD doesn't. This is why Nvidia's CUDA cores became sort of standard in robotics. This tutorial have separate launch files for Linux with Nvidia drivers. Installation guide can be found later.

### Disc space
Docker will need roughly 8 GB of disc space. If you are willing to install it inside virtual machine make sure it can fit it. Same goes for installing linux natively. About 45 BG for should be sufficient for operating system.


# Installation
## Operating system
[Ubuntu](https://ubuntu.com/download) is the most supported platform by ROS and it is one of the easiest and most popular linux distribution. You can install it either as virtual machine or natively on your computer with dual boot alongside windows. The last option is to use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) it runs Linux inside Windows. After installing that you can use Docker with Linux. The only requirement for Windows is it has to be Windows 10. Author doesn't have any experience with Apple ecosystem thus can not suggest any working solution. For each option tutorials can be found here:

- [Ubuntu alongside windows with dual boot](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/).

- [Ubuntu as virtual machine with VirtualbBox](https://itsfoss.com/install-linux-in-virtualbox/).

- [Docker on Windows 10](https://jack-kawell.com/2019/09/11/setting-up-ros-in-windows-through-docker/). This is great tutorial Jack Kawell in which he explained how to set everything up. Since in the end we will focus on Ubuntu author won't cover in details installation process of docker on windows.

Running Ubuntu natively will give you best performance and is the only tested by author option to access Nvidia GPU inside docker. Option with virtual machine might end up being the least efficient but for people starting with linux it might be the best one. Especially they will have access to linux GUI. Installing Linux natively is by far the most risky approach and author is not suggesting it for beginners since they can easlly break boot partition of windows. 


## Docker

Since we are focusing on Ubuntu the following section will include commands that can be executed on Ubuntu and family distributions. Official docker installation guide can be found [here](https://docs.docker.com/engine/install/ubuntu/) and for docker-compose can be found [here](https://docs.docker.com/compose/install/).


Extracted commands from installation guide for docker are following:
```bash
sudo apt -y remove docker docker-engine docker.io containerd runc \
    && apt update \
    && apt install ca-certificates curl gnupg lsb-release \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt update \
    && apt install -y docker-ce docker-ce-cli containerd.io
```

To check if installation succeed run
``` bash
sudo docker run hello-world
```

For docker-compose:
``` bash
sudo apt update \
    && apt install -t python3 python3-dev python3-pip \
    && pip3 install docker-compose
```

To test if installation was successful run
``` bash
sudo docker-compose -v
```

In order to no longer being obligated to use `sudo` command before running docker follow [this instruction](https://docs.docker.com/engine/install/linux-postinstall/) or paste following commands.
``` bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker 
```
To test if changes applied run
``` bash
docker run hello-world
```
Notice you no longer need `sudo` to run `docker` and `docker-compose` commands.


## Docker with Nvidia
Installation of Nvidia Docker is not necessary and is described in [official guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) by Nvidia.

## Final note

That's it for the installation process. Rest will be "docker magic". Everything you need to install will come inside docker and just work.