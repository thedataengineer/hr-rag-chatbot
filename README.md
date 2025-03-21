# HR RAG Chatbot

## Overview

The HR RAG Chatbot is an advanced, enterprise-grade solution leveraging Retrieval Augmented Generation (RAG) to provide accurate and context-aware responses to HR-related queries. Built with scalability, security, and compliance in mind, this chatbot integrates seamlessly with existing HR systems while offering cutting-edge AI capabilities.

## Key Features

- **Multi-Agent Orchestration**: Utilizes AWS Bedrock for intelligent query routing and response generation
- **Vector Database Integration**: High-performance similarity search using OpenSearch for efficient document retrieval
- **Open-Source Model Support**: Incorporates HuggingFace embeddings for cost-effective and customizable NLP tasks
- **React-based Frontend**: Responsive and intuitive user interface for seamless interaction
- **Containerized Architecture**: Docker-based deployment for consistency across environments
- **Enterprise Security**: Vault integration for secrets management, TLS/SSL support, and role-based access control

## Architecture

The HR RAG Chatbot employs a microservices architecture with the following key components:

1. **Frontend Service**: React-based SPA hosted on NGINX
2. **Backend API**: FastAPI service for handling chat requests and orchestrating responses
3. **Document Processor**: Ingests and chunks HR documents, generating embeddings for vector search
4. **Vector Database**: OpenSearch for efficient similarity search of HR policies and documents
5. **LLM Integration**: AWS Bedrock client for accessing foundation models
6. **Multi-Agent System**: Specialized agents for different types of HR queries (policies, benefits, procedures)

## Getting Started

### Prerequisites

- Docker and Docker Compose
- AWS Account with Bedrock access
- OpenSearch cluster (can be set up using provided Terraform scripts)

### Installation

1. Clone the repository:
```

git clone https://github.com/thedataengineer/hr-rag-chatbot.git
cd hr-rag-chatbot

```

2. Set up environment variables:
```

cp .env.example .env

# Edit .env with your specific configurations

```

3. Build and run the containers:
```

docker-compose up --build

```

4. Access the chatbot at `http://localhost:3000`

## Development

### Backend (Python)

The backend is built with FastAPI and uses poetry for dependency management.

```

cd backend
poetry install
poetry run uvicorn api.main:app --reload

```

### Frontend (React)

```

cd frontend
npm install
npm start

```

## Testing

- Backend: `pytest backend/tests`
- Frontend: `npm test`
- E2E: `npm run cypress:open`

## Deployment

Deployment is managed through GitHub Actions CI/CD pipelines. See `.github/workflows` for details.

## Security

This project adheres to enterprise security standards:

- Secrets management via HashiCorp Vault
- TLS/SSL encryption for all communications
- Regular security audits and penetration testing
- Compliance with GDPR, CCPA, and other relevant data protection regulations

For more information, see `SECURITY.md`.

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## Roadmap

- [ ] Integration with popular HRIS systems (Workday, SAP SuccessFactors)
- [ ] Multi-language support
- [ ] Advanced analytics dashboard for HR insights
- [ ] AI-driven policy recommendation engine

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- AWS Bedrock team for their excellent foundation model services
- HuggingFace for open-source NLP models
- The FastAPI and React communities for their robust frameworks

---

Built with ❤️ by Karteek Yadavilli, Field CTO and VP of Strategy at Accion Labs
```