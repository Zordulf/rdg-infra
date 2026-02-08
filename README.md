
[![CI](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml/badge.svg)](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml)
[![CD](https://github.com/Zordulf/rdg-infra/actions/workflows/cd.yml/badge.svg)](https://github.com/Zordulf/rdg-infra/actions/workflows/cd.yml)

[![CI](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml/badge.svg)](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml)


[![CI](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml/badge.svg)](https://github.com/Zordulf/rdg-infra/actions/workflows/ci.yml)
[![CD](https://github.com/Zordulf/rdg-infra/actions/workflows/cd.yml/badge.svg)](https://github.com/Zordulf/rdg-infra/actions/workflows/cd.yml)

AWS Free-Tier DevSecOps Infrastructure with Complete CI/CD Pipeline

## Architecture

- **VPC** with public, private, and data subnets
- **Lambda** (containerized) for API handling
- **API Gateway** for HTTP endpoints
- **DynamoDB** for data storage
- **ECR** for Docker images

## CI/CD Pipeline

- ✅ Code linting and validation
- ✅ Docker build and push
- ✅ Security scanning (Trivy)
- ✅ Infrastructure deployment (Terraform)
- ✅ Automated smoke tests

## Tech Stack

- **Language:** Python 3.11
- **Infrastructure:** Terraform
- **Container:** Docker
- **CI/CD:** GitHub Actions
- **Cloud:** AWS (Free Tier)

## Quick Start
```bash
# Deploy infrastructure
cd terraform
terraform init
terraform apply
```

## API Endpoints

- `GET /` - List all items
- `POST /` - Create new item
- `DELETE /{id}` - Delete item

## Cost

**$0.00** - Completely free tier!

## License

MIT

## Status

Project initialized and connected to GitHub! ✅
