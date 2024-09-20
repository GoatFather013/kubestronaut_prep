# Use the Alpine base image
FROM alpine:3.20.3

CMD ["/bin/sh"]
ARG BIN_NAME=vault
ARG NAME=vault
ARG PRODUCT_VERSION=1.17.5
ARG PRODUCT_REVISION=4d0c53e84094b8017d32b6e5b7f8142035c8837f
ARG TARGETOS=linux TARGETARCH=amd64

ENV NAME=vault
ENV VERSION=

RUN |6 BIN_NAME=vault NAME=vault PRODUCT_VERSION=1.17.5 PRODUCT_REVISION=4d0c53e84094b8017d32b6e5b7f8142035c8837f TARGETOS=linux TARGETARCH=amd64 /bin/sh -c addgroup ${NAME} && adduser -S -G ${NAME} ${NAME}
RUN |6 BIN_NAME=vault NAME=vault PRODUCT_VERSION=1.17.5 PRODUCT_REVISION=4d0c53e84094b8017d32b6e5b7f8142035c8837f TARGETOS=linux TARGETARCH=amd64 /bin/sh -c apk add --no-cache libcap su-exec dumb-init tzdata
RUN |6 BIN_NAME=vault NAME=vault PRODUCT_VERSION=1.17.5 PRODUCT_REVISION=4d0c53e84094b8017d32b6e5b7f8142035c8837f TARGETOS=linux TARGETARCH=amd64 /bin/sh -c mkdir -p /vault/logs && mkdir -p /vault/file && mkdir -p /vault/config && chown -R ${NAME}:${NAME} /vault

VOLUME [/vault/logs]
VOLUME [/vault/file]


# Install OpenSSL 3.3.2-r1
RUN apk add --no-cache openssl=3.3.2-r1


COPY vault.bunkerbouwers.nl/cert.pem /etc/vault/ssl/cert.pem
COPY vault.bunkerbouwers.nl/key.pem /etc/vault/ssl/key.pem
RUN chmod 644 /etc/vault/ssl/cert.pem \
    && chmod 644 /etc/vault/ssl/key.pem