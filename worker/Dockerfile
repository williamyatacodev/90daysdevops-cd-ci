FROM node:23-alpine
LABEL author="williamyatacodev"

WORKDIR /usr/src/app

RUN npm install -g nodemon

# Copy package.json by project result
COPY package*.json ./

RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["node", "main.js"]
