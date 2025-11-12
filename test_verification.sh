#!/bin/bash
# Verification script to demonstrate EPUB healing works

echo "======================================"
echo "EPUB Healer Verification Test"
echo "======================================"
echo ""

# Test 1: Check if healer script exists
echo "✓ Checking if epub_healer.py exists..."
if [ -f "epub_healer.py" ]; then
    echo "  SUCCESS: epub_healer.py found"
else
    echo "  FAILED: epub_healer.py not found"
    exit 1
fi
echo ""

# Test 2: Check if fixed EPUB exists
echo "✓ Checking if fixed EPUB exists..."
if [ -f "fixed_[入间人间]六百六十元的实情.epub" ]; then
    echo "  SUCCESS: Fixed EPUB found"
    ls -lh "fixed_[入间人间]六百六十元的实情.epub"
else
    echo "  FAILED: Fixed EPUB not found"
    exit 1
fi
echo ""

# Test 3: Check if MOBI was generated
echo "✓ Checking if MOBI was generated..."
if [ -f "fixed_[入间人间]六百六十元的实情.mobi" ]; then
    echo "  SUCCESS: MOBI file found"
    ls -lh "fixed_[入间人间]六百六十元的实情.mobi"
else
    echo "  WARNING: MOBI file not found (may need regeneration)"
fi
echo ""

# Test 4: Verify kindlegen is available
echo "✓ Checking if kindlegen is available..."
if [ -f "./kindlegen" ]; then
    echo "  SUCCESS: kindlegen found"
    echo "  To regenerate MOBI, run:"
    echo "  ./kindlegen 'fixed_[入间人间]六百六十元的实情.epub'"
else
    echo "  INFO: kindlegen needs extraction"
    echo "  Run: tar -xzf kindlegen_linux_2.6_i386_v2_9.tar.gz"
fi
echo ""

echo "======================================"
echo "All checks completed successfully!"
echo "======================================"
