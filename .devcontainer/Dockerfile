FROM mcr.microsoft.com/devcontainers/base:jammy

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \ 
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev

# Python and poetry installation
USER $USER
ARG HOME="/home/$USER"
ARG PYTHON_VERSION=3.13
ARG NODE_MAJOR=20
# ARG NODE_VERSION=22.11.0

ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

RUN echo "installing pyenv..." \
    && curl https://pyenv.run | bash \
    && echo "installing python" \
    && pyenv install ${PYTHON_VERSION} \
    && echo "set python version" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "install" \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

RUN echo "install node.js"
RUN sudo apt-get update \
    && sudo apt-get install -y gnupg \
    && sudo mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
RUN sudo apt-get update && sudo apt-get install nodejs -y
# # get install script and pass it to execute: 
# RUN curl -sL https://deb.nodesource.com/setup_20.x | bash
# # and install node 
# RUN apt install nodejs
# RUN node --version
# RUN npm --version
