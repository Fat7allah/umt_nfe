#!/bin/bash

# Build assets
bench build

# Clear website cache
bench clear-website-cache

# Clear cache
bench clear-cache

# Restart bench
bench restart
