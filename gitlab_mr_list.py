import os

import gitlab


def get_open_merge_requests():
    """
    :return: a list of Merge request objects which are open and not WIP
    """
    gl = gitlab.Gitlab(os.environ.get('GITLAB_URL'), os.environ.get('GITLAB_TOKEN'))
    projects = gl.list(gitlab.Project)
    merge_requests = []
    for proj in projects:
        mrs = gl.list(gitlab.ProjectMergeRequest, project_id=proj.id, state='opened', wip=False)
        merge_requests += [m for m in mrs if not m.title.startswith('WIP')]  # wip attr seems not to be used
    return merge_requests


if __name__ == '__main__':
    print(["%s: %s" % (m.title, m.web_url) for m in get_open_merge_requests()])
