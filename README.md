name: ArtHobbies Stock Checker

on: “workflow_dispatch”

jobs:
check-stock:
runs-on: ubuntu-latest
steps:
- name: Get checker code
uses: actions/checkout@v4
- name: Run stock checker
run: python check_stock.py
