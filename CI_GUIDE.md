# SafeStride CI Guide

## Purpose

This guide describes the Continuous Integration workflow used for the SafeStride project.

## Development Workflow

Developers should follow these steps when making changes:

1. Update the local main branch.
2. Create a separate feature branch.
3. Make and test the required changes.
4. Commit the changes with a clear commit message.
5. Push the feature branch to GitHub.
6. Create a Pull Request targeting main.
7. Assign another project member as reviewer.
8. Add review comments and obtain approval.
9. Merge the Pull Request into main.
10. Synchronize the local main branch.

## Jenkins CI Workflow

Jenkins monitors the main branch and validates the project after changes are merged.

The CI process includes:

1. Checkout the latest source code.
2. Install dependencies from requirements.txt.
3. Compile the Python modules.
4. Run the automated pytest test suite.
5. Validate the deployment configuration.

## Testing

Before creating a Pull Request, run:

python -m pytest

## Python Compilation

The main Python modules can be checked with:

python -m py_compile ai_engine.py
python -m py_compile nav_engine.py
python -m py_compile server.py

## Pull Request Checklist

Before requesting a review:

- Code changes are complete.
- Python compilation succeeds.
- Automated tests pass.
- No unnecessary files such as __pycache__ are committed.
- Changes are committed with a clear message.
- Feature branch is pushed to GitHub.
- Pull Request targets main.
- Another project member is assigned as reviewer.

## Merge and Verification

After approval and merge:

1. Switch to main.
2. Pull the latest changes from GitHub.
3. Run the test suite again.
4. Confirm that the local branch is synchronized with origin/main.

This workflow helps maintain consistent code review, testing, and continuous integration practices for SafeStride.
