import tkinter as tk
import nmap

def get_port():
  # Get the host name from the entry widget.
  host = entry.get()

  # Create an Nmap scan object.
  scan = nmap.PortScanner()

  # Scan the host for open ports.
  scan.scan(host, '1-65535')

  # Get the list of open ports.
  open_ports = scan.get_open_ports()

  # Print the list of open ports.
  for port in open_ports:
    print(port)

def main():
  # Create the main window.
  window = tk.Tk()

  # Create the entry widget.
  

  # Create the button widget.
  button = tk.Button(window, text="Get Port", command=get_port)
  button.pack()

  # Start the main loop.
  window.mainloop()

if __name__ == "__main__":
  main()