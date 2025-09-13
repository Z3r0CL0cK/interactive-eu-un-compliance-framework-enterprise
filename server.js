const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 8080;

// Security middleware
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"]
    }
  }
}));

app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000']
}));

app.use(express.json({ limit: '10mb' }));
app.use(express.static('site')); // Serve MkDocs built site

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: process.env.VERSION || 'unknown',
    compliance: {
      gdpr: 'compliant',
      euAiAct: 'mapped',
      nis2: 'configured'
    }
  });
});

// API endpoints for compliance data
app.get('/api/compliance/status', (req, res) => {
  // This would typically read from compliance.yaml
  res.json({
    status: 'configured',
    frameworks: ['EU-AI-Act', 'GDPR', 'NIS2', 'CRA'],
    lastUpdated: '2025-09-13'
  });
});

// Serve docs at root
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/site/index.html');
});

app.listen(port, '0.0.0.0', () => {
  console.log(`🚀 Compliance server running on port ${port}`);
  console.log(`📋 Documentation available at http://localhost:${port}`);
  console.log(`🔒 Security headers enabled`);
  console.log(`✅ Health check at http://localhost:${port}/health`);
});