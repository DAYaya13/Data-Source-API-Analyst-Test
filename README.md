# Data-Source-API-Analyst-Test
# Data Source API Analyst - Homework Assignment

## 📌 Project Description

This repository was created as part of the technical homework for the **Data Source API Analyst** role at Improvado.

The goal of the assignment is to demonstrate the ability to work with REST APIs, specifically the GitHub API, by:
- Understanding data extraction needs
- Testing API endpoints (repositories, commits, file contents)
- Handling authentication, pagination, and error responses
- Documenting the process clearly
- Delivering results via Postman or Google Colab

---

## 🗂️ Repository Structure

```bash
.
├── README.md                        ← Overview of the task, structure and reflections
├── Content/
│   ├── api_documentation.md        ← API endpoints used, structure and key concepts
│   ├── github_api_extraction.py    ← Python code for authentication and data extraction
│   ├── troubleshooting.md          ← Notes and solutions to common API errors
└── Postman_Collection/
    └── github_api_colab.ipynb      ← Colab notebook with test results and code implementation

🚀 Approach Summary
✅ Step 1: Understand Client Needs
Analyzed the requirement to extract:

Public repositories

Commit history

File contents (e.g., README.md)

✅ Step 2: Research GitHub API
Identified the following endpoints:

/search/repositories

/repos/{owner}/{repo}/commits

/repos/{owner}/{repo}/contents/{path}

Studied:

Authentication with personal access tokens

Pagination with ?page= and per_page=

Rate limits and error codes

✅ Step 3: Implement in Google Colab
Used requests and json to connect to the API

Managed pagination and token-based authentication

Handled 401 (Unauthorized) and 403 (Rate Limit) errors

🔍 Testing Results
You can find the Colab implementation and outputs in the Postman_Collection/ folder. The code extracts public repo data and demonstrates how to handle multiple API layers.

💡 Reflection
This assignment was a great opportunity to demonstrate practical knowledge in working with APIs. It required understanding the API's behavior, ensuring robustness in the code, and maintaining good documentation — all critical in data integration roles.

Thank you for the opportunity!

🧵 Contact
Prepared by: Yadira Dominguez
