FROM apache/superset

ENV SUPERSET_ENV=production
ENV SUPERSET_SECRET_KEY=una_clave_ultra_secreta_123456!@#

COPY superset_config.py /app/pythonpath/superset_config.py

EXPOSE 8088

CMD ["bash", "-c", "\
  superset db upgrade && \
  superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin && \
  superset load_examples && \
  superset init && \
  superset run -h 0.0.0.0 -p 8088"]