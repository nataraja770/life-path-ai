# Stage 1: Build the React application
FROM node:18-alpine AS build

WORKDIR /app

# Copy package.json and install dependencies
# We copy package.json and package-lock.json separately
# to take advantage of Docker layer caching.
COPY package.json ./
# Since I cannot run npm install, I assume there is no lock file.
# In a real project, you would also copy package-lock.json or yarn.lock
RUN npm install

# Copy the rest of the application code
COPY . ./

# Build the application
RUN npm run build

# Stage 2: Serve the application using Nginx
FROM nginx:1.21-alpine

# Copy the built static files from the build stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy a custom Nginx configuration
# We will need to create this file next
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# The default command for Nginx is to start the server
CMD ["nginx", "-g", "daemon off;"]
