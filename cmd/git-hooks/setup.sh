# #!/bin/bash
# setup for githooks

# pre-commit
rm .git/hooks/pre-commit
ln -s cmd/git-hooks/pre-commit .git/hooks/pre-commit
