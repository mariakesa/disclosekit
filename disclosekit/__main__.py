import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: disclosekit [doc|dataset|all] ...")
        sys.exit(1)

    cmd = sys.argv[1]
    sys.argv = [sys.argv[0]] + sys.argv[2:]

    if cmd == "doc":
        from disclosekit.cli.doc import main
    elif cmd == "dataset":
        from disclosekit.cli.dataset import main
    elif cmd == "all":
        from disclosekit.cli.all import main
    else:
        raise SystemExit(f"Unknown command: {cmd}")

    main()


if __name__ == "__main__":
    main()
