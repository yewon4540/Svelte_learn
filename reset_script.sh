#!/bin/bash

echo "Cleaning SvelteKit project..."

# 삭제 대상 목록
TARGETS=(
  node_modules
  .svelte-kit
  build
  dist
  .turbo
  package-lock.json
  pnpm-lock.yaml
  yarn.lock
)

for item in "${TARGETS[@]}"; do
  if [ -e "$item" ]; then
    echo "Removing $item"
    rm -rf "$item"
  fi
done

# git 초기화 여부
read -p "Do you want to reinitialize git? (y/N): " answer
if [[ "$answer" =~ ^[Yy]$ ]]; then
  echo "Reinitializing git..."
  rm -rf .git
  git init
  echo "# SvelteKit initialized repo" > README.md
  git add .
  git commit -m "Initial commit after cleanup"
fi

# npm install
echo "Installing dependencies..."
npm install

echo "SvelteKit project reset complete."

