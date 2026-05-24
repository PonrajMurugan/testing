import sys
import platform

print("=" * 50)
print("  Skill input fields demo (fields -> sys.argv)")
print("=" * 50)

# Echo every argument so you can SEE how fields land in sys.argv
print()
print(f"Total arguments: {len(sys.argv) - 1}")
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"  sys.argv[{i}] = {arg!r}")

# Pull values by position (matches the field order in the skill)
user_name = sys.argv[1] if len(sys.argv) > 1 else "unknown"
company_name = sys.argv[2] if len(sys.argv) > 2 else "unknown"

print()
print(f"Hello, {user_name}!")
print(f"You are part of {company_name}.")
print(f"Running on: {platform.system()} {platform.release()}")
print()
print("-- end --")
