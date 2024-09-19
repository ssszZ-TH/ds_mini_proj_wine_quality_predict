## เเบบ dev ไม่มีการ run build ใช้ตอนพัฒณา app
FROM node:20-alpine

WORKDIR /frontend

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]

# เเบบ optimize ไม่เหมาะกับการ develop
# Stage 1: Build the application
# FROM node:20-alpine AS builder

# WORKDIR /frontend

# COPY package*.json ./

# # RUN ls -al /frontend

# RUN npm install

# COPY . .

# RUN npm run build

# # Stage 2: Serve the application
# FROM node:20-alpine

# WORKDIR /frontend

# COPY --from=builder /frontend/build ./build

# RUN npm install -g serve

# CMD ["serve", "-s", "build"]