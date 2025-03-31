FROM node:18 AS frontend-builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY ./ ./
RUN npm run build

FROM nginx:alpine AS frontend-runner
COPY --from=frontend-builder /app/public /usr/share/nginx/html
