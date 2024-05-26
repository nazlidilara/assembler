import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from assembler import Assembler

class AssemblerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Assembler")
        self.root.geometry("900x700")
        
        # Stil ayarları
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Genel stil
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#FFFFFF', background='#4B0082')
        self.style.configure('TLabel', font=('Helvetica', 12, 'bold'), foreground='#333333')
        self.style.configure('TEntry', font=('Helvetica', 12), padding=5)
        self.style.configure('TText', font=('Helvetica', 12), padding=5)
        
        # Sekmeler için stil
        self.style.configure('TNotebook.Tab', font=('Helvetica', 12, 'bold'), padding=[10, 5])
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#1E90FF')
        header_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        
        header_label = tk.Label(header_frame, text="Assembler ", bg='#1E90FF', fg='white', font=('Helvetica', 16, 'bold'))
        header_label.pack(pady=10)
        
        # Input file section
        self.file_label = ttk.Label(self.root, text="Giris dosyanizi seciniz:")
        self.file_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.file_entry = ttk.Entry(self.root, width=50)
        self.file_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        
        self.browse_button = ttk.Button(self.root, text="Ara", command=self.browse_file, style='Accent.TButton')
        self.browse_button.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
        
        self.assemble_button = ttk.Button(self.root, text="Assemble et", command=self.assemble, style='Accent.TButton')
        self.assemble_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.error_label = tk.Label(self.root, text="", fg="red", bg='#D3D3D3', font=('Helvetica', 12, 'bold'))
        self.error_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.tab_control = ttk.Notebook(self.root)
        
        self.object_code_tab = tk.Frame(self.tab_control, bg='#D3D3D3')
        self.output_file_tab = tk.Frame(self.tab_control, bg='#D3D3D3')
        self.symbol_table_tab = tk.Frame(self.tab_control, bg='#D3D3D3')
        
        self.tab_control.add(self.object_code_tab, text="Object Kod")
        self.tab_control.add(self.output_file_tab, text="HTE Kayitlari")
        self.tab_control.add(self.symbol_table_tab, text="Sembol Tablosu")
        
        self.tab_control.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        
        self.object_code_text = tk.Text(self.object_code_tab, wrap='word', font=('Helvetica', 12), bg='#F0F0F0')
        self.object_code_text.pack(expand=1, fill='both', padx=10, pady=10)
        
        self.output_file_text = tk.Text(self.output_file_tab, wrap='word', font=('Helvetica', 12), bg='#F0F0F0')
        self.output_file_text.pack(expand=1, fill='both', padx=10, pady=10)
        
        self.symbol_table_text = tk.Text(self.symbol_table_tab, wrap='word', font=('Helvetica', 12), bg='#F0F0F0')
        self.symbol_table_text.pack(expand=1, fill='both', padx=10, pady=10)
        
        # Arka plan renkleri
        self.root.configure(bg='#D3D3D3')
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
    
    def assemble(self):
        input_file = self.file_entry.get()
        if not input_file:
            self.error_label.config(text="Lutfen Input dosyanizi seciniz.")
            return
        
        assembler = Assembler()
        try:
            assembler.execute(input_file, "output.txt")
            self.error_label.config(text="")
        except Exception as e:
            self.error_label.config(text=f"Assembly failed: {str(e)}")
            return
        
        self.update_object_code_text()
        self.update_output_file_text()
        self.update_symbol_table_text()
        messagebox.showinfo("SONUC", "Assembly islemi basarili.")
    
    def update_object_code_text(self):
        try:
            with open("object_code.txt", "r") as file:
                object_code = file.read()
            self.object_code_text.delete(1.0, tk.END)
            self.object_code_text.insert(tk.END, object_code)
        except FileNotFoundError:
            self.object_code_text.delete(1.0, tk.END)
            self.object_code_text.insert(tk.END, "Error: 'object_code.txt' not found.")
        except Exception as e:
            self.object_code_text.delete(1.0, tk.END)
            self.object_code_text.insert(tk.END, f"Error reading 'object_code.txt': {str(e)}")
    
    def update_output_file_text(self):
        try:
            with open("output.txt", "r") as file:
                output_file = file.read()
            self.output_file_text.delete(1.0, tk.END)
            self.output_file_text.insert(tk.END, output_file)
        except FileNotFoundError:
            self.output_file_text.delete(1.0, tk.END)
            self.output_file_text.insert(tk.END, "Error: 'output.txt' not found.")
        except Exception as e:
            self.output_file_text.delete(1.0, tk.END)
            self.output_file_text.insert(tk.END, f"Error reading 'output.txt': {str(e)}")

    def update_symbol_table_text(self):
        try:
            with open("symtab.txt", "r") as file:
                symbol_table = file.read()
            self.symbol_table_text.delete(1.0, tk.END)
            self.symbol_table_text.insert(tk.END, symbol_table)
        except FileNotFoundError:
            self.symbol_table_text.delete(1.0, tk.END)
            self.symbol_table_text.insert(tk.END, "Error: 'symtab.txt' not found.")
        except Exception as e:
            self.symbol_table_text.delete(1.0, tk.END)
            self.symbol_table_text.insert(tk.END, f"Error reading 'symtab.txt': {str(e)}")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = AssemblerGUI(root)
    root.mainloop()
