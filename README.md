# Data-Source-API-Analyst-Test
## Step 1: Prepare & Test a List of Reports

### 1. Client Needs
The goal was to extract the following types of data from the GitHub API:
- Public repositories via keyword search
- Commits from a given repository
- File contents (like README.md) from a repository

### 2. GitHub API Research

#### Key Endpoints:
- `/search/repositories?q=...`
- `/repos/{owner}/{repo}/commits`
- `/repos/{owner}/{repo}/contents/{path}`

#### API Concepts:
- **Authentication:** via Bearer Token
- **Headers:** `Authorization`, `X-GitHub-Api-Version`
- **Pagination:** `?page=n&per_page=m`
- **Rate Limits:**
  - 5000 req/hr (authenticated)
  - 60 req/hr (unauthenticated)
- **Common Errors:**
  - `401 Unauthorized` – Check token and headers
  - `403 Rate Limit` – Add delay or monitor remaining quota
  - `404 Not Found` – Check endpoint path or repo name
