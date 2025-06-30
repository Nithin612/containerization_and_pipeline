FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Serve with nginx or simple node server in container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
