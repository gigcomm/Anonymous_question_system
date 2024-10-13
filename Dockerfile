FROM ubuntu:latest
LABEL authors="iguly"

ENTRYPOINT ["top", "-b"]