import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pyvisa
from time import sleep
import os
from math import floor
# import spectral_analysis as sa
import numpy as np
import matplotlib.pyplot as plt

class OSAControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OSA Control Interface")

        self.connected = False
        self.repeat_sweeps = False

        # Layout: Left for plot, right for controls
        
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill='both', expand=True)

        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side='left', fill='both', expand=True)

        self.right_frame = ttk.Frame(self.main_frame, padding=10)
        self.right_frame.pack(side='right', fill='y')

        style = ttk.Style()
        bold_font = tk.font.Font(family="Helvetica", size=12, weight="bold")
        style.configure("Bold.TLabel", font=bold_font)
        style.configure("Red.TButton", foreground="red")
        style.configure("Green.TButton", foreground="green")
        style.configure("Black.TButton", foreground="black")

        self.setup_plot()
        self.setup_connection_panel()
        self.setup_sweep_panel()
        self.setup_control_panel()
        self.setup_save_panel()
        self.setup_term_panel()

        self.check_folders()

    def setup_plot(self):
        self.figure = Figure(figsize=(5, 4), dpi=100, tight_layout = True)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Spectrum from OSA")
        self.ax.set_xlabel("Wavelength (nm)")
        self.ax.set_ylabel(r"Intensity ($\mu$W/nm)")

        self.line, = self.ax.plot([], [], color = "darkviolet")
        self.ax.grid()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.left_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

    def setup_connection_panel(self):
        conn_frame = ttk.LabelFrame(self.right_frame, text="Connection")
        conn_frame.pack(fill='x', pady=5)

        ttk.Label(conn_frame, text="IP Address:").grid(row=0, column=0, sticky='w')
        self.ip_entry = ttk.Entry(conn_frame)
        self.ip_entry.insert(0, "10.112.161.149")
        self.ip_entry.grid(row=0, column=1)

        ttk.Label(conn_frame, text="Port:").grid(row=1, column=0, sticky='w')
        self.port_entry = ttk.Entry(conn_frame)
        self.port_entry.insert(0, "10001")
        self.port_entry.grid(row=1, column=1)

        self.connect_button = ttk.Button(conn_frame, text="Connect", command=self.connect_to_osa)
        self.connect_button.grid(row=2, column=0, columnspan=2, pady=5)

    def setup_control_panel(self):
        control_frame = ttk.LabelFrame(self.right_frame, text="Controls")
        control_frame.pack(fill='x', pady=5)

        ttk.Label(control_frame, text="Centre (nm):").grid(row=0, column=0, sticky='w')
        self.centre_entry = ttk.Entry(control_frame, width = 20)
        self.centre_entry.insert(0, "1555")
        self.centre_entry.grid(row=0, column=1)

        ttk.Label(control_frame, text="Span (nm):").grid(row=1, column=0, sticky='w')
        self.span_entry = ttk.Entry(control_frame, width = 20)
        self.span_entry.insert(0, "10")
        self.span_entry.grid(row=1, column=1)

        ttk.Label(control_frame, text="Sensitivity:").grid(row=2, column=0, sticky='w')
        self.speed_combo = ttk.Combobox(control_frame, values=["norm", "mid", "high1", "high2", "high3"], width = 17)
        self.speed_combo.current(1)
        self.speed_combo.grid(row=2, column=1)

        ttk.Label(control_frame, text="Resolution (nm):").grid(row=3, column=0, sticky='w')
        self.resolution_combo = ttk.Combobox(control_frame, values=["0.05", "0.1", "0.2", "0.5", "1", "2"], width = 17)
        self.resolution_combo.current(0)
        self.resolution_combo.grid(row=3, column=1)

    def setup_sweep_panel(self):
        control_frame = ttk.LabelFrame(self.right_frame, text="Sweep")
        control_frame.pack(fill='x', pady=5)

        self.single_button = ttk.Button(control_frame, text="Single", command=self.single)
        self.single_button.grid(row=0, column=0, pady=5)

        self.stop_button = ttk.Button(control_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, pady=5)

        self.repeat_button = ttk.Button(control_frame, text="Repeat", command=self.repeat)
        self.repeat_button.grid(row=1, column=0, pady=5)

        self.auto_button = ttk.Button(control_frame, text="Auto", command=self.auto)
        self.auto_button.grid(row=1, column=1, pady=5)

    def setup_save_panel(self):
        save_frame = ttk.LabelFrame(self.right_frame, text="Save Data")
        save_frame.pack(fill='x', pady=5)

        ttk.Label(save_frame, text="Name:").grid(row=0, column=0, sticky='w')
        self.path_entry = ttk.Entry(save_frame)
        self.path_entry.grid(row=0, column=1)

        self.savepng_button = ttk.Button(save_frame, text="Save .png", command=self.save_png)
        self.savepng_button.grid(row=1, column=0, columnspan = 1, pady=5, sticky = "nsew")
        self.savecsv_button = ttk.Button(save_frame, text="Save .csv", command=self.save_csv)
        self.savecsv_button.grid(row=2, column=0, columnspan=1, pady=5, sticky = "nsew")

    def setup_term_panel(self):
        self.terminal_frame = ttk.Frame(self.right_frame)
        self.terminal_frame.pack(fill='x', pady=5)
        self.term_label = ttk.Label(self.terminal_frame, 
                                        text = "🤖: Hi! I will keep you updated!",
                                        wraplength = 250,       # pixels
                                        justify = "left",   
                                        anchor = "w")
        self.term_label.grid(row = 0, column = 0)

    def talk(self, text):
        text_out = text
        if type(text) != type("string"):
            text_out = str(text)
        self.term_label.configure(text = "🤖: " + text_out)


    def check_folders(self):

        folder1 = os.path.join(os.getcwd(), "pics")
        folder2 = os.path.join(os.getcwd(), "data")

        # Check and create if missing
        for folder in [folder1, folder2]:
            if not os.path.exists(folder):
                os.makedirs(folder)
                self.talk("I created folders, where I will save your data and images. You can thank me later.")
            else:
                pass



    # ---------------- Placeholder Callbacks ----------------

    def connect_to_osa(self):
        if not self.connected:
            self.ip = self.ip_entry.get()
            self.port = self.port_entry.get()
            self.address = "TCPIP::" + self.ip + "::" + self.port + "::SOCKET"

            self.rm = pyvisa.ResourceManager()
            try:
                self.osa = self.rm.open_resource(self.address)

                self.osa.read_termination = "\r\n"
                self.osa.write_termination = "\r\n"
                #self.osa.timeout = 10000  # 10 seconds
                self.osa.query("OPEN \"anonymous\"")
                self.osa.query("password")

                self.connect_button.configure(text = "Connected", style = "Green.TButton")
                self.talk("You connected to OSA!")
                self.connected = True

            except:
                self.connect_button.configure(text = "Error", style = "Red.TButton")
                self.talk("PyVISA Resource Manager failed to reach the device. Please, double check the IP and port.")

        else:
            self.osa.close()
            self.connect_button.configure(text = "Connect", style = "Black.TButton")
            self.connected = False
            self.talk("You disconnected from OSA.")


    def single(self):
        self.upload_settings()
        self.repeat_sweeps = False

        # initiate sweep
        self.osa.write(':init:smode SING')
        self.osa.write('*CLS')                   # clean status
        self.osa.write(":init")

        # wait till sweep finishes
        while True:
            sleep(0.1)
            status = int(self.osa.query(":stat:oper:even?"))
            if status == 1:
                self.talk("Single sweep completed!")
                break

        self.download_data()

        self.auto_button.configure(style = "Black.TButton")
        self.repeat_button.configure(style = "Black.TButton")

    def auto(self):
        self.talk("Initiating auto sweep...")
        self.upload_settings()

        # initiate sweep
        def initiate_sweep():
            self.osa.write(':init:smode AUTO')
            self.osa.write('*CLS')                   # clean status
            self.osa.write(":init")
        
            for i in range(200):
                sleep(0.1)
                status = int(self.osa.query(":stat:oper:even?"))
                if status == 16:
                    self.talk("Auto sweep calibrated! Sweeping...")
                    self.repeat_sweeps = True
                    self.download_data_non_stop()

                    self.auto_button.configure(style = "Green.TButton")
                    self.repeat_button.configure(style = "Black.TButton")
                    #self.span_entry.insert(0, str(round(1e9*float(self.osa.query(':sens:wav:span?')),1)))
                    #self.centre_entry.insert(0, str(round(1e9*float(self.osa.query(':sens:wav:cent?')),1)))

                    break
            
            if not self.repeat_sweeps:
                self.stop()
                self.auto_button.configure(style = "Red.TButton")
                self.talk("Damn, failed to perform auto sweep. Are you sure, there is any light in the fiber?")

        self.root.after(100, initiate_sweep) # this is a bit weird construction, but I did it just to make robot talk
        

    def stop(self):
        self.repeat_sweeps = False
        self.osa.write(":ABOR")
        self.talk("Sweeping stopped.")

        self.auto_button.configure(style = "Black.TButton")
        self.repeat_button.configure(style = "Black.TButton")

    def repeat(self):
        self.upload_settings()
        self.repeat_sweeps = True

        # initiate sweep
        self.osa.write(':init:smode REP')
        self.osa.write('*CLS')                   # clean status
        self.osa.write(":init")
        self.talk("Sweeping...")
        self.download_data_non_stop()

        self.auto_button.configure(style = "Black.TButton")
        self.repeat_button.configure(style = "Green.TButton")    
               
    def download_data_non_stop(self):
        self.download_data()
        if self.repeat_sweeps:
            self.root.after(500, self.download_data_non_stop)

    def download_data(self):
        self.xdata = self.osa.query(":trac:data:X? TRA")
        self.ydata = self.osa.query(":trac:data:Y? TRA")

        def csv_string_to_array(csv_str):
            # Split the string by commas, strip whitespace, and convert to float
            values = [float(val.strip()) for val in csv_str.strip().split(',')]
            return np.array(values)

        self.xdata = csv_string_to_array(self.xdata)*1e9
        self.ydata = csv_string_to_array(self.ydata)

        self.osa.write(":disp:trac:Y1:rlev " + str(1.05*np.max(self.ydata)/1000))

        self.show_plot()

    def upload_settings(self):
        self.osa.write(':sens:wav:cent ' + self.centre_entry.get() + 'nm')
        self.osa.write(':sens:wav:span ' + self.span_entry.get() + 'nm')
        self.osa.write(":sens:sens " + self.speed_combo.get())
        self.osa.write(":disp:trac:Y1:spac " + "LIN")
        self.osa.write(":sens:band:res " + self.resolution_combo.get() + 'nm')

    def show_plot(self):
        self.line.set_xdata(self.xdata)
        self.line.set_ydata(self.ydata)
        self.ax.set_xlim(self.xdata[0], self.xdata[-1])
        self.ax.set_ylim(0, 1.1*np.max(self.ydata))      
        self.canvas.draw()

    def save_csv(self):
        self.name = self.path_entry.get()
        path = os.getcwd() + "/data/" + self.name + ".csv"
        data_out = np.stack((self.xdata, self.ydata))
        np.savetxt(path, data_out, delimiter = ",")
        self.talk("You saved " + self.name + ".csv!")

    def save_png(self):
        self.name = self.path_entry.get()
        self.path = os.getcwd() + "/pics/" + self.name
        self.figure.savefig(self.path)
        self.talk("You saved " + self.name + ".png!")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = OSAControlApp(root)
    root.mainloop()
