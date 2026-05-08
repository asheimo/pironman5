FROM ubuntu:24.04

ARG VARIANT=base
ARG PIPOWER5=false
ARG INSTALLER_REF=main

RUN apt-get update && apt-get install -y curl sudo

RUN curl -fsSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/refs/heads/${INSTALLER_REF}/install_pironman5.sh -o /tmp/install.sh

RUN if [ "$PIPOWER5" = "true" ]; then \
        bash /tmp/install.sh --variant "$VARIANT" --container --pipower5; \
    else \
        bash /tmp/install.sh --variant "$VARIANT" --container; \
    fi

RUN rm /tmp/install.sh

COPY docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 34001
CMD ["/entrypoint.sh"]
