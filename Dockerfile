# syntax: docker/dockerfile:1
FROM node:18-alpine AS base

# Metadata for compliance (CRA requirements)
LABEL org.opencontainers.image.title="l-LCL-l Compliance Blueprint"
LABEL org.opencontainers.image.description="EU/UN Ethics & Compliance Framework"
LABEL org.opencontainers.image.vendor="statesflowwishes-sketch"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/statesflowwishes-sketch/l-LCL-l--Y3zYnC-CnYz3Y2m1l3--l-LCL-l"

# Build arguments for traceability
ARG BUILD_DATE
ARG VCS_REF  
ARG VERSION

LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.revision=${VCS_REF}
LABEL org.opencontainers.image.version=${VERSION}

# Security: Non-root user
RUN addgroup -g 1001 -S appuser && \
    adduser -S appuser -u 1001 -G appuser

WORKDIR /app

# Install Python for MkDocs
RUN apk add --no-cache python3 py3-pip

# Copy package files first (for better caching)
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production && \
    npm cache clean --force

# Install MkDocs and plugins
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=appuser:appuser . .

# Remove sensitive files that shouldn't be in container
RUN rm -f .env* && \
    rm -rf compliance/evidence/*.pdf && \
    rm -rf .git

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD [ "node", "healthcheck.js" ]

# Expose port
EXPOSE 8080

# Default command
CMD ["npm", "start"]

# Multi-stage build for docs
FROM base AS docs
USER root
RUN mkdocs build --strict
USER appuser
CMD ["python3", "-m", "http.server", "8080", "--directory", "site"]