FROM node:20-slim
# Create app directory
WORKDIR /usr/src/app/frontend
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
EXPOSE 3002
RUN npm install
#RUN npm install -g nodemon
COPY . .
CMD ["npm", "run", "dev"]