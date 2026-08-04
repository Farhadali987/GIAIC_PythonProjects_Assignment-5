# Deployment Guide

1.  **Environment Variables**: Ensure all `.env` variables (DATABASE_URL, CLERK_KEYS, LLM_KEYS, CLOUDINARY_URL) are configured on the production server.
2.  **Database**: Run migrations using `alembic upgrade head`.
3.  **Docker**: Use `docker-compose up -d --build` to launch the containers.
4.  **Frontend**: Deploy the web app to Vercel/Render using the production build.
5.  **Reverse Proxy**: Configure Nginx to serve the frontend and reverse-proxy to the backend API.
