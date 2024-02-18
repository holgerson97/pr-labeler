from git import Repo
import os

def get_diff_stats(repo_path: str, base: str, head: str) -> int:
    repository = Repo(repo_path)

    base_ref = repository.commit(base)
    head_ref = repository.commit(head)
    diffs = base_ref.diff(head_ref)

    stats = diffs

    return stats

def main():
    lines_changed = get_diff_stats("./", os.getenv("GITHUB_BASE_REF"), os.getenv("GITHUB_HEAD_REF"))
    print(lines_changed)

if __name__ == "__main__" :
    main()
