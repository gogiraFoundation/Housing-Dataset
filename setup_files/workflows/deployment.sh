#!/bin/bash

# Define branch names
MAIN_BRANCH="main"
TEST_BRANCH="deployment"
DEVELOPMENT_BRANCH="working_tree"
CURRENT_BRANCH=$(git branch --show-current)

# Ensure the script is not run on the main branch directly
if [ "$CURRENT_BRANCH" = "$MAIN_BRANCH" ]; then
    echo "⚠️  Error: Please switch to a feature or development branch before running this script."
    exit 1
fi

# Fetch the latest changes from remote to ensure the branches are up to date
git fetch origin

# Step 1: Create or switch to the tEST branch based oFF the development branch
echo "🔄 Creating or updating '$TEST_BRANCH' branch from '$DEVELOPMENT_BRANCH'..."
git checkout -B $TEST_BRANCH
git pull origin -A $DEVELOPMENT_BRANCH


#COMMIT ALL UNSTAGED CHANGES
git add -A
git commit -A -m "commiting all unstaged changes"
git push origin $TEST_BRANCH

echo "branch staged for merging"

# Step 2: Merge current branch into working_tree for testing
echo "🚧 Merging '$CURRENT_BRANCH' into '$TEST_BRANCH' for testing..."
if git merge $CURRENT_BRANCH; then
    echo "✅ Merge successful on '$TEST_BRANCH'. Ready to merge into main."
else
    echo "❌ Merge conflict detected while merging '$CURRENT_BRANCH' into '$TEST_BRANCH'."
    echo "Please resolve conflicts in '$TEST_BRANCH' before continuing."
    exit 1
fi

# Optional: Run tests or checks here (e.g., unit tests)
# ./run-tests.sh

# Step 3: If tests are successful, merge working_tree into main
echo "🔄 Merging '$TEST_BRANCH' into '$MAIN_BRANCH'..."
git checkout $MAIN_BRANCH
if git merge $TEST_BRANCH; then
    echo "✅ Successfully merged '$TEST_BRANCH' into '$MAIN_BRANCH'. Pushing changes to origin."
    git push origin $MAIN_BRANCH
else
    echo "❌ Merge conflict detected while merging '$TEST_BRANCH' into '$MAIN_BRANCH'."
    echo "Please resolve conflicts in '$MAIN_BRANCH' before pushing."
    exit 1
fi

# Step 4: Clean up by switching back to the original branch
git checkout $CURRENT_BRANCH
echo "🎉 Merge process complete. Returned to branch '$CURRENT_BRANCH'."

