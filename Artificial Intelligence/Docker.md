Simple Docker workflow Example
```ad-summary

`FROM python:3.11-slim`
- This **sets the base image** for your Docker container.
- It uses Python version **3.11**, with the **slim** tag (a minimal version of the Python image that is smaller in size).
- Slim versions are faster to download and run but might miss some system tools (which you can install manually if needed).

`WORKDIR /app`
- This sets the **working directory** inside the container to `/app`.
- All following commands (`COPY`, `RUN`, etc.) will be **executed relative to this directory**.

`RUN apt-get update && apt-get install -y git`
- `apt-get update`: Updates the package index (like refreshing the list of available packages).
- `apt-get install -y git`: Installs Git.
- `-y`: Automatically answers "yes" to prompts during install.
- You probably need Git for installing dependencies or cloning repos.

`COPY requirements.txt .`
- Copies the `requirements.txt` file **from your host machine** into the current working directory (`/app`) inside the container.

`RUN pip install --no-cache-dir -r requirements.txt`
- Installs Python packages listed in `requirements.txt`.
- `--no-cache-dir`: Saves space by **not caching** the installed files (recommended for smaller images).

`COPY . .`
- Copies **everything** from the current directory (your project folder) on your **host machine** into the container’s working directory (`/app`).

`EXPOSE 8000`
- Documents that the container **intends to listen on port 8000**.
- This doesn’t actually publish the port — you still need to do that with `docker run -p 8000:8000`.

  
`CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]`
- This defines the **default command** to run when the container starts.
- It runs a web server called **Uvicorn**.
- `app:app` means:
    - There's a Python file named `app.py`.
    - Inside that file, there's an object or function called `app` (usually a FastAPI or Starlette app).
- `--host 0.0.0.0`: Allows external access to your app.
- `--port 8000`: Listens on port 8000.
- `--workers 4`: Starts 4 worker processes to handle requests (good for production-level performance).
```

