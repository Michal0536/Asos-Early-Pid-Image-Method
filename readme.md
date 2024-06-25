# Product Image Analysis Tool 📸

## Overview 🌐
This Python tool scrapes product images from a given range of product IDs and uses a trained TensorFlow model to determine if the images contain specific items. It logs its process and results, and handles tasks in parallel using multithreading.

## Requirements 🛠️
- Python 3.10
- Required packages: `requests`, `tensorflow`, `numpy`, `PIL`, `colorama`, `logging`, `threading`

## Setup 🔧

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Michal0536/Asos-Early-Pid-Image-Method
   cd Asos-Early-Pid-Image-Method
   ```

2. **Install dependencies:**
   ```bash
   pip install requests tensorflow numpy pillow colorama
   ```

## Usage 🚀

1. **Configure Proxies and Tasks:**
   - Update `proxy.txt` with your proxy details to manage requests efficiently.
   - Configure your PID ranges in the script to define which product IDs to analyze.

2. **Run the script:**
   ```bash
   python earlyPid.py
   ```
   - The script will process each product ID, scrape the image, and use a pre-trained TensorFlow model to analyze it.

## How It Works 🧩

- The tool uses proxies for scraping to avoid blocking.
- It logs all activities, including successes and errors.
- The image analysis uses TensorFlow's InceptionV3 model to check if the scraped images meet the specified criteria.

This tool is effective for monitoring and analyzing large sets of product images efficiently.
