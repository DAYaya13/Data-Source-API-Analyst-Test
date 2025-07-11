# 🛠️ Troubleshooting Guide - GitHub API

This document provides guidance for handling common errors and problems encountered while working with the GitHub REST API.

---

## 401 Unauthorized

### Problem:
The API returns a 401 error when trying to access endpoints.

### Solution:
- Check that your GitHub Personal Access Token (PAT) is active.
- Ensure the token is included correctly in the `Authorization` header:
  ```bash
  Authorization: Bearer <your_token>
