### Blockchain Parser with `libbitcoinkernel` using Python

This is a simple blockchain block parser that utilizes **libbitcoinkernel** through the Python wrapper available at:  
[py-bitcoinkernel](https://github.com/stickies-v/py-bitcoinkernel)

#### Installation Guide

**Requirements**

- Python version >= 3.10

**Steps**

1. Create and activate a new virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

2. Install the required dependencies (`py-bitcoinkernel` and `py-bitcoinlib`):

    ```bash
    pip install . -v
    ```

3. Run the application:

    ```bash
    python src/main.py --datadir='<directory>' --chain_type=<chain> --start_height=<height> --end_height=<height>
    ```

This is a simple example that demonstrates how to use the Python wrapper for the `libbitcoinkernel` library to read blockchain data from a specified height range.

You can easily modify this to suit your needs.
