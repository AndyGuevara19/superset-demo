FROM apache/superset

ENV SUPERSET_ENV=production
ENV SUPERSET_SECRET_KEY=clave_ultra_secreta_superlarga_12345678!@#
ENV PYTHONPATH=/app/pythonpath

# Agrega esta línea para instalar flask-cors
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

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
