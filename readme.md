# IPv4 Subnet Calculator - GUI Edition

### Overview
The **IPv4 Subnet Calculator** is a Python-based desktop application designed to simplify subnet calculations. It provides precise results for network administrators, students, and IT professionals by automating complex subnetting tasks.

Initially conceptualized as a web application using React, the project evolved into a standalone GUI app using Python's Tkinter library, offering a lightweight and accessible tool for subnetting without a browser dependency.

---

### Features
- **IP Input Validation**: Ensures user-entered IP addresses are in valid IPv4 format.
- **Subnet Mask Flexibility**: Accepts subnet masks in both CIDR (e.g., `/24`) and dotted decimal (e.g., `255.255.255.0`) notations.
- **Network and Broadcast Address Calculation**: Displays the network and broadcast addresses instantly.
- **Host Range and Usable Hosts**: Provides the range of usable host IPs and counts the total usable hosts.
- **CIDR Notation and Subnet Mask**: Converts between CIDR and dotted decimal formats for the subnet mask.
- **IP Class Identification**: Identifies the class (A, B, C, D, E) of the given IP address.
- **Binary Conversion**: Displays the binary representation of the IP address and subnet mask.
- **User-Friendly GUI**: A clean and intuitive interface for seamless user interaction.

---

### Technology Stack
- **Frontend**: Python Tkinter (GUI)
- **Backend**: Python with `ipaddress` module for subnetting logic

---

### Installation

#### Prerequisites
- Python 3.x installed on your system.

#### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Jain2098/python-subnet-gui.git

2. Navigate to the project directory:
    ```bash
    cd python-subnet-gui

3. Activate a virtual environment (OPTIONAL):
    ```bash
    .\.venv\Scripts\activate

4. Run the application:
    ```bash
    python main.py


### Usage
1. **Launch the application**:
   - Open a terminal or command prompt.

2. **Enter a valid IPv4 address and subnet mask**:
   - Example inputs:
     - **IP Address**: `192.168.1.1`
     - **Subnet Mask**: `255.255.255.0` or `/24`

3. **Click the "Calculate" button**:
   - The tool will instantly compute the subnet details.

4. **View detailed results**, including:
   - **Network Address**: The base address of the subnet.
   - **Broadcast Address**: The last address in the subnet.
   - **Host Range**: The first and last usable IPs.
   - **Usable Hosts**: The total number of usable IPs.
   - **Subnet Mask**: Displayed in both CIDR (`/24`) and dotted decimal (`255.255.255.0`) formats.
   - **Binary Representations**: Binary format of IP and subnet mask.
   - **IP Class**: Classification of the IP address (A, B, C, etc.).

---

### Screenshots
Here is the screenshot of the IPv4 Subnet Calculator in action:

![Start and Calculated](https://imgshare.xyz/img/5/67982e4b1676195efaa53cbe/Start%20and%20Calculated.png)

---

<!-- THANK YOU -->
### Acknowledgements
- **[ipaddress](https://docs.python.org/3/library/ipaddress.html)** module in Python for subnetting logic.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** library for GUI development.
- **[Python](https://www.python.org/)** programming language for building the application.

---

### License
Distributed under the MIT License.


### Thank you for using the IPv4 Subnet Calculator! 🚀
---
---