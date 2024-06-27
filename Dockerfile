FROM python

WORKDIR ./usr/autolearning
COPY . .
RUN mkdir /usr/autolearning/allure-results

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
RUN pip3 install -r requirements.txt
CMD ["pytest", "--alluredir=allure-results"]