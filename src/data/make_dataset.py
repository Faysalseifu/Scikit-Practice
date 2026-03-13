from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    print(f"Scikit-Learn practice scaffold is ready at: {project_root}")


if __name__ == "__main__":
    main()
