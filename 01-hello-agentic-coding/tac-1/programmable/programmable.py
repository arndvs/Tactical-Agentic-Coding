import subprocess
import sys


def main():
    with open("programmable/prompt.md", "r") as f:
        prompt_content = f.read()

    command = [
        "claude",
        "-p",
        prompt_content,
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True)

        print(result.stdout)

        if result.stderr:
            print(result.stderr, file=sys.stderr)

        sys.exit(result.returncode)

    except Exception as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
