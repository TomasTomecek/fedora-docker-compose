# Fedora docker-compose

Fedora Linux ships latest python version of docker-compose (1.29.2).

This repository tracks that maintenance effort.

There is no feature development expected here. Just to keep the python implementation alive.


## How to release

1. Create a new PR, branch name `release-$version`
2. Put new version in these two files:
    1. Update version in fedora/docker-compose.spec
    2. Update version in compose/__init__.py
3. Commit, title: `Create new upstream release: $version`
4. Create a pull request
5. Make sure all builds pass
6. Merge
7. Create a new GitHub release, title = tag = `$version`
7. Wait for Packit to process it and create a PR in: https://src.fedoraproject.org/rpms/docker-compose/pull-requests
8. Review the PR
9. Wait for all builds to pass
10. Merge
11. Have a lovely day! ☀️
