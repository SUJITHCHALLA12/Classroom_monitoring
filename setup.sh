#!/bin/bash
# Classroom & Timetable Monitoring System - Quick Setup Script (Linux/Mac)

echo ""
echo "==============================================="
echo "Classroom Timetable Monitoring System"
echo "Quick Setup Script"
echo "==============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[STEP 1] Installing Dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies installed successfully"

echo ""
echo "[STEP 2] Initializing Sample Data (Optional)"
read -p "Do you want to load sample data? (y/n): " sample_choice
if [ "$sample_choice" = "y" ] || [ "$sample_choice" = "Y" ]; then
    python3 init_sample_data.py
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to initialize sample data"
        exit 1
    fi
    echo "✓ Sample data loaded successfully"
fi

echo ""
echo "==============================================="
echo "✓ Setup Complete!"
echo "==============================================="
echo ""
echo "Starting the application..."
echo ""
echo "Once the server starts, open your browser to:"
echo "  http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
