FROM node:20-slim as base
# Create app directory
WORKDIR /usr/src/app/backend
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
EXPOSE 3000

FROM base as production
ENV NODE_ENV=production
RUN npm ci
COPY . .
CMD ["node", "/bin/www"]

FROM base as dev
ENV NODE_ENV=development
RUN npm install -g nodemon 
RUN npm install
COPY . .
#Give the path of your endpoint
ENTRYPOINT ["nodemon", "/usr/src/app/bin/www"]  
CMD ["nodemon", "-L", "/bin/www"]