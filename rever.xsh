$PROJECT = 'pkgname'
$ACTIVITIES = ['version_bump', 'changelog', 'tag', 'push_tag', 'ghrelease', 'conda_forge']

$VERSION_BUMP_PATTERNS = [
    ('pkgname/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'version\s*=.*,', "version='$VERSION',")
    ]
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']
$PUSH_TAG_REMOTE = 'git@github.com:billingegroup/mpl-stylesheets.git'

$GITHUB_ORG = 'billingeGroup'
$GITHUB_REPO = 'mpl-stylesheets'
