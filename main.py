import os
from pydriller.metrics.process.lines_count import LinesCount

def get_diff_stats(repo_path: str, base: str, head: str) -> int:
    metric = LinesCount(path_to_repo=repo_path,
                        from_commit=base,
                        to_commit=head)

    changed_lines = 0

    for lines in metric.count().values():
        changed_lines += lines

    return changed_lines

def add_label_to_pr(line_count: int):
    session = requests.Session()
    session.auth = (os.getenv("GITHUB_ACTOR"), os.getenv("GITHUB_API_TOKEN"))
   
    pr_number = os.getenv("GITHUB_REPOSITORY").split('/', 1)[0]
    url = os.getenv("GITHUB_API_URL") + "/repos/" +  os.getenv("GITHUB_REPOSITORY") + "/issues/" + pr_number + "/labels"


def main():
    lines_changed = get_diff_stats("./", os.getenv("GITHUB_BASE_REF"), os.getenv("GITHUB_HEAD_REF"))
    print(lines_changed)

if __name__ == "__main__" :
    main()
