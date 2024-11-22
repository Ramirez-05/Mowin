FROM node:18

WORKDIR /app

COPY Angular/prueba-tecnica/package*.json ./

RUN npm install

COPY Angular/prueba-tecnica/ .

RUN npm run build

EXPOSE 4200

CMD ["npm", "start"]