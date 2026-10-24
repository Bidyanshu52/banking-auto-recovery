# 90-second speaking plan
1. We selected Banking because customers expect reliable digital services.
2. Our prototype is a small status API in Docker; it is not a real banking app.
3. We deliberately crash it using a demo endpoint, then observe automatic restart.
4. TTR is measured from the crash trigger to the first successful health check.
5. The AWS target architecture uses ECR, ECS Fargate, an ALB, and CloudWatch.
6. Security includes TLS, private subnets, least privilege, secrets management, and no customer data.
7. We will report only measurements actually observed.

# Before presenting
- [ ] Open the PPT and update any slide details your professor specified in class.
- [ ] Run `docker compose up --build -d`.
- [ ] Test `http://localhost:5000/health`.
- [ ] Run `curl -X POST http://localhost:5000/crash`.
- [ ] Wait for restart and test health again.
- [ ] Record actual TTR; screenshot logs.
- [ ] Create GitHub repository and push these files if a repository link is required.
- [ ] Only enter a live URL if you have genuinely deployed it.
