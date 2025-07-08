FROM apache/superset

ENV SUPERSET_ENV=production
ENV SUPERSET_SECRET_KEY=clave_ultra_secreta_superlarga_12345678!@#

COPY superset_config.py /app/pythonpath/superset_config.py

CMD superset db upgrade && \
    superset fab create-admin \
        --username admin \
        --firstname Superset \
        --lastname Admin \
        --email admin@superset.com \
        --password admin && \
    superset init && \
    superset run -h 0.0.0.0 -p 8088
