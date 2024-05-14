FROM python:3.7

WORKDIR /webapp
COPY . /webapp

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable
    
# Install ChromeDriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.207/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN cp chromedriver-linux64/chromedriver /usr/local/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set up environment variables for Chrome and ChromeDriver
ENV CHROMIUM_PATH=/usr/bin/google-chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

# Ensure chromedriver is in PATH
ENV PATH=$PATH:/usr/local/bin

CMD ["sh"]
