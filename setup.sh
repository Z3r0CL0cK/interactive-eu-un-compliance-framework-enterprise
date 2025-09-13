#!/bin/bash
# Quick setup script for the compliance framework

set -euo pipefail

echo "🚀 Setting up Compliance Framework with Token Integration..."

# Check prerequisites
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first."
    exit 1
fi

# Create .env from template if not exists
if [ ! -f .env ]; then
    echo "📋 Creating .env from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your actual tokens!"
    echo "   - GitHub tokens are pre-configured"
    echo "   - Docker token is pre-configured"
else
    echo "✅ .env file already exists"
fi

# Install Node.js dependencies
if [ -f package.json ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

# Install Python dependencies for MkDocs
if [ -f requirements.txt ]; then
    echo "🐍 Installing Python dependencies..."
    if command -v python3 &> /dev/null; then
        python3 -m pip install -r requirements.txt
    else
        echo "⚠️  Python3 not found, skipping pip install"
    fi
fi

# Build documentation
echo "📚 Building documentation..."
if command -v mkdocs &> /dev/null; then
    mkdocs build --strict
else
    echo "⚠️  MkDocs not found, skipping docs build"
fi

# Docker setup
echo "🐳 Building Docker images..."
docker compose build

echo ""
echo "✅ Setup complete! Available commands:"
echo ""
echo "🌐 Development:"
echo "   npm run dev              # Start development server"
echo "   mkdocs serve            # Serve docs locally"
echo "   docker compose up       # Run with Docker"
echo ""
echo "🔧 Testing & Building:"
echo "   npm test                # Run tests"
echo "   npm run build           # Build for production"
echo "   docker compose up -d    # Run in background"
echo ""
echo "🔐 Security & Compliance:"
echo "   npm run compliance:check # Validate compliance"
echo "   docker compose logs     # Check container logs"
echo ""
echo "🚀 GitHub Actions are ready to:"
echo "   ✅ Build & deploy docs automatically"
echo "   ✅ Build & push Docker images"
echo "   ✅ Sync across your repos (personal/org/enterprise)"
echo "   ✅ Run security & compliance scans"
echo ""
echo "🔗 Quick URLs (after running):"
echo "   📋 Documentation: http://localhost:8080"
echo "   🏥 Health Check:  http://localhost:8080/health"
echo "   📊 API Status:    http://localhost:8080/api/compliance/status"
echo ""
echo "⚠️  Don't forget to:"
echo "   1. Edit .env with your actual values"
echo "   2. Set up GitHub repository secrets"
echo "   3. Enable GitHub Pages for documentation"