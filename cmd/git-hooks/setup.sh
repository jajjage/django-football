# #!/bin/bash
# setup for githooks. 
# IMPORTANT: Make sure to run this command from the root folder of the repository

# pre-commit
rm .git/hooks/pre-commit
ln -s ../../cmd/git-hooks/pre-commit .git/hooks/pre-commit
