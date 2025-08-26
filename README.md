# Full-Stack Next.js + Express.js Application

A modern full-stack web application built with Next.js (frontend), Express.js (backend), TypeScript, Tailwind CSS, and Docker support.

## 🚀 Features

- **Frontend**: Next.js 14+ with App Router, TypeScript, and Tailwind CSS
- **Backend**: Express.js with TypeScript, CORS, security middleware
- **Styling**: Tailwind CSS with responsive design
- **Type Safety**: Full TypeScript support across the stack
- **Docker**: Multi-stage Docker builds and Docker Compose setup
- **Development**: Hot reloading for both frontend and backend
- **Production**: Optimized builds with security best practices

## 📋 Prerequisites

- Node.js 18+ and npm
- Docker and Docker Compose (optional)
- Git

## 🛠️ Installation

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install all dependencies**
   ```bash
   npm run install:all
   ```

3. **Start development servers**
   ```bash
   npm run dev
   ```

   This will start:
   - Frontend on http://localhost:3000
   - Backend on http://localhost:5000

### Option 2: Docker Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Start with Docker Compose**
   ```bash
   npm run docker:up:build
   ```

   This will start both services in containers with auto-reload.

## 📁 Project Structure

```
├── frontend/                 # Next.js application
│   ├── src/
│   │   └── app/
│   │       └── page.tsx     # Main page with API integration
│   ├── package.json
│   ├── Dockerfile
│   ├── next.config.js
│   └── tailwind.config.js
├── backend/                  # Express.js application
│   ├── src/
│   │   ├── app.ts           # Express app configuration
│   │   └── server.ts        # Server entry point
│   ├── package.json
│   ├── Dockerfile
│   ├── tsconfig.json
│   └── .env
├── docker-compose.yml        # Production Docker setup
├── docker-compose.dev.yml    # Development Docker override
└── package.json             # Root package.json with scripts
```

## 🔧 Available Scripts

### Root Level Scripts

```bash
# Development
npm run dev                   # Start both frontend and backend
npm run dev:frontend         # Start only frontend
npm run dev:backend          # Start only backend

# Production Build
npm run build                # Build both applications
npm run build:frontend       # Build only frontend
npm run build:backend        # Build only backend

# Production Start
npm run start                # Start both applications (after build)

# Docker Commands
npm run docker:build         # Build Docker images
npm run docker:up            # Start containers
npm run docker:up:build      # Build and start containers
npm run docker:down          # Stop containers
npm run docker:dev           # Start development containers
npm run docker:logs          # View container logs

# Maintenance
npm run clean                # Clean all build artifacts
npm run install:all          # Install all dependencies
```

## 🌐 API Endpoints

The backend provides the following REST API endpoints:

- `GET /health` - Health check endpoint
- `GET /api/hello` - Simple hello message
- `GET /api/users` - Get all users
- `POST /api/users` - Create a new user

### Example API Usage

```javascript
// Get users
const users = await fetch('http://localhost:5000/api/users');

// Create user
const newUser = await fetch('http://localhost:5000/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John Doe', email: 'john@example.com' })
});
```

## 🔒 Environment Variables

### Backend (.env)
```env
PORT=5000
NODE_ENV=development
FRONTEND_URL=http://localhost:3000
```

### Frontend
```env
NEXT_PUBLIC_API_URL=http://localhost:5000/api
```

## 🐳 Docker Setup

### Development with Docker

```bash
# Start development environment
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

# Or use the npm script
npm run docker:dev
```

### Production with Docker

```bash
# Build and start production containers
docker-compose up --build

# Or use npm scripts
npm run docker:up:build
```

## 🚦 Health Checks

Both services include health check endpoints:

- Frontend: http://localhost:3000
- Backend: http://localhost:5000/health

## 🛡️ Security Features

- **Helmet**: Security headers
- **CORS**: Cross-origin resource sharing configuration
- **Input Validation**: Request body validation
- **Error Handling**: Centralized error handling
- **Non-root Docker Users**: Security-focused container setup

## 📱 Frontend Features

- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **API Integration**: Real-time data fetching and submission
- **Loading States**: User-friendly loading indicators
- **Error Handling**: Graceful error handling with user feedback
- **Modern UI**: Clean, professional interface

## 🔧 Development Tips

1. **Hot Reloading**: Both frontend and backend support hot reloading
2. **TypeScript**: Full type safety across the stack
3. **Linting**: ESLint configuration for code quality
4. **Docker Development**: Use Docker for consistent environments

## 📊 Monitoring

- Backend includes request logging with Morgan
- Health check endpoints for monitoring
- Docker health checks configured

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the ISC License.

## 🆘 Troubleshooting

### Common Issues

1. **Port conflicts**: Make sure ports 3000 and 5000 are available
2. **Docker issues**: Ensure Docker is running and up to date
3. **API connection**: Check that backend is running before starting frontend
4. **Environment variables**: Verify all required environment variables are set

### Getting Help

If you encounter issues:

1. Check the logs: `npm run docker:logs` or check individual service logs
2. Verify environment variables are properly set
3. Ensure all dependencies are installed: `npm run install:all`
4. Try cleaning and rebuilding: `npm run clean && npm run build`

---

Built with ❤️ using Next.js, Express.js, TypeScript, and Docker.