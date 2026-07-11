# GitHub for a five-year-old

GitHub is an online shelf for code.

- Your project folder is a **toy box**.
- Git takes **photos** of the toy box over time. Each photo is a **commit**.
- GitHub stores the toy box and its photos online.
- A repository is one shelf containing one project.

## Suggested repository name

```text
ai-engineering-school
```

Suggested description:

```text
My step-by-step journey from Python basics to machine learning, deep learning, MLOps, and AI applications.
```

## Easy method: GitHub website

1. Create an empty repository named `ai-engineering-school`.
2. Extract the downloaded ZIP file.
3. Open your empty repository on GitHub.
4. Choose the option to add/upload files.
5. Drag the **contents** of the extracted `ai-engineering-school` folder into the upload area.
6. Write a message such as `Add initial AI engineering school structure`.
7. Commit the upload.

## Better long-term method: Git commands

Run these commands from inside the extracted repository folder:

```bash
git init
git add .
git commit -m "Build the first Python classroom"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_REPOSITORY_URL` with the URL of the empty repository you created.

## Your everyday three-step habit

After changing lessons:

```bash
git add .
git commit -m "Describe what I learned"
git push
```

That means: pack the changes, take a labeled photo, and put the photo on the online shelf.
