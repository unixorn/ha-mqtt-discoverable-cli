FROM python:slim

ARG application_version
LABEL maintainer="Joe Block <jpb@unixorn.net>"
LABEL description="ha-mqtt-discoverable-cli utility image"
LABEL version=${application_version}

RUN python -m pip install --upgrade ha-mqtt-discoverable-cli && \
    pip cache purge

USER nobody

CMD ["bash", "-l"]
