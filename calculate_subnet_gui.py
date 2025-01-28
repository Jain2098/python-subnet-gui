import tkinter as tk
from tkinter import messagebox
import subnet_logic


class SubnetCalculatorGUI:
    def __init__(self, root):
        self.ip_entry = None
        self.subnet_entry = None

        self.binary_subnet_label = None
        self.binary_ip_label = None
        self.ip_class_label = None
        self.cidr_label = None
        self.wildcard_mask_label = None
        self.subnet_mask_label = None
        self.usable_hosts_label = None
        self.total_ips_label = None
        self.host_range_label = None
        self.broadcast_label = None
        self.network_label = None

        self.root = root
        self.root.title("IPv4 Subnet Calculator")
        self.root.geometry("500x600")
        self.create_widgets()

    def create_widgets(self):
        # IP Address Input
        ip_label = tk.Label(self.root, text="IP Address:")
        ip_label.pack(pady=5)
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack(pady=5)

        # Subnet Mask Input
        subnet_label = tk.Label(self.root, text="Subnet Mask (CIDR or Dotted Decimal):")
        subnet_label.pack(pady=5)
        self.subnet_entry = tk.Entry(self.root)
        self.subnet_entry.pack(pady=5)

        # Calculate Button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_subnet)
        calculate_button.pack(pady=10)

        # Output Labels
        self.network_label = tk.Label(self.root, text="Network Address:")
        self.network_label.pack(pady=5)

        self.broadcast_label = tk.Label(self.root, text="Broadcast Address:")
        self.broadcast_label.pack(pady=5)

        self.host_range_label = tk.Label(self.root, text="Host Range:")
        self.host_range_label.pack(pady=5)

        self.total_ips_label = tk.Label(self.root, text="Total IP Addresses:")
        self.total_ips_label.pack(pady=5)

        self.usable_hosts_label = tk.Label(self.root, text="Usable Hosts:")
        self.usable_hosts_label.pack(pady=5)

        self.subnet_mask_label = tk.Label(self.root, text="Subnet Mask:")
        self.subnet_mask_label.pack(pady=5)

        self.wildcard_mask_label = tk.Label(self.root, text="Wildcard Mask:")
        self.wildcard_mask_label.pack(pady=5)

        self.cidr_label = tk.Label(self.root, text="CIDR Notation:")
        self.cidr_label.pack(pady=5)

        self.ip_class_label = tk.Label(self.root, text="IP Class:")
        self.ip_class_label.pack(pady=5)

        self.binary_ip_label = tk.Label(self.root, text="Binary IP:")
        self.binary_ip_label.pack(pady=5)

        self.binary_subnet_label = tk.Label(self.root, text="Binary Subnet Mask:")
        self.binary_subnet_label.pack(pady=5)

    def calculate_subnet(self):
        ip_input = self.ip_entry.get()
        subnet_input = self.subnet_entry.get()

        try:
            ip_interface = subnet_logic.validate_ip_and_subnet(ip_input, subnet_input)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

        # Network address
        network = subnet_logic.calculate_network_address(ip_interface)
        self.network_label.config(text=f"Network Address: {network}")

        # Broadcast address
        broadcast = subnet_logic.calculate_broadcast_address(ip_interface)
        self.broadcast_label.config(text=f"Broadcast Address: {broadcast}")

        # First and last usable host addresses
        first_host, last_host = subnet_logic.calculate_host_range(ip_interface)
        if first_host and last_host:
            self.host_range_label.config(text=f"Host Range: {first_host} - {last_host}")
        else:
            self.host_range_label.config(text="Host Range: N/A")

        # Total IP addresses
        total_ips = subnet_logic.get_total_ips(ip_interface)
        self.total_ips_label.config(text=f"Total IP Addresses: {total_ips}")

        # Number of usable hosts
        num_hosts = subnet_logic.calculate_usable_hosts(ip_interface)
        self.usable_hosts_label.config(text=f"Usable Hosts: {num_hosts}")

        # Subnet mask in dotted decimal
        subnet_mask = subnet_logic.get_subnet_mask(ip_interface)
        self.subnet_mask_label.config(text=f"Subnet Mask: {subnet_mask}")

        # Wildcard mask
        wildcard_mask = subnet_logic.get_wildcard_mask(ip_interface)
        self.wildcard_mask_label.config(text=f"Wildcard Mask: {wildcard_mask}")

        # Subnet mask in CIDR notation
        cidr_notation = subnet_logic.get_cidr_notation(ip_interface)
        self.cidr_label.config(text=f"CIDR Notation: /{cidr_notation}")

        # IP Class
        ip_class = subnet_logic.get_ip_class(ip_interface.ip)
        self.ip_class_label.config(text=f"IP Class: {ip_class}")

        # Binary IP
        binary_ip = subnet_logic.ip_to_binary(ip_interface.ip)
        self.binary_ip_label.config(text=f"Binary IP: {binary_ip}")

        # Binary Subnet Mask
        binary_subnet = subnet_logic.ip_to_binary(subnet_mask)
        self.binary_subnet_label.config(text=f"Binary Subnet Mask: {binary_subnet}")
