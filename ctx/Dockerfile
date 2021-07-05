FROM ubuntu:groovy

ARG USER=deeply
ARG HOME=/home/$USER

RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qqy \
        neovim python3 python3-pip tmux tree

RUN useradd --create-home --shell=/bin/bash $USER
USER $USER
WORKDIR $HOME

RUN python3 -m pip install black pytest

COPY --chown=deeply nvim .config/nvim
COPY --chown=deeply tmux.conf .tmux.conf
COPY --chown=deeply toprc .config/procps/toprc

CMD ["tmux"]
