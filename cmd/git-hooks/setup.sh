# #!/bin/bash
# setup for githooks. 
# IMPORTANT: Make sure to run this command from the root folder of the repository
# e.g.: cmd/git-hooks/setup.sh

# pre-commit
rm -f .git/hooks/pre-commit
ln -s ../../cmd/git-hooks/pre-commit .git/hooks/pre-commit
