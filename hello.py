import platform, sys, os
print("Hello from FLUWENT GitHub-fetched script!")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python: {sys.version.split()[0]}")
print(f"Working dir: {os.getcwd()}")
