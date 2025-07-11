GitHub API Documentation (Used Endpoints)

This document describes the GitHub REST API endpoints used in this assignment, along with request structure, required headers, and behavior related to authentication, pagination, and rate limits.
---
Authentication
All requests use token-based authentication via Personal Access Token (PAT).
Required Headers:
Authorization: Bearer <my_token>
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
---
1. Search Public Repositories
Endpoint:
GET /search/repositories
Example:
https://api.github.com/search/repositories?q=machine+learning&per_page=5
Purpose:
Retrieve public repositories matching a keyword
Notes:
Response includes list of repo objects
Supports pagination (page and per_page)
---
2. List Commits
Endpoint:
GET /repos/{owner}/{repo}/commits
Example:
https://api.github.com/repos/psf/requests/commits?page=1&per_page=5
Purpose:
Retrieve recent commits from a given repository
Notes:
Paginated results
Useful for tracking repo activity
---
3. Get File Content
Endpoint:
GET /repos/{owner}/{repo}/contents/{path}
Example:
https://api.github.com/repos/psf/requests/contents/README.md
Purpose:
Get content of specific files (like README.md)
Notes:
Response contains file info + Base64-encoded content
Only available for files in the default branch (main or master)
---
Pagination Overview
Parameters:
- page: page number (e.g. 1, 2, ...)
- per_page: number of results per page (max: 100)
Example:
?page=2&per_page=10
---
Rate Limits
GitHub applies rate limits based on authentication:

User Type      | Limit per hour
-------------- | -------------
Authenticated  | 5000 requests
Unauthenticated| 60 requests

To monitor usage, inspect headers like:
X-RateLimit-Limit
X-RateLimit-Remaining
X-RateLimit-Reset
---
Common Error Responses
Code | Meaning       | Solution
-----|--------------|--------------------------------------
401  | Unauthorized | Check token and Authorization header
403  | Rate limit hit | Wait and retry after X-RateLimit-Reset
404  | Not found    | Check URL path, file name or repo name
---
Resources
- GitHub REST API docs: https://docs.github.com/en/rest
- GitHub API quickstart: https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28
<img width="432" height="615" alt="image" src="https://github.com/user-attachments/assets/f5505d04-5990-4e62-926e-526f81fae6d6" />

