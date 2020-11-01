$PROJECT = 'billinge_style'
$ACTIVITIES = ['version_bump', 'changelog', 'tag', 'push_tag', 'ghrelease', 'conda_forge']

$VERSION_BUMP_PATTERNS = [
    ('billinge_style/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'version\s*=.*,', "version='$VERSION',")
    ]
$CHANGELOG_FILENAME = 'v0.1.0.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']
$PUSH_TAG_REMOTE = 'git@github.com:billingegroup/mpl-stylesheets.git'

$GITHUB_ORG = 'billingeGroup'
$GITHUB_REPO = 'mpl-stylesheets'
