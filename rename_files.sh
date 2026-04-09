#!/bin/bash
# Rename files to remove -unmatched suffix (preserves git history)

set -e

cd "$(dirname "$0")"

echo "Renaming files to remove -unmatched..."

# Rename reference files
echo ""
echo "Reference files:"
ref_count=0
for f in data/reference/*-unmatched*.jsonl; do
    if [ -f "$f" ]; then
        newname="${f//-unmatched/}"
        echo "  $f -> $newname"
        git mv "$f" "$newname"
        ((ref_count++))
    fi
done

# Rename system submission files
echo ""
echo "System submission files:"
sys_count=0
for f in data/systems/*-unmatched*.jsonl; do
    if [ -f "$f" ]; then
        newname="${f//-unmatched/}"
        echo "  $f -> $newname"
        git mv "$f" "$newname"
        ((sys_count++))
    fi
done

echo ""
echo "Renamed $ref_count reference files and $sys_count system files"
echo ""
echo "You can now run: git status"
echo "Then commit with: git commit -m 'Rename files: remove -unmatched suffix for consistency'"
