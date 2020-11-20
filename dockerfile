FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu16.04

LABEL maintainer="StepNeverStop(Keavnn)"\
      github="https://github.com/StepNeverStop/RLs"\
      description="Docker image for runing RLs."\
      rls_version="0.0.1"\
      email="keavnn.wjs@gmail.com"

ENV LANG C.UTF-8

# install apt packages
RUN mv /etc/apt/sources.list.d/cuda.list /etc/apt/sources.list.d/nvidia-ml.list /tmp && \
    apt-get upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get update --fix-missing && \
    apt-get install -y apt-file apt-utils nano --no-install-recommends wget bzip2 ca-certificates curl git openssh-server \
    libglib2.0-dev libsm6 libxrender1 libxext6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /var/run/sshd && \
    echo "root:1234" | chpasswd && \
    sed -i 's/prohibit-password/yes/g' /etc/ssh/sshd_config && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\srequired\spam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# install miniconda3 and change source of pip
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda init bash && \
    conda update conda && \
    conda install -y conda-build && \
    /opt/conda/bin/conda build purge-all

# install my own conda environment
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda create -n rls python=3.8 && \
    conda activate rls && \
    echo -e "\033[4;41;32m conda activate rls successed. \033[0m" && \
    cd ~ && git clone https://github.com/StepNeverStop/RLs.git && cd RLs && \
    pip install -e . && \
    /opt/conda/bin/conda build purge-all && \
    rm -rf ~/.cache/pip/* && \
    python run.py --gym -a dqn -t 2000 -s 100 --prefill-steps 1000 --no-save && \
    echo -e "\033[4;41;32m run rls successed. \033[0m"

# 22:ssh 6006:tensorboard 8888:jupyter lab
EXPOSE 22 6006 8888

ENTRYPOINT ["/usr/sbin/sshd","-D"]