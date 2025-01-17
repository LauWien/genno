Releasing
*********

Before releasing, check:

- https://github.com/khaeru/genno/actions/workflows/pytest.yaml?query=branch:main to ensure that the push and scheduled builds are passing.
- https://readthedocs.org/projects/genno/builds/ to ensure that the docs build is passing.

Address any failures before releasing.

1. Edit :file:`doc/whatsnew.rst`.
   Comment the heading "Next release", then insert another heading below it, at the same level, with the version number and date.
   Make a commit with a message like "Mark vX.Y.Z in doc/whatsnew".

2. Tag the release candidate version, i.e. with a ``rcN`` suffix, and push::

    $ git tag v1.2.3rc1
    $ git push --tags origin main

3. Check:

   - at https://github.com/khaeru/genno/actions/workflows/publish.yaml that the workflow completes: the package builds successfully and is published to TestPyPI.
   - at https://test.pypi.org/project/genno/ that:

      - The package can be downloaded, installed and run.
      - The README is rendered correctly.

   Address any warnings or errors that appear.
   If needed, make a new commit and go back to step (2), incrementing the rc number.

4. (optional) Tag the release itself and push::

    $ git tag v1.2.3
    $ git push --tags origin main

   This step (but *not* step (2)) can also be performed directly on GitHub; see (5), next.

5. Visit https://github.com/khaeru/genno/releases and mark the new release: either using the pushed tag from (4), or by creating the tag and release simultaneously.

6. Check at https://github.com/khaeru/genno/actions/workflows/publish.yaml and https://pypi.org/project/genno/ that the distributions are published.
