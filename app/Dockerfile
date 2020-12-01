FROM node:14.8.0-alpine

WORKDIR /usr/src/app
COPY . .
RUN yarn install && yarn build && rm -rf node_modules && yarn install --production && yarn cache clean
CMD ["yarn", "start"]




