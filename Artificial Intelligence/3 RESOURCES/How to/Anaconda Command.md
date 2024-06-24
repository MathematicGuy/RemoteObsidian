
```ad-note
**Important Notes:**

- You'll typically execute these commands in your command prompt or terminal (like Windows PowerShell or cmd.exe)
- Replace `<environment_name>` and `<package_name>` with the actual names you want to use.
```

**conda create -n <environment_name> [packages]**
Creates a new environment with a specified name and optionally installs a list of packages. Example: `conda create -n my-ai python=3.9 numpy pandas`

---

**Install from requirement.txt**
pip install -r requirements.txt

**conda activate <environment_name>**

-   
    Activates a specific environment. Example: `conda activate my_ml_env`
    
- **conda deactivate** Deactivates the current environment.
    
- **conda env list** Lists all the available conda environments.
    
- **conda env remove -n <environment_name>** Deletes an environment.
    

**Package Management**

- **conda install <package_name>**  
    Installs a package in the current active environment. Example: `conda install scikit-learn`
    
- **conda update <package_name>**  
    Updates a package in the current environment. Example: `conda update tensorflow`
    
- **conda remove <package_name>** Removes a package from the current environment.
    
- **conda list**  
    Lists all packages installed within the current environment.
    
- **conda search <package_name>** Searches for packages in the Anaconda repositories.
    

**Getting Information**

- **conda info**  
    Displays general information about your Anaconda installation.
    
- **conda info --envs**  
    Displays information specifically about your environments.
    

**Additional Useful Commands**

- **conda env export > environment.yml**  
    Exports the current environment requirements to a YAML file, useful for reproducibility.
    
- **conda env create -f environment.yml** Creates a new environment from a YAML specification file.