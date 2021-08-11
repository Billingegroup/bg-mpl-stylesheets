$PROJECT = 'bg-mpl-stylesheets'
$ACTIVITIES = [
    'version_bump',
    'changelog',
    'tag',
    'push_tag',
    'ghrelease',
    'conda_forge',
]

# version_bump activity
$VERSION_BUMP_PATTERNS = [
    ('bg_mpl_stylesheet/__init__.py', r'__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', r'version\s*=.*,', "version='$VERSION',")
]

# changelog activity
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']

# tag, push_tag activity
$PUSH_TAG_REMOTE = 'git@github.com:connorjbracy/bg-mpl-stylesheets.git'

# ghrelease activity
$GITHUB_ORG = 'connorjbracy'
$GITHUB_REPO = 'bg-mpl-stylesheets'

# conda_forge activity
$FORGE_FEEDSTOCK_ORG = $GITHUB_ORG
$FORGE_FEEDSTOCK = 'git@github.com:$FORGE_FEEDSTOCK_ORG/$PROJECT-feedstock.git'
$FORGE_PROTOCOL = 'ssh'
$FORGE_SOURCE_URL = 'https://github.com/$GITHUB_ORG/$GITHUB_REPO/releases/download/$VERSION/$PROJECT-$VERSION.tar.gz'
$FORGE_HASH_TYPE = 'sha256'
$FORGE_PULL_REQUEST = True
$FORGE_RERENDER = True
$FORGE_USE_GIT_URL = False
