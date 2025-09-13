const http = require('http');

// Simple health check for Docker
http.get('http://localhost:8080/health', (res) => {
  if (res.statusCode === 200) {
    process.exit(0);
  } else {
    process.exit(1);
  }
}).on('error', () => {
  process.exit(1);
});