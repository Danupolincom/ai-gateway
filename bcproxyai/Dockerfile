FROM ghcr.io/berriai/litellm:main-latest
COPY config.yaml /app/config.yaml
EXPOSE 8080
CMD ["--config","/app/config.yaml","--port","8080","--host","0.0.0.0"]
