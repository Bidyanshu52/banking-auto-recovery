# Banking Service Availability & Auto-Recovery Mini Project

## What it demonstrates
A small, **non-production** banking-service status API packaged in Docker. It exposes `/` and `/health`. The `/crash` endpoint deliberately terminates the main application process so Docker can restart the container.

## Run locally (Docker required)
```bash
docker compose up --build -d
curl http://localhost:5000/
curl http://localhost:5000/health
```
Simulate a crash (the request will fail because the process exits):
```bash
curl -X POST http://localhost:5000/crash
docker compose ps
docker compose logs --tail=50 banking-api
curl http://localhost:5000/health
```
Because `restart: unless-stopped` is set, Docker should restart the container. Measure TTR with a stopwatch from crash request to first successful `/health` response. Repeat 3 times and report actual results.

## AWS target architecture (for the presentation)
Client -> Application Load Balancer -> ECS Fargate Service (desired count 2) -> Docker image in ECR. CloudWatch collects container logs/metrics and alarms on unhealthy targets / elevated 5xx. ECS replaces failed tasks. Use private subnets for tasks, IAM task roles with least privilege, Secrets Manager for credentials, TLS at the ALB, and budget alerts.

## Important limitations / honest presentation notes
- This starter app is a demo, not a real banking platform; it has no accounts, balances, authentication, or transaction processing.
- The local Docker restart demo proves local container restart, **not** AWS ECS auto-recovery.
- For an AWS demo, build and push the image to ECR, create an ECS Fargate service behind an ALB, configure CloudWatch logs/alarms, and use the ECS service desired count to replace stopped tasks.
- Do not publish real credentials or customer data.
- Replace the GitHub URL and live application URL in the slides after you actually create/deploy them.
