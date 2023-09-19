FROM node:20-slim
# Create app directory
WORKDIR /usr/src/app/backend
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
EXPOSE 3000
RUN npm install
RUN npm install -g nodemon
COPY . .
CMD ["npm", "run", "start:dev"]