FROM node:16.15 as build

COPY . /.
RUN yarn install
RUN yarn build

FROM nginx:stable

RUN mkdir /www
COPY --from=build dist/ www/
COPY --from=build private_pkey.pem /etc/nginx/private_pkey.pem
COPY --from=build out_cert.pem /etc/nginx/out_cert.pem

EXPOSE 80
