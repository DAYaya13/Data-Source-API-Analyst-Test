# 🛠 Troubleshooting Guide – GitHub API Extraction

This document summarizes the most common errors encountered during authentication and data consumption from the GitHub API, and how to resolve them.

---

## 1. Error 401 Unauthorized

**Message:**  
```json
{
  "message": "Bad credentials",
  "documentation_url": "https://docs.github.com/rest",
  "status": "401"
}
Possible Causes:
Invalid or incorrectly copied token
Make sure you are using a valid Personal Access Token (PAT) generated from: https://github.com/settings/tokens
The token should not contain extra spaces, quotes, or hidden characters.

Malformed header
The correct header must be:

makefile
Copiar
Editar
Authorization: Bearer <your_token>
Token lacks required permissions
Verify that the token has the necessary scopes (e.g., repo or public_repo).

Expired or revoked token
If the token has been revoked or expired, generate a new one.

2. Rate Limit Exceeded
Common error message:

json
Copiar
Editar
{
  "message": "API rate limit exceeded",
  "documentation_url": "...",
  "status": "403"
}
Solution:
Authenticated users: have a limit of 5000 requests per hour.

Unauthenticated users: only 60 requests per hour.

To avoid this error:

Always use token authentication in your requests.

Implement error handling and wait (time.sleep()) if the rate limit is reached.

Inspect these headers in each response to monitor usage:

X-RateLimit-Limit

X-RateLimit-Remaining

X-RateLimit-Reset

3. Verify your tests with Postman
If you are using Postman:

Ensure environment variables are set correctly:

Authorization → Bearer <your_token>

X-GitHub-Api-Version → 2022-11-28

Use the Authorization tab and select the type Bearer Token.

Save and reuse environment variables to avoid errors in repeated requests.

Resources
GitHub REST API documentation: https://docs.github.com/en/rest

Rate Limits management: https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting
