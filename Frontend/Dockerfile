FROM node:16.15 as build

COPY . /.
RUN yarn install
RUN yarn build

FROM nginx:stable

RUN mkdir /www
COPY --from=build dist/ www/

EXPOSE 80
