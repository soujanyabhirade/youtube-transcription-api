#!/bin/bash

echo "Starting YouTube Transcription Server..."
echo ""

# Activate virtual environment if it exists
if [ -f ".venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Check if cookies.txt exists
if [ ! -f "cookies.txt" ]; then
    echo "WARNING: cookies.txt not found!"
    echo "Please export cookies from your browser first."
    echo "See README.md for instructions."
    echo ""
    read -p "Press enter to exit..."
    exit 1
fi

# Start the server
echo "Starting server on http://127.0.0.1:8000"
echo "Press Ctrl+C to stop"
echo ""
python main.py
