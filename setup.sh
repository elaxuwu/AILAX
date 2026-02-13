#!/bin/bash

# ============================================================
# AILAX Setup Script for Mac/Linux
# ============================================================
# This script will:
# 1. Check if Ollama is installed
# 2. Pull required Ollama models
# 3. Install all required Python packages from requirements.txt
# 4. Download the openwakeword models
#
# Run this script before using AILAX for the first time.
# ============================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print headers
print_header() {
    echo -e "\n${CYAN}============================================================${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}============================================================${NC}\n"
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Function to print error messages
print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to print info messages
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Function to print warning messages
print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Main script starts here
print_header "AILAX Setup Script v1.0"

# Check if Ollama is installed
print_info "Checking for Ollama installation..."
if ! command -v ollama &> /dev/null; then
    print_error "Ollama is not installed or not in PATH!"
    echo ""
    echo "Please install Ollama first:"
    echo "  1. Visit https://ollama.com/download"
    echo "  2. Download and install Ollama for your OS"
    echo "  3. Run this setup script again"
    echo ""
    exit 1
fi

print_success "Ollama is installed:"
ollama --version
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed or not in PATH!"
    echo "Please install Python 3.7+ and try again."
    echo ""
    exit 1
fi

print_info "Python found:"
python3 --version
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 is not installed!"
    echo "Please install pip3 and try again."
    echo ""
    exit 1
fi

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.txt"

# Check if requirements.txt exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    print_error "requirements.txt not found at $REQUIREMENTS_FILE"
    echo "Please make sure requirements.txt is in the same directory as this script."
    echo ""
    exit 1
fi

# Step 1: Pull Ollama models
print_header "Step 1: Pulling Ollama AI Models"
echo "This may take a while depending on your internet connection..."
echo ""

echo "Pulling qwen3-vl:235b-instruct-cloud (General mode model)..."
ollama pull qwen3-vl:235b-instruct-cloud

if [ $? -ne 0 ]; then
    echo ""
    print_warning "Failed to pull qwen3-vl:235b-instruct-cloud"
    echo "You may need to pull it manually later:"
    echo "  ollama pull qwen3-vl:235b-instruct-cloud"
    echo ""
else
    print_success "qwen3-vl:235b-instruct-cloud pulled successfully!"
fi

echo ""
echo "Pulling qwen3-coder-next:cloud (Coding mode model)..."
ollama pull qwen3-coder-next:cloud

if [ $? -ne 0 ]; then
    echo ""
    print_warning "Failed to pull qwen3-coder-next:cloud"
    echo "You may need to pull it manually later:"
    echo "  ollama pull qwen3-coder-next:cloud"
    echo ""
else
    print_success "qwen3-coder-next:cloud pulled successfully!"
fi

# Step 2: Install requirements
print_header "Step 2: Installing Python Packages"
echo "Installing packages from requirements.txt..."
echo ""

python3 -m pip install -r "$REQUIREMENTS_FILE"

if [ $? -ne 0 ]; then
    echo ""
    print_warning "Package installation failed!"
    echo "Please check the error messages above."
    echo ""
    read -p "Do you want to continue anyway? (y/N): " continue_choice
    if [[ ! "$continue_choice" =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
else
    echo ""
    print_success "All packages installed successfully!"
fi

# Step 3: Download openwakeword models
print_header "Step 3: Downloading OpenWakeWord Models"
echo "Downloading openwakeword models..."
echo ""

python3 -c "from openwakeword.utils import download_models; download_models()"

if [ $? -ne 0 ]; then
    echo ""
    print_error "Failed to download OpenWakeWord models."
    echo "You can try manually running:"
    echo "  python3 -c \"from openwakeword.utils import download_models; download_models()\""
    echo ""
else
    echo ""
    print_success "OpenWakeWord models downloaded successfully!"
fi

# Step 4: Summary
print_header "Setup Complete!"
print_success "All setup steps have been completed."
echo ""
echo "You can now run AILAX with:"
echo "  python3 main.py"
echo ""
echo "Or make it executable and run directly:"
echo "  chmod +x main.py"
echo "  ./main.py"
echo ""
echo -e "${CYAN}============================================================${NC}"
echo ""

