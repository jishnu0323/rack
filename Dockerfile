FROM openjdk:17-jdk-slim

RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install gTTS qrcode[pil]

COPY target/RackSystemApplication.jar /app.jar
COPY scripts/generate_audio_qr.py /scripts/

WORKDIR /scripts
RUN python3 generate_audio_qr.py

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]